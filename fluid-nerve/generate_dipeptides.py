"""Generate an atom-based capped-dipeptide family Ace-X-NMe (20 standard amino acids) with OpenMM.

Protocol (recorded in data/dipeptides/<X>/protocol.json):
  amber14 (ff14SB) + GBn2 implicit solvent, no cutoff, HBonds constrained, 2 fs,
  LangevinMiddle 300 K / 1 ps^-1, 100 ps equilibration discarded, production DIPEP_NS (default 10) ns per run,
  3 independent runs per peptide (seeds 1,2,3), all-atom positions saved every 1 ps (nm).
Starting structure: the mdshare alanine-dipeptide topology mutated with PDBFixer (ALA-2-X).
These are new, small-scale simulations for descriptive geometry, not converged thermodynamics.
"""
import json, os, sys, time, hashlib
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data/dipeptides"
TEMPLATE = ROOT.parent / "alanine-nerve/data/alanine-dipeptide-nowater.pdb"
AMINO = ["ALA","ARG","ASN","ASP","CYS","GLN","GLU","GLY","HIS","ILE",
         "LEU","LYS","MET","PHE","PRO","SER","THR","TRP","TYR","VAL"]
PROD_NS = float(os.environ.get("DIPEP_NS", "10"))
EQ_PS = 100.0
SAVE_PS = 1.0
DT_FS = 2.0


def build(aa):
    """Mutate the alanine dipeptide template to Ace-X-NMe; write a PDB; return paths."""
    import openmm.app as app, openmm.unit as u
    from pdbfixer import PDBFixer
    folder = OUT / aa; folder.mkdir(parents=True, exist_ok=True)
    pdb_path = folder / f"{aa}_dipeptide.pdb"
    if pdb_path.exists():
        return pdb_path
    fixer = PDBFixer(filename=str(TEMPLATE))
    if aa != "ALA":
        fixer.applyMutations([f"ALA-2-{aa}"], "X")
    fixer.findMissingResidues(); fixer.findMissingAtoms(); fixer.addMissingAtoms()
    # Remove all hydrogens then re-add with the force field conventions (pH 7).
    modeller = app.Modeller(fixer.topology, fixer.positions)
    modeller.delete([a for a in modeller.topology.atoms() if a.element.symbol == "H"])
    ff = app.ForceField("amber14-all.xml", "implicit/gbn2.xml")
    modeller.addHydrogens(ff, pH=7.0)
    with open(pdb_path, "w") as f:
        app.PDBFile.writeFile(modeller.topology, modeller.positions, f, keepIds=True)
    return pdb_path


def run(job):
    aa, seed, platform = job
    import openmm as mm, openmm.app as app, openmm.unit as u
    t0 = time.time()
    folder = OUT / aa; pdb_path = build(aa)
    out = folder / f"run-{seed}.npz"
    if out.exists():
        return aa, seed, "exists"
    pdb = app.PDBFile(str(pdb_path))
    ff = app.ForceField("amber14-all.xml", "implicit/gbn2.xml")
    system = ff.createSystem(pdb.topology, nonbondedMethod=app.NoCutoff, constraints=app.HBonds)
    integ = mm.LangevinMiddleIntegrator(300*u.kelvin, 1/u.picosecond, DT_FS*u.femtoseconds)
    integ.setRandomNumberSeed(seed)
    props = {"Threads": "1"} if platform == "CPU" else {"Precision": "mixed"}
    sim = app.Simulation(pdb.topology, system, integ, mm.Platform.getPlatformByName(platform), props)
    steps_per_save = int(round(SAVE_PS*1000/DT_FS))
    n_save = int(round(PROD_NS*1000/SAVE_PS))
    heavy = np.array([a.element.symbol != "H" for a in pdb.topology.atoms()])
    pos = np.zeros((n_save, pdb.topology.getNumAtoms(), 3), np.float32)
    energy = np.zeros(n_save, np.float32)
    partial = folder / f"run-{seed}.partial.npz"
    resumed = 0
    if partial.exists():
        z = np.load(partial)
        resumed = min(len(z["positions"]), n_save)
        pos[:resumed] = z["positions"][:resumed]; energy[:resumed] = z["energy"][:resumed]
        # Continue from the last saved positions with freshly drawn velocities (position-continuous restart).
        sim.context.setPositions(pos[resumed-1].astype(np.float64) * u.nanometer)
        sim.context.setVelocitiesToTemperature(300*u.kelvin, seed + 1000)
        sim.step(int(2000/DT_FS))  # 2 ps re-thermalisation
    else:
        sim.context.setPositions(pdb.positions)
        sim.minimizeEnergy()
        sim.context.setVelocitiesToTemperature(300*u.kelvin, seed)
        sim.step(int(EQ_PS*1000/DT_FS))
    for k in range(resumed, n_save):
        sim.step(steps_per_save)
        st = sim.context.getState(getPositions=True, getEnergy=True)
        pos[k] = st.getPositions(asNumpy=True).value_in_unit(u.nanometer)
        energy[k] = st.getPotentialEnergy().value_in_unit(u.kilojoule_per_mole)
        if k % 5000 == 4999:
            np.savez_compressed(folder / f"run-{seed}.partial.npz", positions=pos[:k+1], energy=energy[:k+1])
    np.savez_compressed(out, positions=pos, energy=energy, heavy=heavy,
                        atom_names=np.array([a.name for a in pdb.topology.atoms()]),
                        residues=np.array([a.residue.name for a in pdb.topology.atoms()]),
                        elements=np.array([a.element.symbol for a in pdb.topology.atoms()]))
    (folder / f"run-{seed}.partial.npz").unlink(missing_ok=True)
    proto = dict(forcefield=["amber14-all.xml", "implicit/gbn2.xml"], temperatureK=300, frictionPerPs=1,
                 timestepFs=DT_FS, constraints="HBonds", nonbonded="NoCutoff", integrator="LangevinMiddle",
                 equilibrationPs=EQ_PS, productionNs=PROD_NS, savePs=SAVE_PS, seed=seed,
                 platform=platform, openmm=mm.__version__, template=str(TEMPLATE.name),
                 resumed_from_partial_frames=int(resumed),
                 template_sha256=hashlib.sha256(TEMPLATE.read_bytes()).hexdigest(),
                 mutation=None if aa == "ALA" else f"ALA-2-{aa}", wall_seconds=round(time.time()-t0),
                 finished=time.strftime("%Y-%m-%dT%H:%M:%S"))
    (folder / f"run-{seed}.protocol.json").write_text(json.dumps(proto, indent=2))
    return aa, seed, f"{round(time.time()-t0)} s"


if __name__ == "__main__":
    workers = int(os.environ.get("DIPEP_WORKERS", "14"))
    gpu_share = int(os.environ.get("DIPEP_GPU_JOBS", "6"))   # of each `workers` consecutive jobs, this many use OpenCL
    jobs = [(aa, seed) for seed in (1, 2, 3) for aa in AMINO]
    jobs = [(aa, seed, "OpenCL" if (i % workers) < gpu_share else "CPU") for i, (aa, seed) in enumerate(jobs)]
    OUT.mkdir(parents=True, exist_ok=True)
    for aa in AMINO:
        try: build(aa); print("built", aa, flush=True)
        except Exception as e: print("BUILD FAILED", aa, e, flush=True)
    with ProcessPoolExecutor(max_workers=workers) as ex:
        for res in ex.map(run, jobs):
            print(*res, flush=True)

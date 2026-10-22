"""Loaders that turn each raw source into runs of site coordinates (nm) plus provenance.

Every loader returns a dict:
  runs        list of float32 arrays (n_frames, n_sites, 3) in nm, one per independent trajectory
  run_meta    list of dicts (file, temperature, replica, ...)
  sites       list of site labels
  chart       None, or list of (n_frames, 2) arrays when the chart is a precomputed dihedral pair
  clock_ps    picoseconds between saved frames, or None when the physical clock is unresolved
  info        provenance (source, license, hashes, selection rules, caveats)
"""
import json
import hashlib
from pathlib import Path
import numpy as np
from .geometry import dihedral

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT.parent / "alanine-nerve"
DATA = ROOT / "data"


def sha256(path, limit=None):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 24), b""):
            h.update(chunk)
    return h.hexdigest()


def load_ala2():
    """mdshare alanine dipeptide: 3 x 250 ns, 1 ps, 10 heavy atoms, phi/psi supplied."""
    coords = np.load(ATLAS / "data/alanine-dipeptide-3x250ns-heavy-atom-positions.npz")
    angles = np.load(ATLAS / "data/alanine-dipeptide-3x250ns-backbone-dihedrals.npz")
    runs = [coords[k].reshape(-1, 10, 3).astype(np.float32) for k in coords]
    chart = [np.rad2deg(angles[k]).astype(np.float64) for k in angles]
    sites = ["ACE_CH3", "ACE_C", "ACE_O", "ALA_N", "ALA_CA", "ALA_CB", "ALA_C", "ALA_O", "NME_N", "NME_CH3"]
    info = dict(source="https://markovmodel.github.io/mdshare/ALA2/", license="upstream terms (mdshare)",
                files={p.name: sha256(p) for p in [ATLAS / "data/alanine-dipeptide-3x250ns-heavy-atom-positions.npz",
                                                     ATLAS / "data/alanine-dipeptide-3x250ns-backbone-dihedrals.npz"]},
                temperatureK=300, note="Heavy-atom positions as supplied (nm); site order as in the mdshare topology.")
    return dict(runs=runs, run_meta=[dict(run=i) for i in range(3)], sites=sites, chart=chart, clock_ps=1.0, info=info)


def load_dipeptide(aa):
    """Locally generated Ace-X-NMe (OpenMM, amber14/GBn2, 300 K); heavy atoms; phi/psi computed here."""
    folder = DATA / "dipeptides" / aa
    files = sorted(folder.glob("run-*.npz"))
    files = [f for f in files if ".partial" not in f.name]
    if not files:
        raise FileNotFoundError(f"no finished runs for {aa}")
    runs, chart, meta = [], [], []
    sites = None
    for f in files:
        z = np.load(f)
        pos = z["positions"].astype(np.float32)
        heavy = z["heavy"]
        names = [str(x) for x in z["atom_names"]]
        res = [str(x) for x in z["residues"]]
        def idx(resname, atom):
            return next(i for i, (r, a) in enumerate(zip(res, names)) if r == resname and a == atom)
        c0, n1, ca, c1, n2 = idx("ACE", "C"), idx(aa, "N"), idx(aa, "CA"), idx(aa, "C"), idx("NME", "N")
        phi = dihedral(pos[:, c0], pos[:, n1], pos[:, ca], pos[:, c1])
        psi = dihedral(pos[:, n1], pos[:, ca], pos[:, c1], pos[:, n2])
        runs.append(pos[:, heavy])
        chart.append(np.column_stack([phi, psi]))
        proto = json.loads(f.with_name(f.name.replace(".npz", ".protocol.json")).read_text()) if f.with_name(f.name.replace(".npz", ".protocol.json")).exists() else {}
        meta.append(dict(file=f.name, sha256=sha256(f), seed=proto.get("seed"), wall_seconds=proto.get("wall_seconds")))
        if sites is None:
            sites = [f"{r}_{a}" for r, a, h in zip(res, names, heavy) if h]
    info = dict(source="generate_dipeptides.py (this repository)", license="original data of this repository",
                forcefield="amber14-all + implicit/gbn2", temperatureK=300, protocol=str(folder / "run-1.protocol.json"),
                note="Small new implicit-solvent simulations for descriptive geometry; not converged thermodynamics.")
    return dict(runs=runs, run_meta=meta, sites=sites, chart=chart, clock_ps=1.0, info=info)


SGDML_CLOCK_FS = {"md17": 0.5, "md22": 1.0}


def load_sgdml(name):
    """MD17 / MD22 ab initio MD (quantum-machine.org). Heavy atoms; single trajectory; time order checked."""
    manifest = json.loads((DATA / "sgdml/manifest.json").read_text())
    rec = manifest[name]
    path = DATA / "sgdml" / rec["file"]
    z = np.load(path, allow_pickle=True)
    R = z["R"].astype(np.float32) / 10.0  # Angstrom -> nm
    Z = z["z"]
    heavy = Z > 1
    symbols = {1: "H", 6: "C", 7: "N", 8: "O", 16: "S"}
    sites = [f"{symbols.get(int(a), str(a))}{i}" for i, a in enumerate(Z) if a > 1]
    X = R[:, heavy]
    # time-order diagnostic: consecutive vs random-pair RMSD
    rng = np.random.default_rng(0)
    n = len(X)
    cons = np.sqrt(((X[1:] - X[:-1]) ** 2).sum(2).mean(1))
    a = rng.integers(0, n, 2000)
    b = rng.integers(0, n, 2000)
    rand = np.sqrt(((X[a] - X[b]) ** 2).sum(2).mean(1))
    ratio = float(np.median(cons) / np.median(rand))
    family = "md17" if name.startswith("md17") else "md22"
    info = dict(source=rec["url"], sha256=rec["sha256"], bytes=rec["bytes"], family=family,
                dataset_name=str(z["name"]) if "name" in z.files else name, theory=str(z["theory"]) if "theory" in z.files else None,
                nominal_timestep_fs=SGDML_CLOCK_FS[family], time_order_ratio=ratio,
                time_ordered=bool(ratio < 0.3),
                license="see sGDML / quantum-machine.org terms (Chmiela et al. 2017, 2023)",
                note="Single ab initio trajectory; nominal timestep from the dataset papers; hydrogens omitted from sites.")
    clock = SGDML_CLOCK_FS[family] / 1000.0 if ratio < 0.3 else None
    return dict(runs=[X], run_meta=[dict(file=rec["file"])], sites=sites, chart=None, clock_ps=clock, info=info)


def _parse_pdb_atoms(text):
    atoms = []
    for line in text.splitlines():
        if line.startswith(("ATOM", "HETATM")):
            name = line[12:16].strip()
            resn = line[17:20].strip()
            resi = line[22:26].strip()
            elem = line[76:78].strip() if len(line) >= 78 else ""
            if not elem:
                elem = "H" if name[:1] == "H" or (name[:1].isdigit() and name[1:2] == "H") else name[:1]
            atoms.append((name, resn, resi, elem.upper()))
    return atoms


MDCATH_TEMPS = [320, 348, 379, 413, 450]


def load_mdcath(domain, representation="ca", temperatures=None, max_frames_per_run=None):
    import h5py
    path = DATA / "mdcath" / f"mdcath_dataset_{domain}.h5"
    manifest = json.loads((DATA / "mdcath/manifest.json").read_text())
    with h5py.File(path, "r") as f:
        g = f[domain]
        atoms = _parse_pdb_atoms(g["pdbProteinAtoms"][()].decode())
        if representation == "ca":
            sel = np.array([a[0] == "CA" for a in atoms])
        else:
            sel = np.array([a[3] != "H" for a in atoms])
        sites = [f"{a[1]}{a[2]}_{a[0]}" for a, s in zip(atoms, sel) if s]
        runs, meta = [], []
        for T in (temperatures or MDCATH_TEMPS):
            for rep in range(5):
                key = f"{T}/{rep}"
                if key not in g:
                    continue
                c = g[key]["coords"]
                arr = c[:max_frames_per_run] if max_frames_per_run else c[()]
                runs.append((arr[:, sel] / 10.0).astype(np.float32))
                meta.append(dict(temperature=int(T), replica=int(rep), frames=int(len(arr))))
        attrs = {k: (int(v) if hasattr(v, "__int__") else str(v)) for k, v in g.attrs.items()}
    rec = manifest.get(domain, {})
    info = dict(source=rec.get("url"), sha256=rec.get("sha256"), bytes=rec.get("bytes"), license="CC BY 4.0",
                citation="Mirarchi, Giorgino & De Fabritiis, Sci Data 11, 1299 (2024)", domain=domain,
                attrs=attrs, representation=representation, frame_interval_ps=1000.0,
                note="Five temperatures x five replicas; frames saved every 1 ns per the dataset description.")
    return dict(runs=runs, run_meta=meta, sites=sites, chart=None, clock_ps=1000.0, info=info)


def load_cln025(max_runs=None):
    """CLN025 subset already present in alanine-nerve/data/chignolin (128 runs); C-alpha sites; clock unresolved."""
    import mdtraj as md
    src = ATLAS / "data/chignolin"
    manifest = json.loads((src / "manifest.json").read_text())
    top = md.load(str(src / "topology.pdb")).topology
    ca = top.select("name CA")
    runs, meta = [], []
    for rec in manifest["files"]:
        if not rec["file"].endswith(".xtc"):
            continue
        if max_runs and len(runs) >= max_runs:
            break
        t = md.load(str(src / rec["file"]), top=str(src / "topology.pdb"), atom_indices=ca)
        runs.append(t.xyz.astype(np.float32))
        meta.append(dict(file=rec["file"], member=rec["member"], sha256=rec["sha256"], frames=int(t.n_frames)))
    sites = [f"{top.atom(i).residue.name}{top.atom(i).residue.resSeq}_CA" for i in ca]
    info = dict(source=manifest["source"], doi=manifest["doi"], license=manifest["license"], variant=manifest["variant"],
                sequence=manifest["sequence"], temperatureK=manifest["temperatureK"], selection=manifest["selection"],
                note="Frame indices only; XTC timing metadata conflicts with nominal run lengths (see alanine-nerve/VALIDATION.md).")
    return dict(runs=runs, run_meta=meta, sites=sites, chart=None, clock_ps=None, info=info)

# PE globule screening workflow

The target is **8 PE50 replicas × 200 ns + 4 PE25 replicas × 100 ns = 2 microseconds of production**, plus equilibration. PE50 is C100H202; PE25 is C50H102. This is a single-chain packing/rearrangement screen, not a nanoplastic aggregate or a sheaf-training experiment yet.

## Run in Linux or Ubuntu WSL

From PowerShell, open the existing environment:

```powershell
wsl -d Ubuntu-22.04
```

Then:

```bash
cd /mnt/d/pronerv_MTNerv
bash bootstrap_wsl.sh
python3 pilot.py build --output smoke --smoke --candidates 16
python3 pilot.py run smoke/PE25/rep01 --threads 4
python3 pilot.py run smoke/PE50/rep01 --threads 4
python3 analyze.py smoke --discard-ns 0 --stride 1

# The scientific run: do not reuse smoke outputs.
python3 pilot.py build --output runs
python3 run_screen.py runs --threads 8
# On completion, or for provisional progress (missing runs are flagged):
python3 analyze.py runs
```

Builders refuse to overwrite an existing manifest. If the directories already exist, skip their build commands. A short smoke uses full minimization but only 1 ps each of NVT, NPT, and relaxation, and 2 ps production. It tests plumbing, never physics or equilibration.

Use `--gmx /absolute/path/to/gmx` on run and analysis commands to select a CUDA-enabled build. Ubuntu's packaged GROMACS 2021.4 is CPU-only on this installation. An optional local CUDA build is described in `build_gpu.sh`. Do not switch GROMACS versions in the middle of a scientific replica; record and retain the executable/version. Analysis uses GRO/XTC to avoid coupling to a particular MDAnalysis TPR parser version.

## Chemistry and provenance

The generator builds only neutral, hydrogen-terminated, saturated linear alkanes. Carbon sites are ordered along the backbone, followed by attached hydrogens. `pe.itp` enumerates every bond, angle, proper dihedral and unique graph-distance-three 1–4 pair. CHARMM functions are bond 1, Urey–Bradley angle 5, multiple proper torsion 9, pair 1, with nrexcl=3. There are no tetrahedral-carbon impropers for this achiral linear alkane.

Types and charges are explicitly checked against the official CGenFF propane (`PRPA`) residue: terminal CG331 −0.27, internal CG321 −0.18, HGA3/HGA2 +0.09. The homologous extension introduces no new chemical environments beyond alkane chains; all bonded terms must resolve from the archived force field through `grompp`. This is a documented alkane-template construction, **not a new CGenFF server assignment or a fitted PE parameter set**. No missing parameter is guessed and no `-maxwarn` is used. An external long-alkane benchmark remains necessary before physical rate claims.

The official July 2022 CHARMM GROMACS port includes CGenFF and CHARMM TIP3P. It is downloaded from the MacKerell laboratory. File hashes are recorded in every manifest. `spc216.gro` supplies initial three-site water coordinates only; the topology and subsequent rigid geometry are CHARMM TIP3P. No SPC interaction parameters are used. Full processed topologies and resolved MDPs are retained.

RDKit generates independent self-avoiding trans/gauche carbon chains and adds hydrogens. A brief MMFF geometry cleanup avoids severe local clashes; MMFF is **never used for reference dynamics**. A candidate pool is ranked by radius of gyration and trans fraction to produce compact, order-enriched, and expanded preparations. These labels are relative rankings, not verified crystals or equilibrium globules. The achieved metrics appear in metadata. PE50 has 3 compact / 3 order-enriched / 2 expanded starts; PE25 has 2 / 1 / 1. Every conformation is distinct and every velocity seed is distinct.

## Protocol

All times below are per replica:

| Stage | Duration | Settings |
|---|---:|---|
| Minimization | Up to 50,000 steps | Steepest descent, unconstrained polymer bonds, Fmax < 500 kJ/mol/nm |
| NVT | 0.5 ns | Carbon position restraints, 1000 kJ/mol/nm²; generate velocities |
| NPT | 5 ns | Unrestrained, 300 K, 1 bar, isotropic C-rescale; tau_p = 5 ps |
| NVT relaxation | 1 ns | Unrestrained, inherited equilibrated box and velocities |
| Production | 200 or 100 ns | Unrestrained NVT, continuous velocities |

2 fs timestep, normal masses, hydrogen-bond constraints, rigid water, global v-rescale at 300 K with tau_t=2 ps. PME, 1.2 nm electrostatic cutoff; LJ force switch 1.0–1.2 nm and no dispersion correction. No hydrogen-mass repartitioning, accelerated dynamics or bias potential. NVT uses the final NPT volume, not an asserted exact equilibrium mean; review density stability and extend NPT if needed.

The initial cubic box is at least 8 nm and enlarged to fit selected coils with 3 nm total Cartesian padding. All replicas of a chain length use the same initial box size. The analyzer checks periodic-image separation throughout production, using a conservative bounding-box lower bound or exact 26-neighbor image calculation when necessary. This does not replace a larger-box sensitivity study.

Production saves the full-system compressed trajectory every 1 ps and energies every 1 ps. It does not save a training-grade force/velocity dataset. About two million full-system frames may require hundreds of GB; check storage before launching the complete queue. High-frequency dynamics/force collection belongs in the subsequent learning study.

## Execution and recovery

`pilot.py run` logs all commands, stops on GROMACS warnings/errors, and resumes existing checkpoints. Stage completion is checked against the requested step count, so a clean `-maxh` exit is not mistaken for a finished trajectory. The serial queue runs one replica at a time, PE25 first. It never creates a paid remote job.

```bash
# Bounded execution; rerun the same command to continue from a checkpoint.
python3 pilot.py run runs/PE25/rep01 --maxh 0.25
# Run through preprocessing/minimization only.
python3 pilot.py run runs/PE50/rep01 --until em
# Solvate and check topology without executing MD.
python3 pilot.py run runs/PE50/rep01 --until prepare
```

Each active replica has a `RUNNING` lock containing its Python PID. After an abnormal OS termination, confirm the process is gone before deleting that lock. Never delete a live lock. A root-level `STOP` file stops the queue between stage-bounded invocations. To stop active MD promptly, send SIGTERM to its `gmx mdrun` PID so it checkpoints. Avoid SIGKILL. Check `queue_status.json` and replica logs for progress. Do not edit topologies or MDPs in a running/preprocessed replica; create a new output tree for protocol changes.

```bash
python3 status.py runs
# Optional detached local execution with persistent PID/log:
python3 launch.py runs --gmx "$PWD/vendor/gromacs-install/bin/gmx" --threads 8
```

The runner checks force-field hashes, input hashes and the GROMACS executable hash on resumption and rejects changed inputs. Library/build provenance is additionally recorded in the GROMACS version log.

## Analysis and decision

`analyze.py` reads full-system GRO/XTC files. It unwraps the ordered backbone using periodic displacements; it does not compute shape from a broken, wrapped chain. Each analyzed frame records:

- Backbone radius of gyration and relative shape anisotropy.
- Nonlocal C–C contacts below 0.5 nm with sequence separation at least four bonds, divided by carbon count.
- Backbone nematic alignment and trans fraction (within 30 degrees of trans).
- Unique water oxygens within 0.45 nm of any backbone carbon.
- Periodic-image clearance and maximum backbone C–C bond length.

Default analysis samples every 10 ps and discards the first 20 ns of production. The discard is a sensitivity choice, **not a guarantee of equilibration**. Repeat at 10/20/40 ns and inspect preparation dependence. Energy checks flag mean temperature outside 300 ± 5 K, NPT quarter-block density differences above 1%, missing outputs and LINCS/fatal errors. No automatic gate proves adequate equilibration.

Outputs are per-replica `observables.csv`, `candidate_states.csv`, `screening.png`, and root `screening_report.json`. A two-cluster fit to standardized structural features proposes candidate states for discovery only. Ambiguous assignments are excluded using a 15% distance margin, and uninterrupted residence of 100 ps is required before a crossing is counted. Counts at 50 and 200 ps expose flicker sensitivity. **Clustering always partitions data; it does not demonstrate metastability.**

The provisional `CANDIDATE_FOR_KINETIC_VALIDATION` gate requires all production runs complete and numerically clean, at least ten committed crossings in each direction, and recurrence in at least three replicas. These are exploratory crossings, not independent-event counts or rate estimates. Before proceeding, manually verify distinct packing/contact patterns, meaningful dwell/transition-time separation, robust counts under dwell and discard choices, and reasonable preparation mixing. Rapid continuous motion split by clustering must not be mistaken for two metastable states.

If no recurrence is detected, inspect whether there is one basin or arrested packing; consider PE25 or longer sampling. If only prepared coils collapse, report a preparation-conditioned collapse experiment, not reversible equilibrium kinetics. Do not estimate equilibrium populations from equal numbers of deliberately chosen starting classes. Freeze any accepted state definitions before the later held-out kinetic dataset. The eventual rate comparison still needs approximately 100 independent held-out events per direction for ~20% relative 95% precision under a simple Poisson approximation.

## Sources

- [Official CHARMM downloads and references](https://mackerell.umaryland.edu/charmm_ff.shtml)
- [GROMACS CHARMM settings](https://github.com/gromacs/gromacs/blob/main/docs/user-guide/force-fields.rst)
- [CGenFF formulation](https://pmc.ncbi.nlm.nih.gov/articles/PMC2888302/)
- [PE force-field benchmark](https://pubs.acs.org/doi/10.1021/acs.jpcb.6c02507)

The screen tests reproducibility of this force-field/water/thermostat model. It does not validate experimental PE transformation rates or demonstrate a sheaf-network advantage by itself.

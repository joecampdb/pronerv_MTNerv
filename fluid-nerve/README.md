# Fluid nerve atlas: many systems, deformation fields, ambient-time filtrations

This directory extends the two-system molecular atlas (alanine dipeptide, CLN025) to a catalog of
systems, half **atom-based** (heavy-atom sites) and half **backbone-based** (C-alpha sites), and adds
three constructions to the witnessed cover nerve of the measured revision:

| construction | what it is | where |
|---|---|---|
| deformation field | per-chart-bin conditional statistics of the lag-τ displacement: mobility *h* (RMS pair-distance change, nm), drift, spread, rigid-aligned site displacement; a ladder of lags | `dist/systems/<id>/field.npz`, `summary.json` |
| witnessed nerve | 18-ball cover, maximal simplices, face-poset nerve (objects/inclusions/triangles), GF(2) Betti numbers, radius sensitivity | `dist/systems/<id>/nerve.json` |
| fluid filtration | nerve of the cover thickened by ±τ frames along each run; Betti curves and persistence over ambient time | `summary.json` → `fluid_filtration` |
| flooding filtration | sublevel sets of −log occupancy on the chart (cubical, periodic on the torus); basin merge levels; the geometric analogue of metadynamics | `summary.json` → `flooding` |
| homotopy.io export | oriental encoding of each nerve as 0/1/2/3-cells, replayed through homotopy.io's proof model into `.hom` files | `dist/homotopy/<id>/`, `docs/homotopy-io-instructions.md` |
| comparison | within/between-group invariants, tests, embedding, atomistic→C-alpha comparison functor, temperature ladder | `dist/comparison/` |
| theory | *Fluid nerve theory* PDF: constructions, synthetic differential geometry (Kock–Lawvere), rigidity theorem, results | `dist/fluid-nerve-theory.pdf`, `theory/` |
| atlas PDF | legend in categorical terms, catalog of all systems, overview figures, one plate per system (3D biophysical object with the deformation field on the molecule, chart + annotated nerve, field, filtrations, categorical reading) | `dist/fluid-nerve-atlas.pdf`, `render_plate.py`, `make_atlas_pdf.py`, `make_legend.py` |
| video | pedagogical animation: how the nerve plate rises out of alanine dipeptide (molecule → chart → cover → deformation field → nerve → ambient time) | `dist/video/nerve-plate-alanine.mp4` (+ GIF preview), `make_video.py` |

> Descriptive constructions only. No equilibrium free energy, validated kinetics, calibrated uncertainty
> or configuration-space nerve theorem is claimed. See the paper's limitations section.

## Systems

`python -m fluidnerve.catalog` writes `catalog/systems.json` from whatever data is present:

- **atom group**: mdshare alanine dipeptide; twenty Ace-X-NMe capped dipeptides generated with OpenMM
  (`generate_dipeptides.py`: amber14/GBn2, 300 K, 3 × 10 ns, 1 ps frames); MD22 ab initio trajectories
  (Ac-Ala3-NHMe, DHA, stachyose, AT-AT, AT-AT-CG-CG) and MD17 trajectories (ethanol, malonaldehyde,
  aspirin, uracil, salicylic acid, toluene, naphthalene, paracetamol, azobenzene) from quantum-machine.org.
- **backbone group**: CLN025 (the 128-run subset in `../alanine-nerve/data/chignolin`); mdCATH CATH
  domains (`catalog/mdcath_selection.json` records the deterministic selection rule), five temperatures ×
  five replicas each, 1 ns frames, CC BY 4.0.
- **paired**: every mdCATH domain again with all heavy atoms on the same frames, used only for the
  atomistic → C-alpha comparison.

Charts: φ/ψ (periodic) for the dipeptide family; otherwise the two leading principal components of the
aligned site coordinates. Raw data live in ignored `data/`; every `summary.json` records URLs, SHA-256
hashes, selection rules and licences.

## Run

```bash
cd fluid-nerve
python acquire_sgdml.py                 # MD17 / MD22 npz files (+ manifest with SHA-256)
python acquire_mdcath.py                # selected mdCATH domains (~250 MB each)
python generate_dipeptides.py           # OpenMM dipeptide family (hours; DIPEP_NS / DIPEP_WORKERS env)
python build_all.py --workers 2         # fields, nerves, filtrations for every system with data
python render.py                        # per-system figures
python export_homotopy.py               # .hom files (needs the nerve_hom binary, see docs/)
python compare_all.py                   # comparative analysis + figures
python theory/make_results.py && tectonic theory/fluid-nerve-theory.tex --outdir dist
python render_plate.py                  # per-system atlas plates (needs representatives.npz from the build)
python make_legend.py && python make_atlas_pdf.py   # dist/fluid-nerve-atlas.pdf
python make_video.py                    # dist/video/nerve-plate-alanine.mp4 (needs ffmpeg)
python make_gallery.py                  # dist/index.html
bash pipeline.sh [--force]              # everything above after acquisition, in order
python -m unittest discover -s tests    # synthetic-data tests
```

`build_system.py <id>` builds one system; `--quick` subsamples for debugging. The alanine dipeptide
build reproduces the measured atlas of `../alanine-nerve` exactly (same centres, maximal simplices,
78/212/138 nerve, β = (3,3,0)).

## Layout

```
fluidnerve/        geometry (Kabsch, PCA, dihedrals), nerve (covers, GF(2) homology), field, filtration,
                   loaders (mdshare, OpenMM npz, sGDML npz, mdCATH h5, CLN025 xtc), catalog, homotopy_export
build_system.py    one system -> dist/systems/<id>/{summary.json, nerve.json, field.npz, membership.npz, chart.npz}
build_all.py       parallel driver
render.py          figures           compare_all.py   comparison        export_homotopy.py  homotopy.io
theory/            LaTeX source, generated tables, figures   docs/   homotopy.io instructions
tools/nerve_hom.rs the small Rust binary (built inside vendor/homotopy-rs, which is not committed)
tests/             unit tests on synthetic data
```

## Reading the outputs

- `summary.json`: provenance, chart, lag ladder, block length, per-lag field summaries, mobility
  exponent, nerve counts and Betti numbers, radius sensitivity, fluid filtration rows/pairs, flooding rows
  and basin pairs, mdCATH temperature ladder.
- `field.npz`: arrays over the 30×30 chart grid for every lag: `h`, `h_interval`, `support`, `count`,
  `v` (drift), `cov`; `u_ref` (site displacement at the reference lag); `occupancy`, `free`.
- `figure.png`: occupancy + nerve, mobility + drift arrows, fluid Betti curves, flooding Betti curves.

Intervals are block-resampling spread, not confidence intervals. Unsupported bins are null, never filled.

# Data, attribution and licensing

## Alanine dipeptide

- Metadata: https://markovmodel.github.io/mdshare/ALA2/
- Files: `alanine-dipeptide-3x250ns-heavy-atom-positions.npz`,
  `alanine-dipeptide-3x250ns-backbone-dihedrals.npz`, and topology PDB.
- Three 250 ns runs, 300 K, 1 ps sampling; 750,000 paired observations.
- Raw data are downloaded on demand and excluded from the current source tree.
  Earlier Git history contains raw alanine inputs and generated simulation artifacts;
  history is preserved rather than rewritten.
- Source-file hashes: `alanine-nerve/dist/data.json`.
- Upstream terms govern the original data; public availability is not a blanket
  license grant. This repository does not claim ownership of upstream trajectories.

## Chignolin CLN025

**Adrià Pérez Culubret and Gianni De Fabritiis (2021), Chignolin Simulations.**
https://doi.org/10.6084/m9.figshare.13858898

Licensed by the depositors under **CC BY 4.0**:
https://creativecommons.org/licenses/by/4.0/

The deposited system is **CLN025, YYDPETGTWY**. The full collection comprises
3,744 nominal 50 ns adaptive trajectories, 187.2 μs aggregate, at 350 K,
ACEMD/CHARMM22*/TIP3P.

This prototype selects the first 128 non-hidden XTC members in archive order:
63,999 frames, nominal 6.4 μs aggregate. This is a reproducible convenience sample,
not a representative random selection. Never concatenate runs for counting.

Changes: Cα selection, Å-to-nm conversion, centering, proper rigid alignment,
feature projection, clustering, density estimation, representative selection,
interpolation, Gaussian envelopes, mesh deformation and rendering.
The original authors do not endorse these transformations or interpretations.

`alanine-nerve/dist/chignolin/provenance.json` records exact member names,
per-file SHA-256, source URL and metadata. `data.json` preserves per-run XTC
timestamps. Their clock conflicts with nominal run lengths; analysis uses frame
indices. The archive's supplied MD5 is metadata, not independently verified.

## Software and other material

- Three.js/OrbitControls: MIT notice in `alanine-nerve/dist/THREE-LICENSE.txt`.
- Scientific packages and Blender have their own licenses and are not relicensed.
- Historical polyethylene files include third-party CHARMM force-field material
  already in repository history. Upstream terms apply. It is not needed by the atlas.
- Original atlas code, manuscript and figures are provided for inspection.
  No new blanket license is asserted over third-party inputs or historical files.
  Cite Joseph Campagna, PSM and the dataset authors when discussing this work.
  Contact the owner about reuse permissions beyond applicable upstream licenses.

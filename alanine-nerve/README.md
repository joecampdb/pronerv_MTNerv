# Molecular Atlas — developer and reproduction guide

Alanine dipeptide and chignolin CLN025 share a static Three.js viewer and
MD-derived deforming-skin construction. The directory name is historical.

## View without scientific dependencies

From this directory:

```bash
python -m http.server 8765 --directory dist
```

Open http://localhost:8765/ or http://localhost:8765/chignolin.html.
Browser dependencies are vendored. A WebGL-capable browser is required.

## Reproduce data and geometry

Tested with Python 3.12 on Windows. Use a virtual environment.

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell instead:
# .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run from this directory:

```bash
# Alanine: three independent 250 ns runs
python download.py
python prepare.py
python dynamics.py
python build_skins.py
python build_deformation.py
python validate_dynamics.py

# CLN025: deterministic subset
python download_chignolin.py
python build_chignolin.py
python validate_chignolin.py
```

The CLN025 downloader streams the first 128 non-hidden XTC members from the
Figshare archive, preserving member names and individual SHA-256 hashes. It does
not download or claim to verify the entire 1.41 GB archive. Raw inputs live in
ignored `data/`; ready-to-use derived outputs live in `dist/`.
Network access is needed only for downloads.

The subset contains 63,999 frames (one run has 499). Coordinate units are nm.
The builder verifies ten Cα sites, sequence YYDPETGTWY, neighboring distances,
and hashes before analysis. It preserves conflicting XTC timing metadata but uses
frame indices. The nominal 6.4 μs aggregate comes from the deposit's run lengths.

## Validate

```bash
python -m unittest discover -s tests -v
node test-morph.mjs
node --check dist/app.js
node --check dist/chignolin.js
```

The unittest suite needs NumPy but no raw trajectories or network access.
`validate_chignolin.py` additionally needs downloaded inputs and the full
requirements. It independently recounts core changes and compares exported
conformations against source-frame intersite distances.

## Rebuild the paper and figures

Install Blender **4.0** and [Tectonic](https://tectonic-typesetting.github.io/)
separately. Add them to `PATH`, or use full executable paths.
These are optional for running the viewer.

```bash
blender --background --python paper/render_blender.py
blender --background --python paper/render_blender.py -- --chignolin
blender --background --python paper/render_cartoons.py
blender --background --python paper/render_animation.py
blender --background --python paper/render_animation.py -- --chignolin
python -c "from pathlib import Path; Path('output/pdf').mkdir(parents=True, exist_ok=True)"
tectonic paper/paper.tex --outdir output/pdf
python publish_paper.py
```

`publish_paper.py` copies the compiled PDF to `dist/paper.pdf` and repository-root
`paper/molecular-atlas.pdf`. Blender scenes retain actual morph targets. PNGs and
MP4 loops use the browser's geometry. `paper/linkedin-post.txt` is an unposted draft.

## Implementation map

- `prepare.py`, `dynamics.py`: alanine occupancy, overlaps, states and passages.
- `build_skins.py`, `build_deformation.py`: alanine envelopes and morph targets.
- `download_chignolin.py`, `build_chignolin.py`: CLN025 provenance and construction.
- `dist/app.js`, `dist/dynamics.js`: alanine interactions.
- `dist/chignolin.js`: CLN025 interactions and path-nerve overlays.
- `dist/path-skins.js`: shared GPU morph-target renderer.
- `dist/cartoon.js`: shared smooth backbone-trace cartoons.
- `dist/chignolin/provenance.json`: source selection, attribution and hashes.

The systems deliberately use different charts. CLN025's geometric clusters are
not validated folding macrostates. See the paper for parameters and limitations.

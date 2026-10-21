# Measured revision: scope, evidence and reproduction

Author: **Joseph Campagna, PSM**. Revision: October 21, 2026.

This revision addresses the original limitation categories in paper order.
It does **not** declare all scientific limitations solved. In particular, no
physical CLN025 clock, equilibrium free energy, validated folding kinetics,
configuration-space nerve theorem or smooth molecular deformation law is claimed.

Serve `dist` over HTTP and open **http://localhost:8765/measured.html**:

```bash
python -m http.server 8765 --directory dist
```

The compact measured assets are included; raw MD downloads are unnecessary to
use the viewer or run the invariant tests. `index.html` and `chignolin.html`
are explicitly labeled legacy illustrative viewers. This revision is local;
existing public pages and the previously published PDF are historical until a
coordinated release. No Instagram assets are included in publication work.

## Evidence in original paper order

| Original limitation | Work and interpretation | Evidence in `dist/validation/` |
|---|---|---|
| Dataset scale/selection | Complete CLN025 archive and 3,744 runs verified; 1,868,861 frames analyzed. Finite deposit coverage is not configuration-space coverage. | `01-provenance.json` |
| Timing conflict | Full inventory finds no production output-stride configuration. Raw XTC times preserved; physical time is null in CLN025 playback. | `01-provenance.json` |
| Adaptive sampling/comparability | Root-balanced descriptive height; whole inferred initial-conformation cohorts resampled. Pooled comparison, dominance and sensitivity retained. No equilibrium correction. | `initial-cohorts.json`, `*-pooled-height.json`, `*-atlas.json`, `06-topology-height-sensitivity.json` |
| Chemical identity/cartoons | PSF/PDB mapping, caps/ions, all-frame bonds and backbone PBC, phi/psi/omega, 2RVD NMR distance reference. No native-state classification. | `04-chemistry.json`, `04-alanine-chemistry.json` |
| Projection/state definitions | Nested train-only feature scaling and ridge selection; several targets and history; root/cohort holdouts. No selected best interface. | `05-predictive-validation*.json` |
| Categorical claims | Full-data witnesses, periodic alanine metric, maximal simplices, GF(2) H0/H1/H2 and scale sensitivity. Drawing is only a specified finite subcategory. | `*-atlas.json` |
| Statistics/dynamics | Train-only k-means partitions, 4/8/16 states, within-run lag counts, rowwise CK, conditional group resampling, synthetic coverage, explicit kernel composition contract. | `07-*.json`, `composition-contract.json` |
| Deformation/geometry | 48 phase samples for each of 22 legacy skins; overlap candidates found. Measured viewer instead uses exact recorded sites under proper rigid alignment. | `08-geometry.json`, `*-recorded.json` |
| Rendering/software | Version pins, numerical/semantic tests, desktop/mobile Chrome and Edge checks and screenshot review. Both browsers use Chromium; no universal GPU claim. | `09-browser-checks.json`, `environment.json` |
| Publication/reproducibility | Source/data/figures versionable together; raw archive separate. Open limitations source compiles independently and remains an input to the manuscript. Public release is separate. | `artifact-manifest.json`, `limitation-register.json` |

## What the vertical dimension means

For each frame and a declared within-run lag, take the RMS change of the 45
pair distances among the ten displayed sites. This is invariant to rigid
translation/rotation and has units of nm. It is not a rate or energy.

Alanine: ten heavy atoms, 100 ps lag, pair-weighted conditional mean.
CLN025: ten C-alpha sites, ten-frame lag, equal mean of root-conditional means.
Only roots with >=20 retained lag pairs per bin contribute to that latter
estimand. It is **not equilibrium reweighting**. Root membership is inferred
from restart-like filenames; all descendants of a filename-inferred initial
cohort remain together for the stronger validation and resampling.

Report a bin only with >=100 pairs, >=5 blocks, >=3 runs, >=3 resampling units
and >=3 effective unit contributions. Effective contributions are a weight
concentration diagnostic, not a complete autocorrelation-corrected sample size.
The revision has 100 supported alanine bins and 78 supported CLN025 bins.
The pooled CLN025 comparison has no bins passing the stronger contribution
criterion. Missing support stays missing, and the underlying categorical
records are not removed merely because an embedding height is unavailable.

Intervals are conditional percentile resampling spread. The known-process
coverage example obtained 90% coverage for a nominal 95% cohort-bootstrap
interval, and 40.5% under deliberately false descendant independence. It does
not calibrate the MD intervals. Interfaces are not selected on plot appearance.

## Reproduce in paper order

Tested on Python 3.12.3. Use an isolated environment:

```bash
python -m venv .venv
# Activate it using the command appropriate to your shell.
python -m pip install -r requirements-validation.lock.txt
```

The lock pins direct scientific dependencies; the generated environment
inventory records installed transitive versions. GPU/OS variation can still
change rendered pixels. The MDshare downloader and complete CLN025 acquisition
require internet access and approximately gigabytes of storage.

```bash
# Acquisition and the retained baseline audit:
python download.py
python verify_full_chignolin.py
python robustness.py --full
# 1–3: integrity, clock inventory, claim gates:
python close_limitations.py provenance
# 4: PSF mapping, every-frame geometry, omega and NMR reference:
python close_limitations.py chemistry
python validate_alanine_geometry.py
# 5: train-only nested prediction (retain both groupings):
python validate_models.py --prediction-only
python validate_models.py --prediction-only --initial-cohorts
# 6: full witnessed cover and supported height, including sensitivity:
python build_validated_atlas.py
# 7: partitions fitted only on training groups, statistical diagnostics:
python validate_models.py --kinetics-only
python validate_models.py --kinetics-only --initial-cohorts
python calibrate_resampling.py
python composition_contract.py
# 8: use Blender 4.0 executable in place of 'blender' if not on PATH:
blender -b --python validate_geometry_blender.py
python export_recorded.py
# 9–10: figures, checks and provenance:
python render_revision_figures.py
blender -b --python paper/render_measured_blender.py
python -m unittest discover -s tests -v
npm ci
# With the HTTP server above running, installed Chrome and Edge on Windows:
node test-measured.mjs
python finalize_validation.py
```

`close_limitations.py chemistry` rejects downstream use if its backbone PBC
check changes coordinates; that would require regenerating the older feature
cache. The present full-data scan found zero changed frames. The PSF stores
nominal masses; the actual hydrogen-repartitioned integrator masses and saved
output stride remain unresolved provenance. The source reference is the
[2RVD NMR ensemble](https://www.rcsb.org/structure/2RVD); its distance similarity
is neither a folding label nor an experimental validation of kinetics.

## Figure and manuscript status

`paper/limitations.tex` is updated **in place** and compiles in the desktop
editor. `paper.tex` defines `AtlasMain`, allowing the same section to be included
in the manuscript without a duplicate preamble. The full manuscript source
now references the new measured Blender views, annotated nerve views, grouped
diagnostics and revised Figure 9. The already-published PDF has not been
overwritten during this open-document editing pass.

Legacy skin meshes and animations are preserved for comparison, with no claim
that a Boolean union or optical realism repairs their molecular validity.
BLEND scenes for the measured figures are generated under ignored
`output/measured-scenes/`; figure PNGs and their generator are versionable.

## Remaining gates

1. Authoritative saved-frame timing and restart/preparation provenance.
2. Independent experimental/simulation validation, rare-event coverage and
   calibrated uncertainty, including model-selection uncertainty.
3. Validated equilibrium estimation before free-energy interpretations.
4. Stable covers/projections and hypotheses for a configuration-space theorem.
5. Chemically constrained, collision-checked correspondence before smooth
   molecular deformation dynamics.
6. Explicit coupling interfaces and predictive comparison of composed and
   jointly modeled dynamics. Finite stochastic matrix laws alone are insufficient.

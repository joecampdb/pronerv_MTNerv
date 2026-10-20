# Alanine as landscape

Interactive WebGL prototype of a molecular-geometry landscape and a categorical nerve overlay.
Serve `dist/` with any static HTTP server. No build or network dependency is required at runtime.

## Reproduce

From this directory, create an isolated Python environment, install `requirements.txt`,
run `python download.py`, then `python prepare.py`.
For a local preview: `python -m http.server 8765 --directory dist`.
Run `node --check dist/app.js` for JavaScript syntax validation.

The public data source is https://markovmodel.github.io/mdshare/ALA2/:
three 250 ns alanine-dipeptide runs, 300 K, sampled at 1 ps. Inputs contain 750,000
paired phi/psi observations and 10 aligned heavy-atom positions per frame.
The raw files are excluded from source control; SHA-256 hashes are included in
`dist/data.json`. The first 100 coordinate frames were independently checked against
both supplied torsions; maximum angular discrepancy was 2.4e-7 radians.

## Construction

Occupancy is estimated on a 30×30 equal-area angular grid, smoothed periodically with
a Gaussian of sigma 0.85 bins, and expressed as -log(p/pmax). Pooling is unweighted.
This is an empirical occupancy estimate, not a validated equilibrium free-energy model.

324 bins with at least 25 samples contribute one real conformation each, selected
nearest their bin center. Centered heavy-atom positions are scaled by 3.5 and translated
to (phi/12, 1.3 F/kBT, psi/12). Summed atomic Gaussians of width 0.36 form an isosurface
at density 0.7. Surface color samples the angular free-energy field. The resulting
surface is an artistic density embedding, not a physical solvent-accessible surface.
Surface height combines free-energy placement with molecular relief.

Eighteen farthest-point cover centers define radius-73-degree balls in the cut chart.
Membership intersections are witnessed using every tenth frame (75,000 observations).
The overlap complex is truncated to its 2-skeleton. The category is the face poset
of that complex. The displayed nerve has 91 objects, 282 strict inclusions and 204
length-two strict chains. Identities and degeneracies are implicit. No nondegenerate
simplex above dimension two is possible in this truncated face poset.

Node positions use mean witness angles and do not constitute an embedding theorem.
The representative molecule is the frame nearest those angles. Morphism direction
is inclusion of index sets; it is not the reverse inclusion of intersection regions.
The overlay is not a transition-path category. The angular seam remains unglued;
no good-cover/homotopy-recovery claim is made.

Playback samples the first trajectory every 50 ps without interpolation.

## Viewer

Orbit/top cameras; selectable nerve nodes; skin, nerve and membrane visibility;
opacity and vertical scale; actual conformation inspection; trajectory playback;
Ramachandran occupancy map; PNG export; responsive layout.

Three.js 0.170.0 and OrbitControls are vendored under the MIT license (see
`dist/THREE-LICENSE.txt`). The source and scientific provenance are intentionally
separate from the experimental visual interpretation.

## Dynamics extension

Run `python dynamics.py` after `prepare.py`, then `python validate_dynamics.py`.
The dynamics file is separate so the existing geometry remains reproducible.

Four periodic density modes, found on a 60×60 grid smoothed with sigma 1.4 bins,
define disjoint angular cores of radius 25°. They lie at A=(-75°,153°),
B=(-141°,159°), C=(-75°,-15°), and D=(51°,33°). A/B interconvert rapidly:
these density basins are not claimed to be validated metastable macrostates.
Each frame retains the last core visited. A different core entry is one passage.
Before-first-core frames are excluded. Independent trajectories never share count pairs.

There are 73,145 observed passages and 10 directed route types, including rare routes
with only one or two observations. Per-run counts are provided. Lagged transition
probabilities at 10/50/100 ps use sliding endpoint pairs including self transitions;
they may include multiple intermediate passages and are not direct-route probabilities.
No detailed balance, Markov validation, uncertainty interval or net-flux claim is made.

Each displayed route uses an actual passage closest to its direction's median duration.
Time resampling uses unwrapped angles. Chart-crossing segments are not drawn.
Short connectors between mode centers and core endpoints are schematic.
Particle density scales logarithmically with passage count; animation speed is illustrative.

The dynamic category is the free path category on the observed route graph. Formal
composites are not identified with independently observed direct arrows. Its 25 pairs
of composable generators are selectable 2-simplices; the full nerve also contains
arbitrary paths and higher simplices. Return paths are not identity morphisms.
Composition only asserts matching endpoints, not consecutive observation in MD.
This nerve and the overlap face-poset nerve are distinct selectable constructions.

## Moving molecular conformations

Every representative passage now includes all its original 1 ps heavy-atom frames,
centered on the heavy-atom centroid, and the matching backbone angles. The moving
model is synchronized by trajectory time, not by path arc length. It does not travel
along the schematic mode-center connectors. Each normalized playback loop restarts
the recorded excerpt; it does not simulate a reverse transition.

Space-filling C/N/O spheres (radii 0.170/0.155/0.152 nm) and ball-and-stick views
are available. Hydrogens are omitted, and visual magnification is adjustable.
Smooth mode uses linear interpolation of the already aligned Cartesian coordinates
and shortest periodic interpolation of the corresponding angles. Intermediate
structures need not preserve bond lengths or satisfy molecular mechanics.
Recorded-frame mode displays the actual sampled coordinates without interpolation.
Displayed height comes from the same angular free-energy grid as the landscape.

The initial view selects A→C. Route filtering, composition filtering, pause/resume,
manual scrubbing, independent particle/model visibility and multiple-route views
are supported. Distinct excerpts in a categorical composition are not spliced into
a fictitious continuous trajectory.

Validation: `python validate_dynamics.py` compares every exported molecular frame
against the original coordinates and checks its matching angles. `node test-morph.mjs`
checks frame recovery, endpoint recovery, discrete sampling and seam interpolation.

## Continuous pathway skins

Run `python build_skins.py` after `dynamics.py`. Each passage contributes a swept
Gaussian atomic-density envelope at exactly the terrain's molecular magnification
(3.5) and free-energy height (no floating-marker offset). Temporal interpolation
provides at least 96 conformations per sweep. We take the maximum of per-conformation
densities, smooth by 0.45 voxels, and extract the 0.7 isosurface on a 0.22-unit grid.
This avoids making envelopes thicker merely by adding temporal samples.

The skins intersect and visually blend with the terrain; they are separate
translucent meshes, not a remeshed Boolean union with the original landscape.
Opacity is adjustable. The default view shows all route skins over a 60%-opaque
terrain, with standalone molecules, particles and guide lines hidden.

A shader highlight follows the approximate nearest-atom trajectory phase at each
surface vertex. At spatial self-overlaps this phase assignment can be ambiguous.
The highlight is a playback cue, not density, flux or a newly simulated deformation.
The swept geometry is fixed through playback; its illumination and transparency vary.
Route and categorical-composition selections filter skins, and the existing
pause, speed and progress controls apply to their highlights.

Cut-chart seam crossings remain separated; no straight surface is intentionally
drawn across the chart. Generated meshes are checked for finite values, bounded
phase attributes and local triangle edges. The separate skins do not change
the estimated kinetics, overlap nerve or path category.

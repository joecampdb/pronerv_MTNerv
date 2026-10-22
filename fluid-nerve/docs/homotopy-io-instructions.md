# Turning a nerve complex into a 3D categorical complex with homotopy.io

homotopy.io (https://homotopy.io, live master build https://beta.homotopy.io) is a proof assistant for
finitely presented semistrict n-categories. A workspace has two parts: the **signature** (generating
0-, 1-, 2-, 3-cells …) and the **workspace diagram**, a composite built from the generators. Diagrams of
dimension 3 are rendered as 3D geometry; 4-dimensional diagrams are shown as movies of 3D geometries
(homotopy-rs README; Corbyn, Heidemann, Hu, Sarti, Tataru & Vicary, "homotopy.io: a proof assistant for
finitely-presented globular n-categories", FSCD 2024, arXiv:2402.13179; TUTORIAL.md in the repository).

This document explains (1) the two encodings we use for a nerve, (2) how to import the generated
`.hom` files, (3) how to build the same thing by hand, and (4) how to read the 3D rendering.

## 1. Encodings (Street orientals)

A witnessed cover nerve is a finite simplicial complex with a total order on its vertices. Street's
*orientals* turn an ordered n-simplex into a free n-category; we use them only up to dimension 3.

| homotopy.io cell | base encoding (`base.hom`) | face-poset encoding (`poset.hom`) |
|---|---|---|
| 0-cell | cover ball U_i | a face σ of the complex (dim ≤ 3) |
| 1-cell i→j (i<j) | the overlap U_i ∩ U_j is witnessed | strict inclusion σ ⊂ τ |
| 2-cell (ij ; jk) ⇒ ik | triple overlap [i,j,k] | composable pair σ ⊂ τ ⊂ ρ |
| 3-cell | quadruple overlap [i,j,k,l] | length-3 chain σ ⊂ τ ⊂ ρ ⊂ π |

A 3-cell for [i,j,k,l] goes from the pasting "[i,j,k] then [i,k,l]" (odd faces d₃, d₁) to the pasting
"[j,k,l] then [i,j,l]" (even faces d₀, d₂). Both pastings run from the path i→j→k→l to the arrow i→l,
so the globularity check of the tool passes. The orientation convention is a choice; the inverse
convention gives an equivalent presentation. No cell is marked invertible: witnessing an overlap is a
directed, factual statement, and we make no claim that any overlap "composes" dynamically.

The face-poset encoding is the categorical object the atlas draws (the nerve of the face poset); the
base encoding is smaller (≤ 18 objects) and is the one to use first when learning the tool.

## 2. Import the generated files

Files live in `fluid-nerve/dist/homotopy/<system-id>/`: `base.hom`, `poset.hom`, their `*.ops.json`
sources, and a `README.md` with sizes and a click script. They were produced by
`vendor/homotopy-rs/target/release/nerve_hom` (our small binary built on the homotopy-rs crates, commit
c51f0cd), which replays the ops through the tool's own proof model and runs its deep diagram check
before serialising with the tool's `serialize` module (MessagePack, `Data_v0_1_3`).

1. Open https://beta.homotopy.io (the `.hom` format belongs to the Rust/WASM version, not the legacy site).
2. Click the top-most button on the left (project view). Use **Import** and choose a `.hom` file.
3. Press the **Signature** button (second on the left). Cells are listed with their dimension; names
   are `U3`, `U3→U7`, `[3,7,12]`, `[3,7,12,15]` (base) or `{3}`, `{3}→{3,7}`, … (poset).
4. Click a 3-cell. The workspace shows it as a 2D projection; use the view controls (top-right) to set
   the view dimension to 3 and orbit the 3D rendering. Slices (the arrows at the right) step through the
   movie of 2D diagrams whose frames are the source and target pastings.
5. `Image Export` (third button, top-left) exports 2D diagrams and slices as SVG or TikZ.

The poset encoding of a large nerve can reach several thousand generators; the browser needs a few
seconds per thousand and the signature panel becomes long. `export_homotopy.py --max-generators`
controls the cut-off (default 4000); systems above it get only the base encoding.

## 3. Build it by hand (what the generator automates)

Keyboard: `A` add 0-cell, `S` set source, `T` set target, `I` identity, `C` clear, `U`/`Y` undo/redo,
`H` theorem, numbers 1–9 select signature cells.

1. **0-cells.** Press `A` once per vertex; click left of a name to rename (LaTeX allowed).
2. **1-cells.** For each edge i<j: select U_i, press `S`; select U_j, press `T`. A directed 1-cell
   U_i→U_j is created. (Both boundaries are 0-cells, so no globularity issue arises.)
3. **2-cells.** For each triangle [i,j,k]: select the 1-cell U_i→U_j so it is the workspace diagram.
   Click just above its upper end point; the tool offers the 1-cells whose source is U_j — choose
   U_j→U_k. The workspace now shows the composite i→j→k. Press `S`. Select the 1-cell U_i→U_k and press
   `T`. The 2-cell (ij ; jk) ⇒ ik is created.
4. **3-cells.** For each tetrahedron [i,j,k,l]:
   - select the 2-cell [i,j,k]; click the right edge of the diagram and choose U_k→U_l (this whiskers
     the diagram: the source path becomes i→j→k→l); click the top edge above the two remaining strands
     and choose [i,k,l]; press `S`;
   - select the 2-cell [j,k,l]; click the left edge and choose U_i→U_j; click the top edge and choose
     [i,j,l]; press `T`.
   The two pastings share the source path i→j→k→l and the target arrow i→l, so the tool accepts them as
   the boundaries of a new 3-cell.
5. Save with **Export** in the project view.

In the replay format used by `nerve_hom` these steps are literally `zero`, `select`/`source`/`target`,
`attach` with `boundary ["Target",0]` (append above), `["Target",1]` / `["Source",1]` (whisker right /
left) and `embedding [0]` (the attached cell's source occupies the first regular position of the top
boundary). The tool infers the whiskering depth from the dimension difference between the workspace
diagram and the attached cell (`DiagramN::attach` in homotopy-core).

## 4. Reading the 3D rendering

In the 3D view of a 3-cell, surfaces are 1-cells swept through time, wires are 2-cells (the triangles)
and the single vertex is the 3-cell itself — the point where the two ways of filling the quadruple
overlap are identified. Reading the slices bottom to top shows "[i,j,k] then [i,k,l]" deforming into
"[j,k,l] then [i,j,l]". For the face-poset encoding the same picture shows two factorisations of a
length-three chain of inclusions being identified.

What the pictures do **not** say: an overlap of cover balls is a statement about a projected chart and a
finite witness set. The 3D complex is a faithful presentation of that combinatorics; it is not a model
of molecular kinetics, and nothing in it asserts a configuration-space nerve theorem.

## 5. Reproduce the files

```bash
cd fluid-nerve
# build the writer once (Rust stable, cargo); the clone lives in vendor/ and is ignored by git
git clone --depth 1 https://github.com/homotopy-io/homotopy-rs.git vendor/homotopy-rs
cp tools/nerve_hom.rs vendor/homotopy-rs/homotopy-cli/src/bin/nerve_hom.rs
(cd vendor/homotopy-rs && CARGO_PROFILE_RELEASE_LTO=false cargo build --release -p homotopy-cli --bin nerve_hom)
python export_homotopy.py            # all built systems
python export_homotopy.py ala2       # one system
```

# homotopy.io export: naphthalene (MD17 ab initio MD) (`sgdml-md17-naphthalene`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 20 1-cells, 3 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U11
- U0 → U12
- U0 → U17
- U1 → U13
- U2 → U14
- U3 → U15
- U3 → U16
- U5 → U12
- U6 → U11
- U6 → U12
- U7 → U14
- U7 → U15
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [3,15,16]: (U3→U15 ; U15→U16) ⇒ U3→U16
- [7,14,16]: (U7→U14 ; U14→U16) ⇒ U7→U16
- [7,15,16]: (U7→U15 ; U15→U16) ⇒ U7→U16

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 41 0-cells, 58 1-cells, 18 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,11}
- {0} → {0,12}
- {0} → {0,17}
- {1} → {1,13}
- {2} → {2,14}
- {3} → {3,15}
- {3} → {3,16}
- {3} → {3,15,16}
- {5} → {5,12}
- {6} → {6,11}
- {6} → {6,12}
- {7} → {7,14}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [3,23,38]: ({3}→{3,15} ; {3,15}→{3,15,16}) ⇒ {3}→{3,15,16}
- [3,24,38]: ({3}→{3,16} ; {3,16}→{3,15,16}) ⇒ {3}→{3,15,16}
- [7,28,39]: ({7}→{7,14} ; {7,14}→{7,14,16}) ⇒ {7}→{7,14,16}
- [7,29,40]: ({7}→{7,15} ; {7,15}→{7,15,16}) ⇒ {7}→{7,15,16}
- [7,30,39]: ({7}→{7,16} ; {7,16}→{7,14,16}) ⇒ {7}→{7,14,16}
- [7,30,40]: ({7}→{7,16} ; {7,16}→{7,15,16}) ⇒ {7}→{7,15,16}
- [14,28,39]: ({14}→{7,14} ; {7,14}→{7,14,16}) ⇒ {14}→{7,14,16}
- [14,36,39]: ({14}→{14,16} ; {14,16}→{7,14,16}) ⇒ {14}→{7,14,16}
- [15,23,38]: ({15}→{3,15} ; {3,15}→{3,15,16}) ⇒ {15}→{3,15,16}
- [15,29,40]: ({15}→{7,15} ; {7,15}→{7,15,16}) ⇒ {15}→{7,15,16}
- [15,37,38]: ({15}→{15,16} ; {15,16}→{3,15,16}) ⇒ {15}→{3,15,16}
- [15,37,40]: ({15}→{15,16} ; {15,16}→{7,15,16}) ⇒ {15}→{7,15,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

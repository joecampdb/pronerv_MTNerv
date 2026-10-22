# homotopy.io export: Ace-ARG-NMe dipeptide (OpenMM) (`dipeptide-arg`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 51 1-cells, 64 2-cells, 38 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U4
- U0 → U7
- U0 → U9
- U0 → U11
- U0 → U12
- U0 → U13
- U1 → U6
- U1 → U16
- U2 → U4
- U2 → U5
- U2 → U8
- U2 → U10
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,4,9]: (U0→U4 ; U4→U9) ⇒ U0→U9
- [0,4,11]: (U0→U4 ; U4→U11) ⇒ U0→U11
- [0,4,12]: (U0→U4 ; U4→U12) ⇒ U0→U12
- [0,7,9]: (U0→U7 ; U7→U9) ⇒ U0→U9
- [0,7,11]: (U0→U7 ; U7→U11) ⇒ U0→U11
- [0,7,13]: (U0→U7 ; U7→U13) ⇒ U0→U13
- [0,9,11]: (U0→U9 ; U9→U11) ⇒ U0→U11
- [0,9,12]: (U0→U9 ; U9→U12) ⇒ U0→U12
- [0,9,13]: (U0→U9 ; U9→U13) ⇒ U0→U13
- [0,11,12]: (U0→U11 ; U11→U12) ⇒ U0→U12
- [0,11,13]: (U0→U11 ; U11→U13) ⇒ U0→U13
- [0,12,13]: (U0→U12 ; U12→U13) ⇒ U0→U13
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,4,9,11]
- [0,4,9,12]
- [0,4,11,12]
- [0,7,9,11]
- [0,7,9,13]
- [0,7,11,13]
- [0,9,11,12]
- [0,9,11,13]
- [0,9,12,13]
- [0,11,12,13]
- [2,4,8,10]
- [2,4,8,17]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 171 0-cells, 1018 1-cells, 1752 2-cells, 912 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,4}
- {0} → {0,7}
- {0} → {0,9}
- {0} → {0,11}
- {0} → {0,12}
- {0} → {0,13}
- {0} → {0,4,9}
- {0} → {0,4,11}
- {0} → {0,4,12}
- {0} → {0,7,9}
- {0} → {0,7,11}
- {0} → {0,7,13}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,69]: ({0}→{0,4} ; {0,4}→{0,4,9}) ⇒ {0}→{0,4,9}
- [0,18,70]: ({0}→{0,4} ; {0,4}→{0,4,11}) ⇒ {0}→{0,4,11}
- [0,18,71]: ({0}→{0,4} ; {0,4}→{0,4,12}) ⇒ {0}→{0,4,12}
- [0,18,133]: ({0}→{0,4} ; {0,4}→{0,4,9,11}) ⇒ {0}→{0,4,9,11}
- [0,18,134]: ({0}→{0,4} ; {0,4}→{0,4,9,12}) ⇒ {0}→{0,4,9,12}
- [0,18,135]: ({0}→{0,4} ; {0,4}→{0,4,11,12}) ⇒ {0}→{0,4,11,12}
- [0,19,72]: ({0}→{0,7} ; {0,7}→{0,7,9}) ⇒ {0}→{0,7,9}
- [0,19,73]: ({0}→{0,7} ; {0,7}→{0,7,11}) ⇒ {0}→{0,7,11}
- [0,19,74]: ({0}→{0,7} ; {0,7}→{0,7,13}) ⇒ {0}→{0,7,13}
- [0,19,136]: ({0}→{0,7} ; {0,7}→{0,7,9,11}) ⇒ {0}→{0,7,9,11}
- [0,19,137]: ({0}→{0,7} ; {0,7}→{0,7,9,13}) ⇒ {0}→{0,7,9,13}
- [0,19,138]: ({0}→{0,7} ; {0,7}→{0,7,11,13}) ⇒ {0}→{0,7,11,13}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,69,133]
- [0,18,69,134]
- [0,18,70,133]
- [0,18,70,135]
- [0,18,71,134]
- [0,18,71,135]
- [0,19,72,136]
- [0,19,72,137]
- [0,19,73,136]
- [0,19,73,138]
- [0,19,74,137]
- [0,19,74,138]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

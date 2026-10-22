# homotopy.io export: AT-AT-CG-CG (MD22 ab initio MD) (`sgdml-md22-at-at-cg-cg`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 53 1-cells, 64 2-cells, 37 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U4
- U0 → U5
- U0 → U8
- U0 → U10
- U0 → U11
- U0 → U16
- U1 → U6
- U1 → U12
- U1 → U13
- U1 → U14
- U2 → U4
- U2 → U7
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,4,8]: (U0→U4 ; U4→U8) ⇒ U0→U8
- [0,5,8]: (U0→U5 ; U5→U8) ⇒ U0→U8
- [0,5,10]: (U0→U5 ; U5→U10) ⇒ U0→U10
- [0,5,11]: (U0→U5 ; U5→U11) ⇒ U0→U11
- [0,5,16]: (U0→U5 ; U5→U16) ⇒ U0→U16
- [0,8,10]: (U0→U8 ; U8→U10) ⇒ U0→U10
- [0,8,16]: (U0→U8 ; U8→U16) ⇒ U0→U16
- [0,10,11]: (U0→U10 ; U10→U11) ⇒ U0→U11
- [0,10,16]: (U0→U10 ; U10→U16) ⇒ U0→U16
- [0,11,16]: (U0→U11 ; U11→U16) ⇒ U0→U16
- [1,6,12]: (U1→U6 ; U6→U12) ⇒ U1→U12
- [1,6,13]: (U1→U6 ; U6→U13) ⇒ U1→U13
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,5,8,10]
- [0,5,8,16]
- [0,5,10,11]
- [0,5,10,16]
- [0,5,11,16]
- [0,8,10,16]
- [0,10,11,16]
- [1,6,12,13]
- [1,6,12,14]
- [1,6,13,14]
- [1,12,13,14]
- [2,4,7,9]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 172 0-cells, 1008 1-cells, 1716 2-cells, 888 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,4}
- {0} → {0,5}
- {0} → {0,8}
- {0} → {0,10}
- {0} → {0,11}
- {0} → {0,16}
- {0} → {0,4,8}
- {0} → {0,5,8}
- {0} → {0,5,10}
- {0} → {0,5,11}
- {0} → {0,5,16}
- {0} → {0,8,10}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,71]: ({0}→{0,4} ; {0,4}→{0,4,8}) ⇒ {0}→{0,4,8}
- [0,19,72]: ({0}→{0,5} ; {0,5}→{0,5,8}) ⇒ {0}→{0,5,8}
- [0,19,73]: ({0}→{0,5} ; {0,5}→{0,5,10}) ⇒ {0}→{0,5,10}
- [0,19,74]: ({0}→{0,5} ; {0,5}→{0,5,11}) ⇒ {0}→{0,5,11}
- [0,19,75]: ({0}→{0,5} ; {0,5}→{0,5,16}) ⇒ {0}→{0,5,16}
- [0,19,135]: ({0}→{0,5} ; {0,5}→{0,5,8,10}) ⇒ {0}→{0,5,8,10}
- [0,19,136]: ({0}→{0,5} ; {0,5}→{0,5,8,16}) ⇒ {0}→{0,5,8,16}
- [0,19,137]: ({0}→{0,5} ; {0,5}→{0,5,10,11}) ⇒ {0}→{0,5,10,11}
- [0,19,138]: ({0}→{0,5} ; {0,5}→{0,5,10,16}) ⇒ {0}→{0,5,10,16}
- [0,19,139]: ({0}→{0,5} ; {0,5}→{0,5,11,16}) ⇒ {0}→{0,5,11,16}
- [0,20,71]: ({0}→{0,8} ; {0,8}→{0,4,8}) ⇒ {0}→{0,4,8}
- [0,20,72]: ({0}→{0,8} ; {0,8}→{0,5,8}) ⇒ {0}→{0,5,8}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,19,72,135]
- [0,19,72,136]
- [0,19,73,135]
- [0,19,73,137]
- [0,19,73,138]
- [0,19,74,137]
- [0,19,74,139]
- [0,19,75,136]
- [0,19,75,138]
- [0,19,75,139]
- [0,20,72,135]
- [0,20,72,136]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

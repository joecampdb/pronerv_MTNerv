# homotopy.io export: malonaldehyde (MD17 ab initio MD) (`sgdml-md17-malonaldehyde`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 39 1-cells, 22 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U8
- U0 → U9
- U0 → U10
- U0 → U11
- U0 → U12
- U1 → U7
- U1 → U8
- U1 → U13
- U1 → U15
- U2 → U7
- U2 → U12
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,8]: (U0→U7 ; U7→U8) ⇒ U0→U8
- [0,7,12]: (U0→U7 ; U7→U12) ⇒ U0→U12
- [0,8,9]: (U0→U8 ; U8→U9) ⇒ U0→U9
- [0,9,10]: (U0→U9 ; U9→U10) ⇒ U0→U10
- [0,10,11]: (U0→U10 ; U10→U11) ⇒ U0→U11
- [0,11,12]: (U0→U11 ; U11→U12) ⇒ U0→U12
- [1,7,8]: (U1→U7 ; U7→U8) ⇒ U1→U8
- [1,7,13]: (U1→U7 ; U7→U13) ⇒ U1→U13
- [1,8,15]: (U1→U8 ; U8→U15) ⇒ U1→U15
- [2,7,12]: (U2→U7 ; U7→U12) ⇒ U2→U12
- [2,7,13]: (U2→U7 ; U7→U13) ⇒ U2→U13
- [2,12,14]: (U2→U12 ; U12→U14) ⇒ U2→U14
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 79 0-cells, 210 1-cells, 132 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,10}
- {0} → {0,11}
- {0} → {0,12}
- {0} → {0,7,8}
- {0} → {0,7,12}
- {0} → {0,8,9}
- {0} → {0,9,10}
- {0} → {0,10,11}
- {0} → {0,11,12}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,57]: ({0}→{0,7} ; {0,7}→{0,7,8}) ⇒ {0}→{0,7,8}
- [0,18,58]: ({0}→{0,7} ; {0,7}→{0,7,12}) ⇒ {0}→{0,7,12}
- [0,19,57]: ({0}→{0,8} ; {0,8}→{0,7,8}) ⇒ {0}→{0,7,8}
- [0,19,59]: ({0}→{0,8} ; {0,8}→{0,8,9}) ⇒ {0}→{0,8,9}
- [0,20,59]: ({0}→{0,9} ; {0,9}→{0,8,9}) ⇒ {0}→{0,8,9}
- [0,20,60]: ({0}→{0,9} ; {0,9}→{0,9,10}) ⇒ {0}→{0,9,10}
- [0,21,60]: ({0}→{0,10} ; {0,10}→{0,9,10}) ⇒ {0}→{0,9,10}
- [0,21,61]: ({0}→{0,10} ; {0,10}→{0,10,11}) ⇒ {0}→{0,10,11}
- [0,22,61]: ({0}→{0,11} ; {0,11}→{0,10,11}) ⇒ {0}→{0,10,11}
- [0,22,62]: ({0}→{0,11} ; {0,11}→{0,11,12}) ⇒ {0}→{0,11,12}
- [0,23,58]: ({0}→{0,12} ; {0,12}→{0,7,12}) ⇒ {0}→{0,7,12}
- [0,23,62]: ({0}→{0,12} ; {0,12}→{0,11,12}) ⇒ {0}→{0,11,12}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

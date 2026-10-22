# homotopy.io export: CATH domain 1r8oB01 (mdCATH), C-alpha (`mdcath-1r8ob01-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 42 1-cells, 27 2-cells, 3 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U5
- U0 → U8
- U0 → U9
- U0 → U10
- U0 → U11
- U0 → U13
- U0 → U16
- U1 → U6
- U1 → U7
- U1 → U12
- U1 → U15
- U2 → U5
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,5,11]: (U0→U5 ; U5→U11) ⇒ U0→U11
- [0,5,13]: (U0→U5 ; U5→U13) ⇒ U0→U13
- [0,8,10]: (U0→U8 ; U8→U10) ⇒ U0→U10
- [0,8,11]: (U0→U8 ; U8→U11) ⇒ U0→U11
- [0,9,10]: (U0→U9 ; U9→U10) ⇒ U0→U10
- [0,9,16]: (U0→U9 ; U9→U16) ⇒ U0→U16
- [0,10,16]: (U0→U10 ; U10→U16) ⇒ U0→U16
- [0,11,13]: (U0→U11 ; U11→U13) ⇒ U0→U13
- [0,13,16]: (U0→U13 ; U13→U16) ⇒ U0→U16
- [1,6,12]: (U1→U6 ; U6→U12) ⇒ U1→U12
- [1,7,15]: (U1→U7 ; U7→U15) ⇒ U1→U15
- [1,12,15]: (U1→U12 ; U12→U15) ⇒ U1→U15
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,5,11,13]
- [0,9,10,16]
- [4,12,15,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 90 0-cells, 288 1-cells, 270 2-cells, 72 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,5}
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,10}
- {0} → {0,11}
- {0} → {0,13}
- {0} → {0,16}
- {0} → {0,5,11}
- {0} → {0,5,13}
- {0} → {0,8,10}
- {0} → {0,8,11}
- {0} → {0,9,10}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,60]: ({0}→{0,5} ; {0,5}→{0,5,11}) ⇒ {0}→{0,5,11}
- [0,18,61]: ({0}→{0,5} ; {0,5}→{0,5,13}) ⇒ {0}→{0,5,13}
- [0,18,87]: ({0}→{0,5} ; {0,5}→{0,5,11,13}) ⇒ {0}→{0,5,11,13}
- [0,19,62]: ({0}→{0,8} ; {0,8}→{0,8,10}) ⇒ {0}→{0,8,10}
- [0,19,63]: ({0}→{0,8} ; {0,8}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,20,64]: ({0}→{0,9} ; {0,9}→{0,9,10}) ⇒ {0}→{0,9,10}
- [0,20,65]: ({0}→{0,9} ; {0,9}→{0,9,16}) ⇒ {0}→{0,9,16}
- [0,20,88]: ({0}→{0,9} ; {0,9}→{0,9,10,16}) ⇒ {0}→{0,9,10,16}
- [0,21,62]: ({0}→{0,10} ; {0,10}→{0,8,10}) ⇒ {0}→{0,8,10}
- [0,21,64]: ({0}→{0,10} ; {0,10}→{0,9,10}) ⇒ {0}→{0,9,10}
- [0,21,66]: ({0}→{0,10} ; {0,10}→{0,10,16}) ⇒ {0}→{0,10,16}
- [0,21,88]: ({0}→{0,10} ; {0,10}→{0,9,10,16}) ⇒ {0}→{0,9,10,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,60,87]
- [0,18,61,87]
- [0,20,64,88]
- [0,20,65,88]
- [0,21,64,88]
- [0,21,66,88]
- [0,22,60,87]
- [0,22,67,87]
- [0,23,61,87]
- [0,23,67,87]
- [0,24,65,88]
- [0,24,66,88]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

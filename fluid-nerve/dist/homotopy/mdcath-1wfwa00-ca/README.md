# homotopy.io export: CATH domain 1wfwA00 (mdCATH), C-alpha (`mdcath-1wfwa00-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 37 1-cells, 17 2-cells, 1 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U9
- U0 → U10
- U0 → U12
- U0 → U15
- U0 → U16
- U1 → U7
- U1 → U11
- U2 → U13
- U2 → U17
- U3 → U8
- U3 → U14
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,15]: (U0→U8 ; U8→U15) ⇒ U0→U15
- [0,8,16]: (U0→U8 ; U8→U16) ⇒ U0→U16
- [0,9,12]: (U0→U9 ; U9→U12) ⇒ U0→U12
- [0,9,15]: (U0→U9 ; U9→U15) ⇒ U0→U15
- [0,10,12]: (U0→U10 ; U10→U12) ⇒ U0→U12
- [0,10,16]: (U0→U10 ; U10→U16) ⇒ U0→U16
- [0,15,16]: (U0→U15 ; U15→U16) ⇒ U0→U16
- [2,13,17]: (U2→U13 ; U13→U17) ⇒ U2→U17
- [4,9,13]: (U4→U9 ; U9→U13) ⇒ U4→U13
- [4,9,15]: (U4→U9 ; U9→U15) ⇒ U4→U15
- [4,11,14]: (U4→U11 ; U11→U14) ⇒ U4→U14
- [4,14,15]: (U4→U14 ; U14→U15) ⇒ U4→U15
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,8,15,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 73 0-cells, 190 1-cells, 138 2-cells, 24 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,10}
- {0} → {0,12}
- {0} → {0,15}
- {0} → {0,16}
- {0} → {0,8,15}
- {0} → {0,8,16}
- {0} → {0,9,12}
- {0} → {0,9,15}
- {0} → {0,10,12}
- {0} → {0,10,16}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,55]: ({0}→{0,8} ; {0,8}→{0,8,15}) ⇒ {0}→{0,8,15}
- [0,18,56]: ({0}→{0,8} ; {0,8}→{0,8,16}) ⇒ {0}→{0,8,16}
- [0,18,72]: ({0}→{0,8} ; {0,8}→{0,8,15,16}) ⇒ {0}→{0,8,15,16}
- [0,19,57]: ({0}→{0,9} ; {0,9}→{0,9,12}) ⇒ {0}→{0,9,12}
- [0,19,58]: ({0}→{0,9} ; {0,9}→{0,9,15}) ⇒ {0}→{0,9,15}
- [0,20,59]: ({0}→{0,10} ; {0,10}→{0,10,12}) ⇒ {0}→{0,10,12}
- [0,20,60]: ({0}→{0,10} ; {0,10}→{0,10,16}) ⇒ {0}→{0,10,16}
- [0,21,57]: ({0}→{0,12} ; {0,12}→{0,9,12}) ⇒ {0}→{0,9,12}
- [0,21,59]: ({0}→{0,12} ; {0,12}→{0,10,12}) ⇒ {0}→{0,10,12}
- [0,22,55]: ({0}→{0,15} ; {0,15}→{0,8,15}) ⇒ {0}→{0,8,15}
- [0,22,58]: ({0}→{0,15} ; {0,15}→{0,9,15}) ⇒ {0}→{0,9,15}
- [0,22,61]: ({0}→{0,15} ; {0,15}→{0,15,16}) ⇒ {0}→{0,15,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,55,72]
- [0,18,56,72]
- [0,22,55,72]
- [0,22,61,72]
- [0,23,56,72]
- [0,23,61,72]
- [8,18,55,72]
- [8,18,56,72]
- [8,43,55,72]
- [8,43,70,72]
- [8,44,56,72]
- [8,44,70,72]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

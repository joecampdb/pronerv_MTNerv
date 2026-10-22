# homotopy.io export: CATH domain 2jrrA01 (mdCATH), C-alpha (`mdcath-2jrra01-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 42 1-cells, 33 2-cells, 8 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U7
- U0 → U10
- U0 → U12
- U0 → U13
- U0 → U16
- U1 → U8
- U2 → U6
- U2 → U17
- U3 → U7
- U3 → U9
- U3 → U11
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,12]: (U0→U6 ; U6→U12) ⇒ U0→U12
- [0,6,13]: (U0→U6 ; U6→U13) ⇒ U0→U13
- [0,7,10]: (U0→U7 ; U7→U10) ⇒ U0→U10
- [0,7,16]: (U0→U7 ; U7→U16) ⇒ U0→U16
- [0,10,16]: (U0→U10 ; U10→U16) ⇒ U0→U16
- [0,12,13]: (U0→U12 ; U12→U13) ⇒ U0→U13
- [0,12,16]: (U0→U12 ; U12→U16) ⇒ U0→U16
- [0,13,16]: (U0→U13 ; U13→U16) ⇒ U0→U16
- [2,6,17]: (U2→U6 ; U6→U17) ⇒ U2→U17
- [3,7,15]: (U3→U7 ; U7→U15) ⇒ U3→U15
- [3,9,11]: (U3→U9 ; U9→U11) ⇒ U3→U11
- [3,9,15]: (U3→U9 ; U9→U15) ⇒ U3→U15
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,6,12,13]
- [0,7,10,16]
- [0,12,13,16]
- [3,9,11,15]
- [5,7,10,14]
- [7,9,15,16]
- [7,10,14,16]
- [8,9,11,15]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 101 0-cells, 394 1-cells, 486 2-cells, 192 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,7}
- {0} → {0,10}
- {0} → {0,12}
- {0} → {0,13}
- {0} → {0,16}
- {0} → {0,6,12}
- {0} → {0,6,13}
- {0} → {0,7,10}
- {0} → {0,7,16}
- {0} → {0,10,16}
- {0} → {0,12,13}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,60]: ({0}→{0,6} ; {0,6}→{0,6,12}) ⇒ {0}→{0,6,12}
- [0,18,61]: ({0}→{0,6} ; {0,6}→{0,6,13}) ⇒ {0}→{0,6,13}
- [0,18,93]: ({0}→{0,6} ; {0,6}→{0,6,12,13}) ⇒ {0}→{0,6,12,13}
- [0,19,62]: ({0}→{0,7} ; {0,7}→{0,7,10}) ⇒ {0}→{0,7,10}
- [0,19,63]: ({0}→{0,7} ; {0,7}→{0,7,16}) ⇒ {0}→{0,7,16}
- [0,19,94]: ({0}→{0,7} ; {0,7}→{0,7,10,16}) ⇒ {0}→{0,7,10,16}
- [0,20,62]: ({0}→{0,10} ; {0,10}→{0,7,10}) ⇒ {0}→{0,7,10}
- [0,20,64]: ({0}→{0,10} ; {0,10}→{0,10,16}) ⇒ {0}→{0,10,16}
- [0,20,94]: ({0}→{0,10} ; {0,10}→{0,7,10,16}) ⇒ {0}→{0,7,10,16}
- [0,21,60]: ({0}→{0,12} ; {0,12}→{0,6,12}) ⇒ {0}→{0,6,12}
- [0,21,65]: ({0}→{0,12} ; {0,12}→{0,12,13}) ⇒ {0}→{0,12,13}
- [0,21,66]: ({0}→{0,12} ; {0,12}→{0,12,16}) ⇒ {0}→{0,12,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,60,93]
- [0,18,61,93]
- [0,19,62,94]
- [0,19,63,94]
- [0,20,62,94]
- [0,20,64,94]
- [0,21,60,93]
- [0,21,65,93]
- [0,21,65,95]
- [0,21,66,95]
- [0,22,61,93]
- [0,22,65,93]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

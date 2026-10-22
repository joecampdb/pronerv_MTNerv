# homotopy.io export: CATH domain 2yilA02 (mdCATH), C-alpha (`mdcath-2yila02-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 42 1-cells, 36 2-cells, 13 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U7
- U0 → U10
- U0 → U11
- U0 → U12
- U0 → U14
- U0 → U15
- U0 → U16
- U1 → U8
- U2 → U9
- U2 → U13
- U2 → U17
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,10]: (U0→U6 ; U6→U10) ⇒ U0→U10
- [0,6,11]: (U0→U6 ; U6→U11) ⇒ U0→U11
- [0,6,15]: (U0→U6 ; U6→U15) ⇒ U0→U15
- [0,7,12]: (U0→U7 ; U7→U12) ⇒ U0→U12
- [0,7,14]: (U0→U7 ; U7→U14) ⇒ U0→U14
- [0,7,16]: (U0→U7 ; U7→U16) ⇒ U0→U16
- [0,10,11]: (U0→U10 ; U10→U11) ⇒ U0→U11
- [0,10,15]: (U0→U10 ; U10→U15) ⇒ U0→U15
- [0,10,16]: (U0→U10 ; U10→U16) ⇒ U0→U16
- [0,11,12]: (U0→U11 ; U11→U12) ⇒ U0→U12
- [0,11,15]: (U0→U11 ; U11→U15) ⇒ U0→U15
- [0,12,14]: (U0→U12 ; U12→U14) ⇒ U0→U14
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,6,10,11]
- [0,6,10,15]
- [0,6,11,15]
- [0,7,12,14]
- [0,7,12,16]
- [0,7,14,16]
- [0,10,11,15]
- [0,10,15,16]
- [0,12,14,16]
- [2,9,13,17]
- [4,9,13,17]
- [6,10,11,15]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 109 0-cells, 482 1-cells, 684 2-cells, 312 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,7}
- {0} → {0,10}
- {0} → {0,11}
- {0} → {0,12}
- {0} → {0,14}
- {0} → {0,15}
- {0} → {0,16}
- {0} → {0,6,10}
- {0} → {0,6,11}
- {0} → {0,6,15}
- {0} → {0,7,12}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,60]: ({0}→{0,6} ; {0,6}→{0,6,10}) ⇒ {0}→{0,6,10}
- [0,18,61]: ({0}→{0,6} ; {0,6}→{0,6,11}) ⇒ {0}→{0,6,11}
- [0,18,62]: ({0}→{0,6} ; {0,6}→{0,6,15}) ⇒ {0}→{0,6,15}
- [0,18,96]: ({0}→{0,6} ; {0,6}→{0,6,10,11}) ⇒ {0}→{0,6,10,11}
- [0,18,97]: ({0}→{0,6} ; {0,6}→{0,6,10,15}) ⇒ {0}→{0,6,10,15}
- [0,18,98]: ({0}→{0,6} ; {0,6}→{0,6,11,15}) ⇒ {0}→{0,6,11,15}
- [0,19,63]: ({0}→{0,7} ; {0,7}→{0,7,12}) ⇒ {0}→{0,7,12}
- [0,19,64]: ({0}→{0,7} ; {0,7}→{0,7,14}) ⇒ {0}→{0,7,14}
- [0,19,65]: ({0}→{0,7} ; {0,7}→{0,7,16}) ⇒ {0}→{0,7,16}
- [0,19,99]: ({0}→{0,7} ; {0,7}→{0,7,12,14}) ⇒ {0}→{0,7,12,14}
- [0,19,100]: ({0}→{0,7} ; {0,7}→{0,7,12,16}) ⇒ {0}→{0,7,12,16}
- [0,19,101]: ({0}→{0,7} ; {0,7}→{0,7,14,16}) ⇒ {0}→{0,7,14,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,60,96]
- [0,18,60,97]
- [0,18,61,96]
- [0,18,61,98]
- [0,18,62,97]
- [0,18,62,98]
- [0,19,63,99]
- [0,19,63,100]
- [0,19,64,99]
- [0,19,64,101]
- [0,19,65,100]
- [0,19,65,101]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

# homotopy.io export: CATH domain 1e5wA04 (mdCATH), C-alpha (`mdcath-1e5wa04-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 45 1-cells, 33 2-cells, 6 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U10
- U0 → U11
- U0 → U13
- U0 → U16
- U0 → U17
- U1 → U7
- U1 → U9
- U1 → U15
- U2 → U7
- U2 → U8
- U2 → U12
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,13]: (U0→U8 ; U8→U13) ⇒ U0→U13
- [0,8,16]: (U0→U8 ; U8→U16) ⇒ U0→U16
- [0,10,16]: (U0→U10 ; U10→U16) ⇒ U0→U16
- [0,10,17]: (U0→U10 ; U10→U17) ⇒ U0→U17
- [0,11,17]: (U0→U11 ; U11→U17) ⇒ U0→U17
- [0,13,16]: (U0→U13 ; U13→U16) ⇒ U0→U16
- [0,16,17]: (U0→U16 ; U16→U17) ⇒ U0→U17
- [1,7,15]: (U1→U7 ; U7→U15) ⇒ U1→U15
- [1,9,15]: (U1→U9 ; U9→U15) ⇒ U1→U15
- [2,7,14]: (U2→U7 ; U7→U14) ⇒ U2→U14
- [2,8,12]: (U2→U8 ; U8→U12) ⇒ U2→U12
- [2,8,14]: (U2→U8 ; U8→U14) ⇒ U2→U14
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,8,13,16]
- [0,10,16,17]
- [2,8,12,14]
- [4,8,12,13]
- [5,7,14,15]
- [5,8,14,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 102 0-cells, 372 1-cells, 414 2-cells, 144 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,10}
- {0} → {0,11}
- {0} → {0,13}
- {0} → {0,16}
- {0} → {0,17}
- {0} → {0,8,13}
- {0} → {0,8,16}
- {0} → {0,10,16}
- {0} → {0,10,17}
- {0} → {0,11,17}
- {0} → {0,13,16}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,63]: ({0}→{0,8} ; {0,8}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,18,64]: ({0}→{0,8} ; {0,8}→{0,8,16}) ⇒ {0}→{0,8,16}
- [0,18,96]: ({0}→{0,8} ; {0,8}→{0,8,13,16}) ⇒ {0}→{0,8,13,16}
- [0,19,65]: ({0}→{0,10} ; {0,10}→{0,10,16}) ⇒ {0}→{0,10,16}
- [0,19,66]: ({0}→{0,10} ; {0,10}→{0,10,17}) ⇒ {0}→{0,10,17}
- [0,19,97]: ({0}→{0,10} ; {0,10}→{0,10,16,17}) ⇒ {0}→{0,10,16,17}
- [0,20,67]: ({0}→{0,11} ; {0,11}→{0,11,17}) ⇒ {0}→{0,11,17}
- [0,21,63]: ({0}→{0,13} ; {0,13}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,21,68]: ({0}→{0,13} ; {0,13}→{0,13,16}) ⇒ {0}→{0,13,16}
- [0,21,96]: ({0}→{0,13} ; {0,13}→{0,8,13,16}) ⇒ {0}→{0,8,13,16}
- [0,22,64]: ({0}→{0,16} ; {0,16}→{0,8,16}) ⇒ {0}→{0,8,16}
- [0,22,65]: ({0}→{0,16} ; {0,16}→{0,10,16}) ⇒ {0}→{0,10,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,63,96]
- [0,18,64,96]
- [0,19,65,97]
- [0,19,66,97]
- [0,21,63,96]
- [0,21,68,96]
- [0,22,64,96]
- [0,22,65,97]
- [0,22,68,96]
- [0,22,69,97]
- [0,23,66,97]
- [0,23,69,97]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

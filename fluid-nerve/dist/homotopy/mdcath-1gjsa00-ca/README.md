# homotopy.io export: CATH domain 1gjsA00 (mdCATH), C-alpha (`mdcath-1gjsa00-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 41 1-cells, 27 2-cells, 4 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U8
- U0 → U11
- U0 → U16
- U1 → U6
- U1 → U10
- U2 → U9
- U2 → U15
- U2 → U17
- U3 → U6
- U3 → U7
- U3 → U12
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,16]: (U0→U7 ; U7→U16) ⇒ U0→U16
- [0,8,11]: (U0→U8 ; U8→U11) ⇒ U0→U11
- [0,8,16]: (U0→U8 ; U8→U16) ⇒ U0→U16
- [1,6,10]: (U1→U6 ; U6→U10) ⇒ U1→U10
- [2,9,15]: (U2→U9 ; U9→U15) ⇒ U2→U15
- [2,9,17]: (U2→U9 ; U9→U17) ⇒ U2→U17
- [3,7,12]: (U3→U7 ; U7→U12) ⇒ U3→U12
- [4,7,14]: (U4→U7 ; U7→U14) ⇒ U4→U14
- [4,7,16]: (U4→U7 ; U7→U16) ⇒ U4→U16
- [4,8,9]: (U4→U8 ; U8→U9) ⇒ U4→U9
- [4,8,16]: (U4→U8 ; U8→U16) ⇒ U4→U16
- [4,9,13]: (U4→U9 ; U9→U13) ⇒ U4→U13
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [4,7,14,16]
- [4,8,9,16]
- [4,9,13,17]
- [4,10,13,14]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 90 0-cells, 300 1-cells, 306 2-cells, 96 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,8}
- {0} → {0,11}
- {0} → {0,16}
- {0} → {0,7,16}
- {0} → {0,8,11}
- {0} → {0,8,16}
- {1} → {1,6}
- {1} → {1,10}
- {1} → {1,6,10}
- {2} → {2,9}
- {2} → {2,15}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,59]: ({0}→{0,7} ; {0,7}→{0,7,16}) ⇒ {0}→{0,7,16}
- [0,19,60]: ({0}→{0,8} ; {0,8}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,19,61]: ({0}→{0,8} ; {0,8}→{0,8,16}) ⇒ {0}→{0,8,16}
- [0,20,60]: ({0}→{0,11} ; {0,11}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,21,59]: ({0}→{0,16} ; {0,16}→{0,7,16}) ⇒ {0}→{0,7,16}
- [0,21,61]: ({0}→{0,16} ; {0,16}→{0,8,16}) ⇒ {0}→{0,8,16}
- [1,22,62]: ({1}→{1,6} ; {1,6}→{1,6,10}) ⇒ {1}→{1,6,10}
- [1,23,62]: ({1}→{1,10} ; {1,10}→{1,6,10}) ⇒ {1}→{1,6,10}
- [2,24,63]: ({2}→{2,9} ; {2,9}→{2,9,15}) ⇒ {2}→{2,9,15}
- [2,24,64]: ({2}→{2,9} ; {2,9}→{2,9,17}) ⇒ {2}→{2,9,17}
- [2,25,63]: ({2}→{2,15} ; {2,15}→{2,9,15}) ⇒ {2}→{2,9,15}
- [2,26,64]: ({2}→{2,17} ; {2,17}→{2,9,17}) ⇒ {2}→{2,9,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [4,30,66,86]
- [4,30,67,86]
- [4,31,68,87]
- [4,31,69,87]
- [4,32,68,87]
- [4,32,70,88]
- [4,32,71,87]
- [4,32,72,88]
- [4,33,73,89]
- [4,33,74,89]
- [4,34,70,88]
- [4,34,73,89]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

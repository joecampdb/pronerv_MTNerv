# homotopy.io export: CATH domain 5b1aJ00 (mdCATH), heavy atoms (`mdcath-5b1aj00-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 41 1-cells, 27 2-cells, 4 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U8
- U0 → U10
- U0 → U11
- U0 → U12
- U0 → U16
- U0 → U17
- U1 → U9
- U1 → U13
- U2 → U11
- U2 → U14
- U2 → U15
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,12]: (U0→U7 ; U7→U12) ⇒ U0→U12
- [0,8,10]: (U0→U8 ; U8→U10) ⇒ U0→U10
- [0,8,16]: (U0→U8 ; U8→U16) ⇒ U0→U16
- [0,10,16]: (U0→U10 ; U10→U16) ⇒ U0→U16
- [0,11,16]: (U0→U11 ; U11→U16) ⇒ U0→U16
- [0,11,17]: (U0→U11 ; U11→U17) ⇒ U0→U17
- [0,12,17]: (U0→U12 ; U12→U17) ⇒ U0→U17
- [0,16,17]: (U0→U16 ; U16→U17) ⇒ U0→U17
- [1,9,13]: (U1→U9 ; U9→U13) ⇒ U1→U13
- [2,11,14]: (U2→U11 ; U11→U14) ⇒ U2→U14
- [2,11,15]: (U2→U11 ; U11→U15) ⇒ U2→U15
- [3,8,9]: (U3→U8 ; U8→U9) ⇒ U3→U9
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,8,10,16]
- [0,11,16,17]
- [5,11,15,17]
- [6,8,13,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 90 0-cells, 300 1-cells, 306 2-cells, 96 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,8}
- {0} → {0,10}
- {0} → {0,11}
- {0} → {0,12}
- {0} → {0,16}
- {0} → {0,17}
- {0} → {0,7,12}
- {0} → {0,8,10}
- {0} → {0,8,16}
- {0} → {0,10,16}
- {0} → {0,11,16}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,59]: ({0}→{0,7} ; {0,7}→{0,7,12}) ⇒ {0}→{0,7,12}
- [0,19,60]: ({0}→{0,8} ; {0,8}→{0,8,10}) ⇒ {0}→{0,8,10}
- [0,19,61]: ({0}→{0,8} ; {0,8}→{0,8,16}) ⇒ {0}→{0,8,16}
- [0,19,86]: ({0}→{0,8} ; {0,8}→{0,8,10,16}) ⇒ {0}→{0,8,10,16}
- [0,20,60]: ({0}→{0,10} ; {0,10}→{0,8,10}) ⇒ {0}→{0,8,10}
- [0,20,62]: ({0}→{0,10} ; {0,10}→{0,10,16}) ⇒ {0}→{0,10,16}
- [0,20,86]: ({0}→{0,10} ; {0,10}→{0,8,10,16}) ⇒ {0}→{0,8,10,16}
- [0,21,63]: ({0}→{0,11} ; {0,11}→{0,11,16}) ⇒ {0}→{0,11,16}
- [0,21,64]: ({0}→{0,11} ; {0,11}→{0,11,17}) ⇒ {0}→{0,11,17}
- [0,21,87]: ({0}→{0,11} ; {0,11}→{0,11,16,17}) ⇒ {0}→{0,11,16,17}
- [0,22,59]: ({0}→{0,12} ; {0,12}→{0,7,12}) ⇒ {0}→{0,7,12}
- [0,22,65]: ({0}→{0,12} ; {0,12}→{0,12,17}) ⇒ {0}→{0,12,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,19,60,86]
- [0,19,61,86]
- [0,20,60,86]
- [0,20,62,86]
- [0,21,63,87]
- [0,21,64,87]
- [0,23,61,86]
- [0,23,62,86]
- [0,23,63,87]
- [0,23,66,87]
- [0,24,64,87]
- [0,24,66,87]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

# homotopy.io export: CATH domain 2yilA02 (mdCATH), heavy atoms (`mdcath-2yila02-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 35 1-cells, 20 2-cells, 2 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U9
- U0 → U11
- U0 → U14
- U0 → U16
- U0 → U17
- U1 → U8
- U1 → U13
- U2 → U12
- U2 → U15
- U3 → U9
- U3 → U11
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,11]: (U0→U7 ; U7→U11) ⇒ U0→U11
- [0,7,17]: (U0→U7 ; U7→U17) ⇒ U0→U17
- [0,9,11]: (U0→U9 ; U9→U11) ⇒ U0→U11
- [0,9,16]: (U0→U9 ; U9→U16) ⇒ U0→U16
- [0,11,17]: (U0→U11 ; U11→U17) ⇒ U0→U17
- [0,14,17]: (U0→U14 ; U14→U17) ⇒ U0→U17
- [1,8,13]: (U1→U8 ; U8→U13) ⇒ U1→U13
- [2,12,15]: (U2→U12 ; U12→U15) ⇒ U2→U15
- [3,9,11]: (U3→U9 ; U9→U11) ⇒ U3→U11
- [3,9,12]: (U3→U9 ; U9→U12) ⇒ U3→U12
- [4,10,13]: (U4→U10 ; U10→U13) ⇒ U4→U13
- [5,9,12]: (U5→U9 ; U9→U12) ⇒ U5→U12
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,7,11,17]
- [5,9,12,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 75 0-cells, 218 1-cells, 192 2-cells, 48 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,9}
- {0} → {0,11}
- {0} → {0,14}
- {0} → {0,16}
- {0} → {0,17}
- {0} → {0,7,11}
- {0} → {0,7,17}
- {0} → {0,9,11}
- {0} → {0,9,16}
- {0} → {0,11,17}
- {0} → {0,14,17}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,53]: ({0}→{0,7} ; {0,7}→{0,7,11}) ⇒ {0}→{0,7,11}
- [0,18,54]: ({0}→{0,7} ; {0,7}→{0,7,17}) ⇒ {0}→{0,7,17}
- [0,18,73]: ({0}→{0,7} ; {0,7}→{0,7,11,17}) ⇒ {0}→{0,7,11,17}
- [0,19,55]: ({0}→{0,9} ; {0,9}→{0,9,11}) ⇒ {0}→{0,9,11}
- [0,19,56]: ({0}→{0,9} ; {0,9}→{0,9,16}) ⇒ {0}→{0,9,16}
- [0,20,53]: ({0}→{0,11} ; {0,11}→{0,7,11}) ⇒ {0}→{0,7,11}
- [0,20,55]: ({0}→{0,11} ; {0,11}→{0,9,11}) ⇒ {0}→{0,9,11}
- [0,20,57]: ({0}→{0,11} ; {0,11}→{0,11,17}) ⇒ {0}→{0,11,17}
- [0,20,73]: ({0}→{0,11} ; {0,11}→{0,7,11,17}) ⇒ {0}→{0,7,11,17}
- [0,21,58]: ({0}→{0,14} ; {0,14}→{0,14,17}) ⇒ {0}→{0,14,17}
- [0,22,56]: ({0}→{0,16} ; {0,16}→{0,9,16}) ⇒ {0}→{0,9,16}
- [0,23,54]: ({0}→{0,17} ; {0,17}→{0,7,17}) ⇒ {0}→{0,7,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,53,73]
- [0,18,54,73]
- [0,20,53,73]
- [0,20,57,73]
- [0,23,54,73]
- [0,23,57,73]
- [5,34,64,74]
- [5,34,65,74]
- [5,35,64,74]
- [5,35,67,74]
- [5,37,65,74]
- [5,37,67,74]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

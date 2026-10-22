# homotopy.io export: CATH domain 3pmqA02 (mdCATH), heavy atoms (`mdcath-3pmqa02-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 37 1-cells, 17 2-cells, 1 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U9
- U0 → U11
- U0 → U14
- U0 → U15
- U0 → U17
- U1 → U8
- U1 → U13
- U2 → U10
- U2 → U12
- U3 → U7
- U3 → U8
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,15]: (U0→U7 ; U7→U15) ⇒ U0→U15
- [0,7,17]: (U0→U7 ; U7→U17) ⇒ U0→U17
- [0,9,11]: (U0→U9 ; U9→U11) ⇒ U0→U11
- [0,9,15]: (U0→U9 ; U9→U15) ⇒ U0→U15
- [0,14,17]: (U0→U14 ; U14→U17) ⇒ U0→U17
- [0,15,17]: (U0→U15 ; U15→U17) ⇒ U0→U17
- [2,10,12]: (U2→U10 ; U10→U12) ⇒ U2→U12
- [3,7,16]: (U3→U7 ; U7→U16) ⇒ U3→U16
- [4,9,11]: (U4→U9 ; U9→U11) ⇒ U4→U11
- [4,9,12]: (U4→U9 ; U9→U12) ⇒ U4→U12
- [5,7,15]: (U5→U7 ; U7→U15) ⇒ U5→U15
- [5,9,15]: (U5→U9 ; U9→U15) ⇒ U5→U15
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,7,15,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 73 0-cells, 190 1-cells, 138 2-cells, 24 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,9}
- {0} → {0,11}
- {0} → {0,14}
- {0} → {0,15}
- {0} → {0,17}
- {0} → {0,7,15}
- {0} → {0,7,17}
- {0} → {0,9,11}
- {0} → {0,9,15}
- {0} → {0,14,17}
- {0} → {0,15,17}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,55]: ({0}→{0,7} ; {0,7}→{0,7,15}) ⇒ {0}→{0,7,15}
- [0,18,56]: ({0}→{0,7} ; {0,7}→{0,7,17}) ⇒ {0}→{0,7,17}
- [0,18,72]: ({0}→{0,7} ; {0,7}→{0,7,15,17}) ⇒ {0}→{0,7,15,17}
- [0,19,57]: ({0}→{0,9} ; {0,9}→{0,9,11}) ⇒ {0}→{0,9,11}
- [0,19,58]: ({0}→{0,9} ; {0,9}→{0,9,15}) ⇒ {0}→{0,9,15}
- [0,20,57]: ({0}→{0,11} ; {0,11}→{0,9,11}) ⇒ {0}→{0,9,11}
- [0,21,59]: ({0}→{0,14} ; {0,14}→{0,14,17}) ⇒ {0}→{0,14,17}
- [0,22,55]: ({0}→{0,15} ; {0,15}→{0,7,15}) ⇒ {0}→{0,7,15}
- [0,22,58]: ({0}→{0,15} ; {0,15}→{0,9,15}) ⇒ {0}→{0,9,15}
- [0,22,60]: ({0}→{0,15} ; {0,15}→{0,15,17}) ⇒ {0}→{0,15,17}
- [0,22,72]: ({0}→{0,15} ; {0,15}→{0,7,15,17}) ⇒ {0}→{0,7,15,17}
- [0,23,56]: ({0}→{0,17} ; {0,17}→{0,7,17}) ⇒ {0}→{0,7,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,55,72]
- [0,18,56,72]
- [0,22,55,72]
- [0,22,60,72]
- [0,23,56,72]
- [0,23,60,72]
- [7,18,55,72]
- [7,18,56,72]
- [7,44,55,72]
- [7,44,70,72]
- [7,46,56,72]
- [7,46,70,72]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

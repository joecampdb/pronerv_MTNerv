# homotopy.io export: CATH domain 2j8gA03 (mdCATH), heavy atoms (`mdcath-2j8ga03-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 35 1-cells, 17 2-cells, 2 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U10
- U0 → U11
- U0 → U17
- U2 → U9
- U2 → U12
- U2 → U13
- U3 → U7
- U3 → U10
- U3 → U12
- U3 → U14
- U4 → U8
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,10,17]: (U0→U10 ; U10→U17) ⇒ U0→U17
- [0,11,17]: (U0→U11 ; U11→U17) ⇒ U0→U17
- [2,9,13]: (U2→U9 ; U9→U13) ⇒ U2→U13
- [3,10,14]: (U3→U10 ; U10→U14) ⇒ U3→U14
- [4,8,16]: (U4→U8 ; U8→U16) ⇒ U4→U16
- [4,13,15]: (U4→U13 ; U13→U15) ⇒ U4→U15
- [4,13,16]: (U4→U13 ; U13→U16) ⇒ U4→U16
- [4,15,16]: (U4→U15 ; U15→U16) ⇒ U4→U16
- [5,11,14]: (U5→U11 ; U11→U14) ⇒ U5→U14
- [5,11,17]: (U5→U11 ; U11→U17) ⇒ U5→U17
- [5,14,17]: (U5→U14 ; U14→U17) ⇒ U5→U17
- [6,8,16]: (U6→U8 ; U8→U16) ⇒ U6→U16
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [4,13,15,16]
- [5,11,14,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 72 0-cells, 200 1-cells, 174 2-cells, 48 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,10}
- {0} → {0,11}
- {0} → {0,17}
- {0} → {0,10,17}
- {0} → {0,11,17}
- {2} → {2,9}
- {2} → {2,12}
- {2} → {2,13}
- {2} → {2,9,13}
- {3} → {3,7}
- {3} → {3,10}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,19,53]: ({0}→{0,10} ; {0,10}→{0,10,17}) ⇒ {0}→{0,10,17}
- [0,20,54]: ({0}→{0,11} ; {0,11}→{0,11,17}) ⇒ {0}→{0,11,17}
- [0,21,53]: ({0}→{0,17} ; {0,17}→{0,10,17}) ⇒ {0}→{0,10,17}
- [0,21,54]: ({0}→{0,17} ; {0,17}→{0,11,17}) ⇒ {0}→{0,11,17}
- [2,22,55]: ({2}→{2,9} ; {2,9}→{2,9,13}) ⇒ {2}→{2,9,13}
- [2,24,55]: ({2}→{2,13} ; {2,13}→{2,9,13}) ⇒ {2}→{2,9,13}
- [3,26,56]: ({3}→{3,10} ; {3,10}→{3,10,14}) ⇒ {3}→{3,10,14}
- [3,28,56]: ({3}→{3,14} ; {3,14}→{3,10,14}) ⇒ {3}→{3,10,14}
- [4,29,57]: ({4}→{4,8} ; {4,8}→{4,8,16}) ⇒ {4}→{4,8,16}
- [4,30,58]: ({4}→{4,13} ; {4,13}→{4,13,15}) ⇒ {4}→{4,13,15}
- [4,30,59]: ({4}→{4,13} ; {4,13}→{4,13,16}) ⇒ {4}→{4,13,16}
- [4,30,70]: ({4}→{4,13} ; {4,13}→{4,13,15,16}) ⇒ {4}→{4,13,15,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [4,30,58,70]
- [4,30,59,70]
- [4,31,58,70]
- [4,31,60,70]
- [4,32,59,70]
- [4,32,60,70]
- [5,33,61,71]
- [5,33,62,71]
- [5,34,61,71]
- [5,34,63,71]
- [5,35,62,71]
- [5,35,63,71]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

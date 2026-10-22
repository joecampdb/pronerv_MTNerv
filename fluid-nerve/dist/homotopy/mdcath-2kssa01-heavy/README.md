# homotopy.io export: CATH domain 2kssA01 (mdCATH), heavy atoms (`mdcath-2kssa01-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 31 1-cells, 14 2-cells, 1 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U11
- U0 → U12
- U0 → U16
- U2 → U15
- U3 → U8
- U3 → U9
- U3 → U10
- U3 → U14
- U3 → U17
- U4 → U13
- U5 → U9
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,16]: (U0→U8 ; U8→U16) ⇒ U0→U16
- [0,11,12]: (U0→U11 ; U11→U12) ⇒ U0→U12
- [3,8,14]: (U3→U8 ; U8→U14) ⇒ U3→U14
- [3,8,17]: (U3→U8 ; U8→U17) ⇒ U3→U17
- [3,9,14]: (U3→U9 ; U9→U14) ⇒ U3→U14
- [3,10,17]: (U3→U10 ; U10→U17) ⇒ U3→U17
- [3,14,17]: (U3→U14 ; U14→U17) ⇒ U3→U17
- [5,9,14]: (U5→U9 ; U9→U14) ⇒ U5→U14
- [5,11,13]: (U5→U11 ; U11→U13) ⇒ U5→U13
- [6,10,17]: (U6→U10 ; U10→U17) ⇒ U6→U17
- [6,16,17]: (U6→U16 ; U16→U17) ⇒ U6→U17
- [7,11,12]: (U7→U11 ; U11→U12) ⇒ U7→U12
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [3,8,14,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 64 0-cells, 160 1-cells, 120 2-cells, 24 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,11}
- {0} → {0,12}
- {0} → {0,16}
- {0} → {0,8,16}
- {0} → {0,11,12}
- {2} → {2,15}
- {3} → {3,8}
- {3} → {3,9}
- {3} → {3,10}
- {3} → {3,14}
- {3} → {3,17}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,49]: ({0}→{0,8} ; {0,8}→{0,8,16}) ⇒ {0}→{0,8,16}
- [0,19,50]: ({0}→{0,11} ; {0,11}→{0,11,12}) ⇒ {0}→{0,11,12}
- [0,20,50]: ({0}→{0,12} ; {0,12}→{0,11,12}) ⇒ {0}→{0,11,12}
- [0,21,49]: ({0}→{0,16} ; {0,16}→{0,8,16}) ⇒ {0}→{0,8,16}
- [3,23,51]: ({3}→{3,8} ; {3,8}→{3,8,14}) ⇒ {3}→{3,8,14}
- [3,23,52]: ({3}→{3,8} ; {3,8}→{3,8,17}) ⇒ {3}→{3,8,17}
- [3,23,63]: ({3}→{3,8} ; {3,8}→{3,8,14,17}) ⇒ {3}→{3,8,14,17}
- [3,24,53]: ({3}→{3,9} ; {3,9}→{3,9,14}) ⇒ {3}→{3,9,14}
- [3,25,54]: ({3}→{3,10} ; {3,10}→{3,10,17}) ⇒ {3}→{3,10,17}
- [3,26,51]: ({3}→{3,14} ; {3,14}→{3,8,14}) ⇒ {3}→{3,8,14}
- [3,26,53]: ({3}→{3,14} ; {3,14}→{3,9,14}) ⇒ {3}→{3,9,14}
- [3,26,55]: ({3}→{3,14} ; {3,14}→{3,14,17}) ⇒ {3}→{3,14,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [3,23,51,63]
- [3,23,52,63]
- [3,26,51,63]
- [3,26,55,63]
- [3,27,52,63]
- [3,27,55,63]
- [8,23,51,63]
- [8,23,52,63]
- [8,40,51,63]
- [8,40,61,63]
- [8,42,52,63]
- [8,42,61,63]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

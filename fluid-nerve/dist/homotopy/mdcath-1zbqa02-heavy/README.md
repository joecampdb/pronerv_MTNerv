# homotopy.io export: CATH domain 1zbqA02 (mdCATH), heavy atoms (`mdcath-1zbqa02-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 34 1-cells, 13 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U11
- U0 → U14
- U0 → U16
- U1 → U9
- U1 → U10
- U2 → U13
- U2 → U15
- U3 → U8
- U3 → U17
- U4 → U8
- U4 → U10
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,16]: (U0→U8 ; U8→U16) ⇒ U0→U16
- [0,11,14]: (U0→U11 ; U11→U14) ⇒ U0→U14
- [2,13,15]: (U2→U13 ; U13→U15) ⇒ U2→U15
- [3,8,17]: (U3→U8 ; U8→U17) ⇒ U3→U17
- [4,8,12]: (U4→U8 ; U8→U12) ⇒ U4→U12
- [4,11,13]: (U4→U11 ; U11→U13) ⇒ U4→U13
- [4,13,15]: (U4→U13 ; U13→U15) ⇒ U4→U15
- [5,10,15]: (U5→U10 ; U10→U15) ⇒ U5→U15
- [6,11,13]: (U6→U11 ; U11→U13) ⇒ U6→U13
- [6,11,14]: (U6→U11 ; U11→U14) ⇒ U6→U14
- [7,8,16]: (U7→U8 ; U8→U16) ⇒ U7→U16
- [7,8,17]: (U7→U8 ; U8→U17) ⇒ U7→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 65 0-cells, 146 1-cells, 78 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,11}
- {0} → {0,14}
- {0} → {0,16}
- {0} → {0,8,16}
- {0} → {0,11,14}
- {1} → {1,9}
- {1} → {1,10}
- {2} → {2,13}
- {2} → {2,15}
- {2} → {2,13,15}
- {3} → {3,8}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,52]: ({0}→{0,8} ; {0,8}→{0,8,16}) ⇒ {0}→{0,8,16}
- [0,19,53]: ({0}→{0,11} ; {0,11}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,20,53]: ({0}→{0,14} ; {0,14}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,21,52]: ({0}→{0,16} ; {0,16}→{0,8,16}) ⇒ {0}→{0,8,16}
- [2,24,54]: ({2}→{2,13} ; {2,13}→{2,13,15}) ⇒ {2}→{2,13,15}
- [2,25,54]: ({2}→{2,15} ; {2,15}→{2,13,15}) ⇒ {2}→{2,13,15}
- [3,26,55]: ({3}→{3,8} ; {3,8}→{3,8,17}) ⇒ {3}→{3,8,17}
- [3,27,55]: ({3}→{3,17} ; {3,17}→{3,8,17}) ⇒ {3}→{3,8,17}
- [4,28,56]: ({4}→{4,8} ; {4,8}→{4,8,12}) ⇒ {4}→{4,8,12}
- [4,30,57]: ({4}→{4,11} ; {4,11}→{4,11,13}) ⇒ {4}→{4,11,13}
- [4,31,56]: ({4}→{4,12} ; {4,12}→{4,8,12}) ⇒ {4}→{4,8,12}
- [4,32,57]: ({4}→{4,13} ; {4,13}→{4,11,13}) ⇒ {4}→{4,11,13}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

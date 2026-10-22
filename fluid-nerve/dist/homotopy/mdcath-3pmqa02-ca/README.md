# homotopy.io export: CATH domain 3pmqA02 (mdCATH), C-alpha (`mdcath-3pmqa02-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 35 1-cells, 15 2-cells, 1 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U11
- U0 → U12
- U0 → U16
- U1 → U7
- U1 → U9
- U1 → U13
- U2 → U10
- U2 → U14
- U3 → U7
- U3 → U8
- U3 → U15
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,12,16]: (U0→U12 ; U12→U16) ⇒ U0→U16
- [1,9,13]: (U1→U9 ; U9→U13) ⇒ U1→U13
- [2,10,14]: (U2→U10 ; U10→U14) ⇒ U2→U14
- [3,7,17]: (U3→U7 ; U7→U17) ⇒ U3→U17
- [3,8,15]: (U3→U8 ; U8→U15) ⇒ U3→U15
- [4,10,12]: (U4→U10 ; U10→U12) ⇒ U4→U12
- [4,10,16]: (U4→U10 ; U10→U16) ⇒ U4→U16
- [4,12,16]: (U4→U12 ; U12→U16) ⇒ U4→U16
- [5,8,15]: (U5→U8 ; U8→U15) ⇒ U5→U15
- [6,9,13]: (U6→U9 ; U9→U13) ⇒ U6→U13
- [6,9,14]: (U6→U9 ; U9→U14) ⇒ U6→U14
- [6,10,12]: (U6→U10 ; U10→U12) ⇒ U6→U12
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [4,10,12,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 69 0-cells, 174 1-cells, 126 2-cells, 24 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,11}
- {0} → {0,12}
- {0} → {0,16}
- {0} → {0,12,16}
- {1} → {1,7}
- {1} → {1,9}
- {1} → {1,13}
- {1} → {1,9,13}
- {2} → {2,10}
- {2} → {2,14}
- {2} → {2,10,14}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,20,53]: ({0}→{0,12} ; {0,12}→{0,12,16}) ⇒ {0}→{0,12,16}
- [0,21,53]: ({0}→{0,16} ; {0,16}→{0,12,16}) ⇒ {0}→{0,12,16}
- [1,23,54]: ({1}→{1,9} ; {1,9}→{1,9,13}) ⇒ {1}→{1,9,13}
- [1,24,54]: ({1}→{1,13} ; {1,13}→{1,9,13}) ⇒ {1}→{1,9,13}
- [2,25,55]: ({2}→{2,10} ; {2,10}→{2,10,14}) ⇒ {2}→{2,10,14}
- [2,26,55]: ({2}→{2,14} ; {2,14}→{2,10,14}) ⇒ {2}→{2,10,14}
- [3,27,56]: ({3}→{3,7} ; {3,7}→{3,7,17}) ⇒ {3}→{3,7,17}
- [3,28,57]: ({3}→{3,8} ; {3,8}→{3,8,15}) ⇒ {3}→{3,8,15}
- [3,29,57]: ({3}→{3,15} ; {3,15}→{3,8,15}) ⇒ {3}→{3,8,15}
- [3,30,56]: ({3}→{3,17} ; {3,17}→{3,7,17}) ⇒ {3}→{3,7,17}
- [4,31,58]: ({4}→{4,10} ; {4,10}→{4,10,12}) ⇒ {4}→{4,10,12}
- [4,31,59]: ({4}→{4,10} ; {4,10}→{4,10,16}) ⇒ {4}→{4,10,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [4,31,58,68]
- [4,31,59,68]
- [4,32,58,68]
- [4,32,60,68]
- [4,33,59,68]
- [4,33,60,68]
- [10,31,58,68]
- [10,31,59,68]
- [10,49,58,68]
- [10,49,67,68]
- [10,51,59,68]
- [10,51,67,68]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

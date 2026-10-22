# homotopy.io export: Ac-Ala3-NHMe (MD22 ab initio MD) (`sgdml-md22-ac-ala3-nhme`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 34 1-cells, 12 2-cells, 1 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U9
- U0 → U10
- U0 → U11
- U1 → U14
- U2 → U7
- U2 → U13
- U2 → U16
- U2 → U17
- U3 → U8
- U3 → U12
- U3 → U15
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,9,11]: (U0→U9 ; U9→U11) ⇒ U0→U11
- [2,7,16]: (U2→U7 ; U7→U16) ⇒ U2→U16
- [2,13,16]: (U2→U13 ; U13→U16) ⇒ U2→U16
- [2,13,17]: (U2→U13 ; U13→U17) ⇒ U2→U17
- [3,8,12]: (U3→U8 ; U8→U12) ⇒ U3→U12
- [3,8,15]: (U3→U8 ; U8→U15) ⇒ U3→U15
- [5,7,10]: (U5→U7 ; U7→U10) ⇒ U5→U10
- [5,7,14]: (U5→U7 ; U7→U14) ⇒ U5→U14
- [5,10,14]: (U5→U10 ; U10→U14) ⇒ U5→U14
- [6,13,17]: (U6→U13 ; U13→U17) ⇒ U6→U17
- [7,10,13]: (U7→U10 ; U10→U13) ⇒ U7→U13
- [7,10,14]: (U7→U10 ; U10→U14) ⇒ U7→U14

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [5,7,10,14]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 65 0-cells, 154 1-cells, 108 2-cells, 24 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,10}
- {0} → {0,11}
- {0} → {0,9,11}
- {1} → {1,14}
- {2} → {2,7}
- {2} → {2,13}
- {2} → {2,16}
- {2} → {2,17}
- {2} → {2,7,16}
- {2} → {2,13,16}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,19,52]: ({0}→{0,9} ; {0,9}→{0,9,11}) ⇒ {0}→{0,9,11}
- [0,21,52]: ({0}→{0,11} ; {0,11}→{0,9,11}) ⇒ {0}→{0,9,11}
- [2,23,53]: ({2}→{2,7} ; {2,7}→{2,7,16}) ⇒ {2}→{2,7,16}
- [2,24,54]: ({2}→{2,13} ; {2,13}→{2,13,16}) ⇒ {2}→{2,13,16}
- [2,24,55]: ({2}→{2,13} ; {2,13}→{2,13,17}) ⇒ {2}→{2,13,17}
- [2,25,53]: ({2}→{2,16} ; {2,16}→{2,7,16}) ⇒ {2}→{2,7,16}
- [2,25,54]: ({2}→{2,16} ; {2,16}→{2,13,16}) ⇒ {2}→{2,13,16}
- [2,26,55]: ({2}→{2,17} ; {2,17}→{2,13,17}) ⇒ {2}→{2,13,17}
- [3,27,56]: ({3}→{3,8} ; {3,8}→{3,8,12}) ⇒ {3}→{3,8,12}
- [3,27,57]: ({3}→{3,8} ; {3,8}→{3,8,15}) ⇒ {3}→{3,8,15}
- [3,28,56]: ({3}→{3,12} ; {3,12}→{3,8,12}) ⇒ {3}→{3,8,12}
- [3,29,57]: ({3}→{3,15} ; {3,15}→{3,8,15}) ⇒ {3}→{3,8,15}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [5,33,58,64]
- [5,33,59,64]
- [5,35,58,64]
- [5,35,60,64]
- [5,37,59,64]
- [5,37,60,64]
- [7,33,58,64]
- [7,33,59,64]
- [7,41,58,64]
- [7,41,63,64]
- [7,43,59,64]
- [7,43,63,64]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

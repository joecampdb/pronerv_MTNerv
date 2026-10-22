# homotopy.io export: paracetamol (MD17 ab initio MD) (`sgdml-md17-paracetamol`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 34 1-cells, 20 2-cells, 4 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U8
- U0 → U13
- U0 → U17
- U1 → U9
- U1 → U11
- U1 → U15
- U2 → U7
- U2 → U10
- U3 → U6
- U3 → U7
- U3 → U12
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,13]: (U0→U6 ; U6→U13) ⇒ U0→U13
- [0,8,17]: (U0→U8 ; U8→U17) ⇒ U0→U17
- [1,9,15]: (U1→U9 ; U9→U15) ⇒ U1→U15
- [1,11,15]: (U1→U11 ; U11→U15) ⇒ U1→U15
- [3,6,12]: (U3→U6 ; U6→U12) ⇒ U3→U12
- [3,6,16]: (U3→U6 ; U6→U16) ⇒ U3→U16
- [3,7,12]: (U3→U7 ; U7→U12) ⇒ U3→U12
- [3,7,14]: (U3→U7 ; U7→U14) ⇒ U3→U14
- [3,12,14]: (U3→U12 ; U12→U14) ⇒ U3→U14
- [3,12,16]: (U3→U12 ; U12→U16) ⇒ U3→U16
- [3,14,16]: (U3→U14 ; U14→U16) ⇒ U3→U16
- [4,8,17]: (U4→U8 ; U8→U17) ⇒ U4→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [3,6,12,16]
- [3,7,12,14]
- [3,12,14,16]
- [6,12,13,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 76 0-cells, 244 1-cells, 264 2-cells, 96 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,8}
- {0} → {0,13}
- {0} → {0,17}
- {0} → {0,6,13}
- {0} → {0,8,17}
- {1} → {1,9}
- {1} → {1,11}
- {1} → {1,15}
- {1} → {1,9,15}
- {1} → {1,11,15}
- {2} → {2,7}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,52]: ({0}→{0,6} ; {0,6}→{0,6,13}) ⇒ {0}→{0,6,13}
- [0,19,53]: ({0}→{0,8} ; {0,8}→{0,8,17}) ⇒ {0}→{0,8,17}
- [0,20,52]: ({0}→{0,13} ; {0,13}→{0,6,13}) ⇒ {0}→{0,6,13}
- [0,21,53]: ({0}→{0,17} ; {0,17}→{0,8,17}) ⇒ {0}→{0,8,17}
- [1,22,54]: ({1}→{1,9} ; {1,9}→{1,9,15}) ⇒ {1}→{1,9,15}
- [1,23,55]: ({1}→{1,11} ; {1,11}→{1,11,15}) ⇒ {1}→{1,11,15}
- [1,24,54]: ({1}→{1,15} ; {1,15}→{1,9,15}) ⇒ {1}→{1,9,15}
- [1,24,55]: ({1}→{1,15} ; {1,15}→{1,11,15}) ⇒ {1}→{1,11,15}
- [3,27,56]: ({3}→{3,6} ; {3,6}→{3,6,12}) ⇒ {3}→{3,6,12}
- [3,27,57]: ({3}→{3,6} ; {3,6}→{3,6,16}) ⇒ {3}→{3,6,16}
- [3,27,72]: ({3}→{3,6} ; {3,6}→{3,6,12,16}) ⇒ {3}→{3,6,12,16}
- [3,28,58]: ({3}→{3,7} ; {3,7}→{3,7,12}) ⇒ {3}→{3,7,12}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [3,27,56,72]
- [3,27,57,72]
- [3,28,58,73]
- [3,28,59,73]
- [3,29,56,72]
- [3,29,58,73]
- [3,29,60,73]
- [3,29,60,74]
- [3,29,61,72]
- [3,29,61,74]
- [3,30,59,73]
- [3,30,60,73]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

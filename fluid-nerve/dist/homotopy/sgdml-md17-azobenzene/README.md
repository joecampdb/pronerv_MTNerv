# homotopy.io export: azobenzene (MD17 ab initio MD) (`sgdml-md17-azobenzene`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 31 1-cells, 14 2-cells, 1 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U8
- U0 → U11
- U0 → U15
- U1 → U12
- U1 → U13
- U2 → U6
- U2 → U10
- U2 → U14
- U3 → U7
- U3 → U16
- U3 → U17
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,15]: (U0→U7 ; U7→U15) ⇒ U0→U15
- [0,8,11]: (U0→U8 ; U8→U11) ⇒ U0→U11
- [1,12,13]: (U1→U12 ; U12→U13) ⇒ U1→U13
- [2,6,10]: (U2→U6 ; U6→U10) ⇒ U2→U10
- [2,10,14]: (U2→U10 ; U10→U14) ⇒ U2→U14
- [3,7,16]: (U3→U7 ; U7→U16) ⇒ U3→U16
- [3,7,17]: (U3→U7 ; U7→U17) ⇒ U3→U17
- [3,16,17]: (U3→U16 ; U16→U17) ⇒ U3→U17
- [4,8,11]: (U4→U8 ; U8→U11) ⇒ U4→U11
- [4,8,12]: (U4→U8 ; U8→U12) ⇒ U4→U12
- [5,7,16]: (U5→U7 ; U7→U16) ⇒ U5→U16
- [5,9,14]: (U5→U9 ; U9→U14) ⇒ U5→U14
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [3,7,16,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 64 0-cells, 160 1-cells, 120 2-cells, 24 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,8}
- {0} → {0,11}
- {0} → {0,15}
- {0} → {0,7,15}
- {0} → {0,8,11}
- {1} → {1,12}
- {1} → {1,13}
- {1} → {1,12,13}
- {2} → {2,6}
- {2} → {2,10}
- {2} → {2,14}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,49]: ({0}→{0,7} ; {0,7}→{0,7,15}) ⇒ {0}→{0,7,15}
- [0,19,50]: ({0}→{0,8} ; {0,8}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,20,50]: ({0}→{0,11} ; {0,11}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,21,49]: ({0}→{0,15} ; {0,15}→{0,7,15}) ⇒ {0}→{0,7,15}
- [1,22,51]: ({1}→{1,12} ; {1,12}→{1,12,13}) ⇒ {1}→{1,12,13}
- [1,23,51]: ({1}→{1,13} ; {1,13}→{1,12,13}) ⇒ {1}→{1,12,13}
- [2,24,52]: ({2}→{2,6} ; {2,6}→{2,6,10}) ⇒ {2}→{2,6,10}
- [2,25,52]: ({2}→{2,10} ; {2,10}→{2,6,10}) ⇒ {2}→{2,6,10}
- [2,25,53]: ({2}→{2,10} ; {2,10}→{2,10,14}) ⇒ {2}→{2,10,14}
- [2,26,53]: ({2}→{2,14} ; {2,14}→{2,10,14}) ⇒ {2}→{2,10,14}
- [3,27,54]: ({3}→{3,7} ; {3,7}→{3,7,16}) ⇒ {3}→{3,7,16}
- [3,27,55]: ({3}→{3,7} ; {3,7}→{3,7,17}) ⇒ {3}→{3,7,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [3,27,54,63]
- [3,27,55,63]
- [3,28,54,63]
- [3,28,56,63]
- [3,29,55,63]
- [3,29,56,63]
- [7,27,54,63]
- [7,27,55,63]
- [7,40,54,63]
- [7,40,62,63]
- [7,41,55,63]
- [7,41,62,63]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

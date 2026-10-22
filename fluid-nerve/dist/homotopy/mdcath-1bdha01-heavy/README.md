# homotopy.io export: CATH domain 1bdhA01 (mdCATH), heavy atoms (`mdcath-1bdha01-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 38 1-cells, 21 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U9
- U0 → U13
- U0 → U15
- U1 → U7
- U1 → U10
- U1 → U11
- U2 → U12
- U2 → U16
- U3 → U7
- U3 → U8
- U3 → U14
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,9]: (U0→U8 ; U8→U9) ⇒ U0→U9
- [0,8,13]: (U0→U8 ; U8→U13) ⇒ U0→U13
- [0,13,15]: (U0→U13 ; U13→U15) ⇒ U0→U15
- [1,7,10]: (U1→U7 ; U7→U10) ⇒ U1→U10
- [1,10,11]: (U1→U10 ; U10→U11) ⇒ U1→U11
- [2,12,16]: (U2→U12 ; U12→U16) ⇒ U2→U16
- [3,7,17]: (U3→U7 ; U7→U17) ⇒ U3→U17
- [3,8,17]: (U3→U8 ; U8→U17) ⇒ U3→U17
- [3,14,17]: (U3→U14 ; U14→U17) ⇒ U3→U17
- [4,9,14]: (U4→U9 ; U9→U14) ⇒ U4→U14
- [5,8,10]: (U5→U8 ; U8→U10) ⇒ U5→U10
- [5,8,13]: (U5→U8 ; U8→U13) ⇒ U5→U13
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 77 0-cells, 202 1-cells, 126 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,13}
- {0} → {0,15}
- {0} → {0,8,9}
- {0} → {0,8,13}
- {0} → {0,13,15}
- {1} → {1,7}
- {1} → {1,10}
- {1} → {1,11}
- {1} → {1,7,10}
- {1} → {1,10,11}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,56]: ({0}→{0,8} ; {0,8}→{0,8,9}) ⇒ {0}→{0,8,9}
- [0,18,57]: ({0}→{0,8} ; {0,8}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,19,56]: ({0}→{0,9} ; {0,9}→{0,8,9}) ⇒ {0}→{0,8,9}
- [0,20,57]: ({0}→{0,13} ; {0,13}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,20,58]: ({0}→{0,13} ; {0,13}→{0,13,15}) ⇒ {0}→{0,13,15}
- [0,21,58]: ({0}→{0,15} ; {0,15}→{0,13,15}) ⇒ {0}→{0,13,15}
- [1,22,59]: ({1}→{1,7} ; {1,7}→{1,7,10}) ⇒ {1}→{1,7,10}
- [1,23,59]: ({1}→{1,10} ; {1,10}→{1,7,10}) ⇒ {1}→{1,7,10}
- [1,23,60]: ({1}→{1,10} ; {1,10}→{1,10,11}) ⇒ {1}→{1,10,11}
- [1,24,60]: ({1}→{1,11} ; {1,11}→{1,10,11}) ⇒ {1}→{1,10,11}
- [2,25,61]: ({2}→{2,12} ; {2,12}→{2,12,16}) ⇒ {2}→{2,12,16}
- [2,26,61]: ({2}→{2,16} ; {2,16}→{2,12,16}) ⇒ {2}→{2,12,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

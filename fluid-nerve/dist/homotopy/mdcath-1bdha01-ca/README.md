# homotopy.io export: CATH domain 1bdhA01 (mdCATH), C-alpha (`mdcath-1bdha01-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 38 1-cells, 20 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U8
- U0 → U14
- U0 → U16
- U1 → U9
- U1 → U10
- U1 → U13
- U2 → U11
- U2 → U12
- U2 → U15
- U3 → U8
- U4 → U7
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,8]: (U0→U7 ; U7→U8) ⇒ U0→U8
- [0,7,14]: (U0→U7 ; U7→U14) ⇒ U0→U14
- [0,8,16]: (U0→U8 ; U8→U16) ⇒ U0→U16
- [1,10,13]: (U1→U10 ; U10→U13) ⇒ U1→U13
- [2,11,12]: (U2→U11 ; U11→U12) ⇒ U2→U12
- [2,12,15]: (U2→U12 ; U12→U15) ⇒ U2→U15
- [4,7,10]: (U4→U7 ; U7→U10) ⇒ U4→U10
- [4,7,14]: (U4→U7 ; U7→U14) ⇒ U4→U14
- [4,9,10]: (U4→U9 ; U9→U10) ⇒ U4→U10
- [4,11,12]: (U4→U11 ; U11→U12) ⇒ U4→U12
- [4,12,14]: (U4→U12 ; U12→U14) ⇒ U4→U14
- [5,7,17]: (U5→U7 ; U7→U17) ⇒ U5→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 76 0-cells, 196 1-cells, 120 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,8}
- {0} → {0,14}
- {0} → {0,16}
- {0} → {0,7,8}
- {0} → {0,7,14}
- {0} → {0,8,16}
- {1} → {1,9}
- {1} → {1,10}
- {1} → {1,13}
- {1} → {1,10,13}
- {2} → {2,11}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,56]: ({0}→{0,7} ; {0,7}→{0,7,8}) ⇒ {0}→{0,7,8}
- [0,18,57]: ({0}→{0,7} ; {0,7}→{0,7,14}) ⇒ {0}→{0,7,14}
- [0,19,56]: ({0}→{0,8} ; {0,8}→{0,7,8}) ⇒ {0}→{0,7,8}
- [0,19,58]: ({0}→{0,8} ; {0,8}→{0,8,16}) ⇒ {0}→{0,8,16}
- [0,20,57]: ({0}→{0,14} ; {0,14}→{0,7,14}) ⇒ {0}→{0,7,14}
- [0,21,58]: ({0}→{0,16} ; {0,16}→{0,8,16}) ⇒ {0}→{0,8,16}
- [1,23,59]: ({1}→{1,10} ; {1,10}→{1,10,13}) ⇒ {1}→{1,10,13}
- [1,24,59]: ({1}→{1,13} ; {1,13}→{1,10,13}) ⇒ {1}→{1,10,13}
- [2,25,60]: ({2}→{2,11} ; {2,11}→{2,11,12}) ⇒ {2}→{2,11,12}
- [2,26,60]: ({2}→{2,12} ; {2,12}→{2,11,12}) ⇒ {2}→{2,11,12}
- [2,26,61]: ({2}→{2,12} ; {2,12}→{2,12,15}) ⇒ {2}→{2,12,15}
- [2,27,61]: ({2}→{2,15} ; {2,15}→{2,12,15}) ⇒ {2}→{2,12,15}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

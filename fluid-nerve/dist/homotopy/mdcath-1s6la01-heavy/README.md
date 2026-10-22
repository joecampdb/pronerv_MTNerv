# homotopy.io export: CATH domain 1s6lA01 (mdCATH), heavy atoms (`mdcath-1s6la01-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 51 1-cells, 49 2-cells, 16 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U11
- U0 → U13
- U0 → U17
- U1 → U6
- U1 → U9
- U1 → U10
- U2 → U7
- U2 → U12
- U3 → U5
- U3 → U7
- U3 → U8
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,11]: (U0→U8 ; U8→U11) ⇒ U0→U11
- [0,8,13]: (U0→U8 ; U8→U13) ⇒ U0→U13
- [0,11,13]: (U0→U11 ; U11→U13) ⇒ U0→U13
- [0,11,17]: (U0→U11 ; U11→U17) ⇒ U0→U17
- [0,13,17]: (U0→U13 ; U13→U17) ⇒ U0→U17
- [1,6,10]: (U1→U6 ; U6→U10) ⇒ U1→U10
- [1,9,10]: (U1→U9 ; U9→U10) ⇒ U1→U10
- [2,7,12]: (U2→U7 ; U7→U12) ⇒ U2→U12
- [3,5,8]: (U3→U5 ; U5→U8) ⇒ U3→U8
- [3,5,10]: (U3→U5 ; U5→U10) ⇒ U3→U10
- [3,5,16]: (U3→U5 ; U5→U16) ⇒ U3→U16
- [3,7,9]: (U3→U7 ; U7→U9) ⇒ U3→U9
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,8,11,13]
- [3,5,8,16]
- [3,5,10,16]
- [3,7,9,14]
- [3,7,14,15]
- [3,8,13,15]
- [3,8,15,16]
- [3,9,10,14]
- [3,9,10,16]
- [3,9,14,16]
- [3,10,14,16]
- [3,14,15,16]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 134 0-cells, 620 1-cells, 870 2-cells, 384 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,11}
- {0} → {0,13}
- {0} → {0,17}
- {0} → {0,8,11}
- {0} → {0,8,13}
- {0} → {0,11,13}
- {0} → {0,11,17}
- {0} → {0,13,17}
- {0} → {0,8,11,13}
- {1} → {1,6}
- {1} → {1,9}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,69]: ({0}→{0,8} ; {0,8}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,18,70]: ({0}→{0,8} ; {0,8}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,18,118]: ({0}→{0,8} ; {0,8}→{0,8,11,13}) ⇒ {0}→{0,8,11,13}
- [0,19,69]: ({0}→{0,11} ; {0,11}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,19,71]: ({0}→{0,11} ; {0,11}→{0,11,13}) ⇒ {0}→{0,11,13}
- [0,19,72]: ({0}→{0,11} ; {0,11}→{0,11,17}) ⇒ {0}→{0,11,17}
- [0,19,118]: ({0}→{0,11} ; {0,11}→{0,8,11,13}) ⇒ {0}→{0,8,11,13}
- [0,20,70]: ({0}→{0,13} ; {0,13}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,20,71]: ({0}→{0,13} ; {0,13}→{0,11,13}) ⇒ {0}→{0,11,13}
- [0,20,73]: ({0}→{0,13} ; {0,13}→{0,13,17}) ⇒ {0}→{0,13,17}
- [0,20,118]: ({0}→{0,13} ; {0,13}→{0,8,11,13}) ⇒ {0}→{0,8,11,13}
- [0,21,72]: ({0}→{0,17} ; {0,17}→{0,11,17}) ⇒ {0}→{0,11,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,69,118]
- [0,18,70,118]
- [0,19,69,118]
- [0,19,71,118]
- [0,20,70,118]
- [0,20,71,118]
- [3,27,77,119]
- [3,27,78,120]
- [3,27,79,119]
- [3,27,79,120]
- [3,28,80,121]
- [3,28,81,121]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

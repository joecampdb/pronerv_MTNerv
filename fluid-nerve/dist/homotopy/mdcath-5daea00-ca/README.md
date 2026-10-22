# homotopy.io export: CATH domain 5daeA00 (mdCATH), C-alpha (`mdcath-5daea00-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 38 1-cells, 16 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U8
- U0 → U10
- U0 → U12
- U0 → U14
- U0 → U15
- U1 → U13
- U2 → U6
- U2 → U9
- U2 → U16
- U3 → U7
- U3 → U9
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,15]: (U0→U7 ; U7→U15) ⇒ U0→U15
- [0,8,10]: (U0→U8 ; U8→U10) ⇒ U0→U10
- [0,8,14]: (U0→U8 ; U8→U14) ⇒ U0→U14
- [0,10,15]: (U0→U10 ; U10→U15) ⇒ U0→U15
- [0,12,14]: (U0→U12 ; U12→U14) ⇒ U0→U14
- [0,12,15]: (U0→U12 ; U12→U15) ⇒ U0→U15
- [2,6,16]: (U2→U6 ; U6→U16) ⇒ U2→U16
- [3,7,10]: (U3→U7 ; U7→U10) ⇒ U3→U10
- [4,6,16]: (U4→U6 ; U6→U16) ⇒ U4→U16
- [4,8,17]: (U4→U8 ; U8→U17) ⇒ U4→U17
- [4,11,16]: (U4→U11 ; U11→U16) ⇒ U4→U16
- [4,13,17]: (U4→U13 ; U13→U17) ⇒ U4→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 72 0-cells, 172 1-cells, 96 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,8}
- {0} → {0,10}
- {0} → {0,12}
- {0} → {0,14}
- {0} → {0,15}
- {0} → {0,7,15}
- {0} → {0,8,10}
- {0} → {0,8,14}
- {0} → {0,10,15}
- {0} → {0,12,14}
- {0} → {0,12,15}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,56]: ({0}→{0,7} ; {0,7}→{0,7,15}) ⇒ {0}→{0,7,15}
- [0,19,57]: ({0}→{0,8} ; {0,8}→{0,8,10}) ⇒ {0}→{0,8,10}
- [0,19,58]: ({0}→{0,8} ; {0,8}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,20,57]: ({0}→{0,10} ; {0,10}→{0,8,10}) ⇒ {0}→{0,8,10}
- [0,20,59]: ({0}→{0,10} ; {0,10}→{0,10,15}) ⇒ {0}→{0,10,15}
- [0,21,60]: ({0}→{0,12} ; {0,12}→{0,12,14}) ⇒ {0}→{0,12,14}
- [0,21,61]: ({0}→{0,12} ; {0,12}→{0,12,15}) ⇒ {0}→{0,12,15}
- [0,22,58]: ({0}→{0,14} ; {0,14}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,22,60]: ({0}→{0,14} ; {0,14}→{0,12,14}) ⇒ {0}→{0,12,14}
- [0,23,56]: ({0}→{0,15} ; {0,15}→{0,7,15}) ⇒ {0}→{0,7,15}
- [0,23,59]: ({0}→{0,15} ; {0,15}→{0,10,15}) ⇒ {0}→{0,10,15}
- [0,23,61]: ({0}→{0,15} ; {0,15}→{0,12,15}) ⇒ {0}→{0,12,15}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

# homotopy.io export: CATH domain 2d46A00 (mdCATH), heavy atoms (`mdcath-2d46a00-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 44 1-cells, 30 2-cells, 3 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U7
- U0 → U8
- U0 → U12
- U0 → U14
- U1 → U10
- U1 → U11
- U1 → U15
- U2 → U9
- U2 → U13
- U2 → U16
- U2 → U17
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,12]: (U0→U6 ; U6→U12) ⇒ U0→U12
- [0,6,14]: (U0→U6 ; U6→U14) ⇒ U0→U14
- [0,7,8]: (U0→U7 ; U7→U8) ⇒ U0→U8
- [0,7,14]: (U0→U7 ; U7→U14) ⇒ U0→U14
- [0,8,14]: (U0→U8 ; U8→U14) ⇒ U0→U14
- [0,12,14]: (U0→U12 ; U12→U14) ⇒ U0→U14
- [1,10,15]: (U1→U10 ; U10→U15) ⇒ U1→U15
- [1,11,15]: (U1→U11 ; U11→U15) ⇒ U1→U15
- [2,9,16]: (U2→U9 ; U9→U16) ⇒ U2→U16
- [2,13,16]: (U2→U13 ; U13→U16) ⇒ U2→U16
- [2,13,17]: (U2→U13 ; U13→U17) ⇒ U2→U17
- [3,6,10]: (U3→U6 ; U6→U10) ⇒ U3→U10
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,6,12,14]
- [0,7,8,14]
- [4,7,14,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 95 0-cells, 310 1-cells, 288 2-cells, 72 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,7}
- {0} → {0,8}
- {0} → {0,12}
- {0} → {0,14}
- {0} → {0,6,12}
- {0} → {0,6,14}
- {0} → {0,7,8}
- {0} → {0,7,14}
- {0} → {0,8,14}
- {0} → {0,12,14}
- {0} → {0,6,12,14}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,62]: ({0}→{0,6} ; {0,6}→{0,6,12}) ⇒ {0}→{0,6,12}
- [0,18,63]: ({0}→{0,6} ; {0,6}→{0,6,14}) ⇒ {0}→{0,6,14}
- [0,18,92]: ({0}→{0,6} ; {0,6}→{0,6,12,14}) ⇒ {0}→{0,6,12,14}
- [0,19,64]: ({0}→{0,7} ; {0,7}→{0,7,8}) ⇒ {0}→{0,7,8}
- [0,19,65]: ({0}→{0,7} ; {0,7}→{0,7,14}) ⇒ {0}→{0,7,14}
- [0,19,93]: ({0}→{0,7} ; {0,7}→{0,7,8,14}) ⇒ {0}→{0,7,8,14}
- [0,20,64]: ({0}→{0,8} ; {0,8}→{0,7,8}) ⇒ {0}→{0,7,8}
- [0,20,66]: ({0}→{0,8} ; {0,8}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,20,93]: ({0}→{0,8} ; {0,8}→{0,7,8,14}) ⇒ {0}→{0,7,8,14}
- [0,21,62]: ({0}→{0,12} ; {0,12}→{0,6,12}) ⇒ {0}→{0,6,12}
- [0,21,67]: ({0}→{0,12} ; {0,12}→{0,12,14}) ⇒ {0}→{0,12,14}
- [0,21,92]: ({0}→{0,12} ; {0,12}→{0,6,12,14}) ⇒ {0}→{0,6,12,14}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,62,92]
- [0,18,63,92]
- [0,19,64,93]
- [0,19,65,93]
- [0,20,64,93]
- [0,20,66,93]
- [0,21,62,92]
- [0,21,67,92]
- [0,22,63,92]
- [0,22,65,93]
- [0,22,66,93]
- [0,22,67,92]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

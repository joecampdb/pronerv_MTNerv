# homotopy.io export: CATH domain 2jrrA01 (mdCATH), heavy atoms (`mdcath-2jrra01-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 53 1-cells, 52 2-cells, 19 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U5
- U0 → U7
- U0 → U8
- U0 → U9
- U0 → U12
- U0 → U14
- U0 → U15
- U1 → U6
- U1 → U10
- U1 → U13
- U1 → U17
- U2 → U5
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,5,9]: (U0→U5 ; U5→U9) ⇒ U0→U9
- [0,5,12]: (U0→U5 ; U5→U12) ⇒ U0→U12
- [0,5,14]: (U0→U5 ; U5→U14) ⇒ U0→U14
- [0,7,8]: (U0→U7 ; U7→U8) ⇒ U0→U8
- [0,7,15]: (U0→U7 ; U7→U15) ⇒ U0→U15
- [0,8,9]: (U0→U8 ; U8→U9) ⇒ U0→U9
- [0,8,15]: (U0→U8 ; U8→U15) ⇒ U0→U15
- [0,9,12]: (U0→U9 ; U9→U12) ⇒ U0→U12
- [0,9,14]: (U0→U9 ; U9→U14) ⇒ U0→U14
- [0,9,15]: (U0→U9 ; U9→U15) ⇒ U0→U15
- [0,12,14]: (U0→U12 ; U12→U14) ⇒ U0→U14
- [0,12,15]: (U0→U12 ; U12→U15) ⇒ U0→U15
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,5,9,12]
- [0,5,9,14]
- [0,5,12,14]
- [0,7,8,15]
- [0,8,9,15]
- [0,9,12,14]
- [0,9,12,15]
- [1,6,10,17]
- [1,6,13,17]
- [3,6,10,17]
- [4,7,8,15]
- [4,7,8,16]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 142 0-cells, 684 1-cells, 996 2-cells, 456 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,5}
- {0} → {0,7}
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,12}
- {0} → {0,14}
- {0} → {0,15}
- {0} → {0,5,9}
- {0} → {0,5,12}
- {0} → {0,5,14}
- {0} → {0,7,8}
- {0} → {0,7,15}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,71]: ({0}→{0,5} ; {0,5}→{0,5,9}) ⇒ {0}→{0,5,9}
- [0,18,72]: ({0}→{0,5} ; {0,5}→{0,5,12}) ⇒ {0}→{0,5,12}
- [0,18,73]: ({0}→{0,5} ; {0,5}→{0,5,14}) ⇒ {0}→{0,5,14}
- [0,18,123]: ({0}→{0,5} ; {0,5}→{0,5,9,12}) ⇒ {0}→{0,5,9,12}
- [0,18,124]: ({0}→{0,5} ; {0,5}→{0,5,9,14}) ⇒ {0}→{0,5,9,14}
- [0,18,125]: ({0}→{0,5} ; {0,5}→{0,5,12,14}) ⇒ {0}→{0,5,12,14}
- [0,19,74]: ({0}→{0,7} ; {0,7}→{0,7,8}) ⇒ {0}→{0,7,8}
- [0,19,75]: ({0}→{0,7} ; {0,7}→{0,7,15}) ⇒ {0}→{0,7,15}
- [0,19,126]: ({0}→{0,7} ; {0,7}→{0,7,8,15}) ⇒ {0}→{0,7,8,15}
- [0,20,74]: ({0}→{0,8} ; {0,8}→{0,7,8}) ⇒ {0}→{0,7,8}
- [0,20,76]: ({0}→{0,8} ; {0,8}→{0,8,9}) ⇒ {0}→{0,8,9}
- [0,20,77]: ({0}→{0,8} ; {0,8}→{0,8,15}) ⇒ {0}→{0,8,15}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,71,123]
- [0,18,71,124]
- [0,18,72,123]
- [0,18,72,125]
- [0,18,73,124]
- [0,18,73,125]
- [0,19,74,126]
- [0,19,75,126]
- [0,20,74,126]
- [0,20,76,127]
- [0,20,77,126]
- [0,20,77,127]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

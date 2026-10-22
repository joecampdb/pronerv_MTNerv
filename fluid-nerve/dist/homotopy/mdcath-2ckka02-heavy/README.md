# homotopy.io export: CATH domain 2ckkA02 (mdCATH), heavy atoms (`mdcath-2ckka02-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 64 1-cells, 72 2-cells, 27 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U4
- U0 → U6
- U0 → U8
- U0 → U9
- U0 → U11
- U0 → U13
- U0 → U16
- U1 → U7
- U1 → U12
- U1 → U15
- U1 → U17
- U2 → U6
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,4,13]: (U0→U4 ; U4→U13) ⇒ U0→U13
- [0,4,16]: (U0→U4 ; U4→U16) ⇒ U0→U16
- [0,6,11]: (U0→U6 ; U6→U11) ⇒ U0→U11
- [0,6,16]: (U0→U6 ; U6→U16) ⇒ U0→U16
- [0,8,9]: (U0→U8 ; U8→U9) ⇒ U0→U9
- [0,8,13]: (U0→U8 ; U8→U13) ⇒ U0→U13
- [0,8,16]: (U0→U8 ; U8→U16) ⇒ U0→U16
- [0,9,13]: (U0→U9 ; U9→U13) ⇒ U0→U13
- [0,11,13]: (U0→U11 ; U11→U13) ⇒ U0→U13
- [0,11,16]: (U0→U11 ; U11→U16) ⇒ U0→U16
- [0,13,16]: (U0→U13 ; U13→U16) ⇒ U0→U16
- [1,7,12]: (U1→U7 ; U7→U12) ⇒ U1→U12
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,4,13,16]
- [0,6,11,16]
- [0,8,9,13]
- [0,8,13,16]
- [1,7,12,15]
- [1,7,12,17]
- [1,7,15,17]
- [1,12,15,17]
- [3,7,8,9]
- [3,7,8,15]
- [3,8,9,13]
- [4,5,10,14]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 181 0-cells, 938 1-cells, 1404 2-cells, 648 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,4}
- {0} → {0,6}
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,11}
- {0} → {0,13}
- {0} → {0,16}
- {0} → {0,4,13}
- {0} → {0,4,16}
- {0} → {0,6,11}
- {0} → {0,6,16}
- {0} → {0,8,9}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,82]: ({0}→{0,4} ; {0,4}→{0,4,13}) ⇒ {0}→{0,4,13}
- [0,18,83]: ({0}→{0,4} ; {0,4}→{0,4,16}) ⇒ {0}→{0,4,16}
- [0,18,154]: ({0}→{0,4} ; {0,4}→{0,4,13,16}) ⇒ {0}→{0,4,13,16}
- [0,19,84]: ({0}→{0,6} ; {0,6}→{0,6,11}) ⇒ {0}→{0,6,11}
- [0,19,85]: ({0}→{0,6} ; {0,6}→{0,6,16}) ⇒ {0}→{0,6,16}
- [0,19,155]: ({0}→{0,6} ; {0,6}→{0,6,11,16}) ⇒ {0}→{0,6,11,16}
- [0,20,86]: ({0}→{0,8} ; {0,8}→{0,8,9}) ⇒ {0}→{0,8,9}
- [0,20,87]: ({0}→{0,8} ; {0,8}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,20,88]: ({0}→{0,8} ; {0,8}→{0,8,16}) ⇒ {0}→{0,8,16}
- [0,20,156]: ({0}→{0,8} ; {0,8}→{0,8,9,13}) ⇒ {0}→{0,8,9,13}
- [0,20,157]: ({0}→{0,8} ; {0,8}→{0,8,13,16}) ⇒ {0}→{0,8,13,16}
- [0,21,86]: ({0}→{0,9} ; {0,9}→{0,8,9}) ⇒ {0}→{0,8,9}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,82,154]
- [0,18,83,154]
- [0,19,84,155]
- [0,19,85,155]
- [0,20,86,156]
- [0,20,87,156]
- [0,20,87,157]
- [0,20,88,157]
- [0,21,86,156]
- [0,21,89,156]
- [0,22,84,155]
- [0,22,91,155]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

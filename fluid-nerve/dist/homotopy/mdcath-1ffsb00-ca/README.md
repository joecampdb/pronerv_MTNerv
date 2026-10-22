# homotopy.io export: CATH domain 1ffsB00 (mdCATH), C-alpha (`mdcath-1ffsb00-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 54 1-cells, 67 2-cells, 37 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U9
- U0 → U11
- U0 → U12
- U0 → U13
- U0 → U14
- U0 → U15
- U1 → U6
- U1 → U16
- U1 → U17
- U2 → U5
- U3 → U4
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,9]: (U0→U7 ; U7→U9) ⇒ U0→U9
- [0,7,11]: (U0→U7 ; U7→U11) ⇒ U0→U11
- [0,7,13]: (U0→U7 ; U7→U13) ⇒ U0→U13
- [0,7,14]: (U0→U7 ; U7→U14) ⇒ U0→U14
- [0,7,15]: (U0→U7 ; U7→U15) ⇒ U0→U15
- [0,9,11]: (U0→U9 ; U9→U11) ⇒ U0→U11
- [0,9,13]: (U0→U9 ; U9→U13) ⇒ U0→U13
- [0,9,15]: (U0→U9 ; U9→U15) ⇒ U0→U15
- [0,11,12]: (U0→U11 ; U11→U12) ⇒ U0→U12
- [0,11,13]: (U0→U11 ; U11→U13) ⇒ U0→U13
- [0,11,15]: (U0→U11 ; U11→U15) ⇒ U0→U15
- [0,12,13]: (U0→U12 ; U12→U13) ⇒ U0→U13
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,7,9,11]
- [0,7,9,13]
- [0,7,9,15]
- [0,7,11,13]
- [0,7,11,15]
- [0,7,13,14]
- [0,7,13,15]
- [0,9,11,13]
- [0,9,11,15]
- [0,9,13,15]
- [0,11,12,13]
- [0,11,12,15]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 176 0-cells, 1028 1-cells, 1734 2-cells, 888 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,9}
- {0} → {0,11}
- {0} → {0,12}
- {0} → {0,13}
- {0} → {0,14}
- {0} → {0,15}
- {0} → {0,7,9}
- {0} → {0,7,11}
- {0} → {0,7,13}
- {0} → {0,7,14}
- {0} → {0,7,15}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,72]: ({0}→{0,7} ; {0,7}→{0,7,9}) ⇒ {0}→{0,7,9}
- [0,18,73]: ({0}→{0,7} ; {0,7}→{0,7,11}) ⇒ {0}→{0,7,11}
- [0,18,74]: ({0}→{0,7} ; {0,7}→{0,7,13}) ⇒ {0}→{0,7,13}
- [0,18,75]: ({0}→{0,7} ; {0,7}→{0,7,14}) ⇒ {0}→{0,7,14}
- [0,18,76]: ({0}→{0,7} ; {0,7}→{0,7,15}) ⇒ {0}→{0,7,15}
- [0,18,139]: ({0}→{0,7} ; {0,7}→{0,7,9,11}) ⇒ {0}→{0,7,9,11}
- [0,18,140]: ({0}→{0,7} ; {0,7}→{0,7,9,13}) ⇒ {0}→{0,7,9,13}
- [0,18,141]: ({0}→{0,7} ; {0,7}→{0,7,9,15}) ⇒ {0}→{0,7,9,15}
- [0,18,142]: ({0}→{0,7} ; {0,7}→{0,7,11,13}) ⇒ {0}→{0,7,11,13}
- [0,18,143]: ({0}→{0,7} ; {0,7}→{0,7,11,15}) ⇒ {0}→{0,7,11,15}
- [0,18,144]: ({0}→{0,7} ; {0,7}→{0,7,13,14}) ⇒ {0}→{0,7,13,14}
- [0,18,145]: ({0}→{0,7} ; {0,7}→{0,7,13,15}) ⇒ {0}→{0,7,13,15}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,72,139]
- [0,18,72,140]
- [0,18,72,141]
- [0,18,73,139]
- [0,18,73,142]
- [0,18,73,143]
- [0,18,74,140]
- [0,18,74,142]
- [0,18,74,144]
- [0,18,74,145]
- [0,18,75,144]
- [0,18,76,141]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

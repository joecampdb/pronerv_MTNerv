# homotopy.io export: CATH domain 1s6lA01 (mdCATH), C-alpha (`mdcath-1s6la01-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 46 1-cells, 36 2-cells, 7 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U5
- U0 → U6
- U0 → U7
- U0 → U12
- U0 → U14
- U0 → U17
- U1 → U8
- U1 → U9
- U1 → U13
- U2 → U10
- U2 → U11
- U2 → U15
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,5,12]: (U0→U5 ; U5→U12) ⇒ U0→U12
- [0,5,14]: (U0→U5 ; U5→U14) ⇒ U0→U14
- [0,6,7]: (U0→U6 ; U6→U7) ⇒ U0→U7
- [0,6,12]: (U0→U6 ; U6→U12) ⇒ U0→U12
- [0,6,14]: (U0→U6 ; U6→U14) ⇒ U0→U14
- [0,12,14]: (U0→U12 ; U12→U14) ⇒ U0→U14
- [0,14,17]: (U0→U14 ; U14→U17) ⇒ U0→U17
- [1,8,9]: (U1→U8 ; U8→U9) ⇒ U1→U9
- [1,9,13]: (U1→U9 ; U9→U13) ⇒ U1→U13
- [2,10,11]: (U2→U10 ; U10→U11) ⇒ U2→U11
- [2,10,15]: (U2→U10 ; U10→U15) ⇒ U2→U15
- [3,6,12]: (U3→U6 ; U6→U12) ⇒ U3→U12
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,5,12,14]
- [0,6,12,14]
- [3,6,12,16]
- [3,10,12,15]
- [4,6,9,16]
- [4,9,13,16]
- [5,10,11,12]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 107 0-cells, 406 1-cells, 468 2-cells, 168 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,5}
- {0} → {0,6}
- {0} → {0,7}
- {0} → {0,12}
- {0} → {0,14}
- {0} → {0,17}
- {0} → {0,5,12}
- {0} → {0,5,14}
- {0} → {0,6,7}
- {0} → {0,6,12}
- {0} → {0,6,14}
- {0} → {0,12,14}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,64]: ({0}→{0,5} ; {0,5}→{0,5,12}) ⇒ {0}→{0,5,12}
- [0,18,65]: ({0}→{0,5} ; {0,5}→{0,5,14}) ⇒ {0}→{0,5,14}
- [0,18,100]: ({0}→{0,5} ; {0,5}→{0,5,12,14}) ⇒ {0}→{0,5,12,14}
- [0,19,66]: ({0}→{0,6} ; {0,6}→{0,6,7}) ⇒ {0}→{0,6,7}
- [0,19,67]: ({0}→{0,6} ; {0,6}→{0,6,12}) ⇒ {0}→{0,6,12}
- [0,19,68]: ({0}→{0,6} ; {0,6}→{0,6,14}) ⇒ {0}→{0,6,14}
- [0,19,101]: ({0}→{0,6} ; {0,6}→{0,6,12,14}) ⇒ {0}→{0,6,12,14}
- [0,20,66]: ({0}→{0,7} ; {0,7}→{0,6,7}) ⇒ {0}→{0,6,7}
- [0,21,64]: ({0}→{0,12} ; {0,12}→{0,5,12}) ⇒ {0}→{0,5,12}
- [0,21,67]: ({0}→{0,12} ; {0,12}→{0,6,12}) ⇒ {0}→{0,6,12}
- [0,21,69]: ({0}→{0,12} ; {0,12}→{0,12,14}) ⇒ {0}→{0,12,14}
- [0,21,100]: ({0}→{0,12} ; {0,12}→{0,5,12,14}) ⇒ {0}→{0,5,12,14}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,64,100]
- [0,18,65,100]
- [0,19,67,101]
- [0,19,68,101]
- [0,21,64,100]
- [0,21,67,101]
- [0,21,69,100]
- [0,21,69,101]
- [0,22,65,100]
- [0,22,68,101]
- [0,22,69,100]
- [0,22,69,101]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

# homotopy.io export: DHA (MD22 ab initio MD) (`sgdml-md22-dha`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 43 1-cells, 27 2-cells, 4 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U9
- U0 → U12
- U0 → U14
- U0 → U16
- U1 → U8
- U1 → U10
- U1 → U13
- U2 → U7
- U2 → U11
- U2 → U15
- U2 → U17
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,14]: (U0→U6 ; U6→U14) ⇒ U0→U14
- [0,6,16]: (U0→U6 ; U6→U16) ⇒ U0→U16
- [0,9,12]: (U0→U9 ; U9→U12) ⇒ U0→U12
- [0,9,14]: (U0→U9 ; U9→U14) ⇒ U0→U14
- [0,12,14]: (U0→U12 ; U12→U14) ⇒ U0→U14
- [0,14,16]: (U0→U14 ; U14→U16) ⇒ U0→U16
- [1,10,13]: (U1→U10 ; U10→U13) ⇒ U1→U13
- [2,11,15]: (U2→U11 ; U11→U15) ⇒ U2→U15
- [3,8,10]: (U3→U8 ; U8→U10) ⇒ U3→U10
- [3,9,12]: (U3→U9 ; U9→U12) ⇒ U3→U12
- [3,10,12]: (U3→U10 ; U10→U12) ⇒ U3→U12
- [4,6,11]: (U4→U6 ; U6→U11) ⇒ U4→U11
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,6,14,16]
- [0,9,12,14]
- [4,6,11,14]
- [5,13,15,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 92 0-cells, 304 1-cells, 306 2-cells, 96 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,9}
- {0} → {0,12}
- {0} → {0,14}
- {0} → {0,16}
- {0} → {0,6,14}
- {0} → {0,6,16}
- {0} → {0,9,12}
- {0} → {0,9,14}
- {0} → {0,12,14}
- {0} → {0,14,16}
- {0} → {0,6,14,16}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,61]: ({0}→{0,6} ; {0,6}→{0,6,14}) ⇒ {0}→{0,6,14}
- [0,18,62]: ({0}→{0,6} ; {0,6}→{0,6,16}) ⇒ {0}→{0,6,16}
- [0,18,88]: ({0}→{0,6} ; {0,6}→{0,6,14,16}) ⇒ {0}→{0,6,14,16}
- [0,19,63]: ({0}→{0,9} ; {0,9}→{0,9,12}) ⇒ {0}→{0,9,12}
- [0,19,64]: ({0}→{0,9} ; {0,9}→{0,9,14}) ⇒ {0}→{0,9,14}
- [0,19,89]: ({0}→{0,9} ; {0,9}→{0,9,12,14}) ⇒ {0}→{0,9,12,14}
- [0,20,63]: ({0}→{0,12} ; {0,12}→{0,9,12}) ⇒ {0}→{0,9,12}
- [0,20,65]: ({0}→{0,12} ; {0,12}→{0,12,14}) ⇒ {0}→{0,12,14}
- [0,20,89]: ({0}→{0,12} ; {0,12}→{0,9,12,14}) ⇒ {0}→{0,9,12,14}
- [0,21,61]: ({0}→{0,14} ; {0,14}→{0,6,14}) ⇒ {0}→{0,6,14}
- [0,21,64]: ({0}→{0,14} ; {0,14}→{0,9,14}) ⇒ {0}→{0,9,14}
- [0,21,65]: ({0}→{0,14} ; {0,14}→{0,12,14}) ⇒ {0}→{0,12,14}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,61,88]
- [0,18,62,88]
- [0,19,63,89]
- [0,19,64,89]
- [0,20,63,89]
- [0,20,65,89]
- [0,21,61,88]
- [0,21,64,89]
- [0,21,65,89]
- [0,21,66,88]
- [0,22,62,88]
- [0,22,66,88]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

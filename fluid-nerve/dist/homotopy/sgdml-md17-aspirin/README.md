# homotopy.io export: aspirin (MD17 ab initio MD) (`sgdml-md17-aspirin`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 62 1-cells, 78 2-cells, 40 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U5
- U0 → U6
- U0 → U9
- U0 → U13
- U0 → U14
- U1 → U7
- U1 → U8
- U1 → U11
- U1 → U15
- U2 → U5
- U2 → U7
- U2 → U10
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,5,9]: (U0→U5 ; U5→U9) ⇒ U0→U9
- [0,5,13]: (U0→U5 ; U5→U13) ⇒ U0→U13
- [0,5,14]: (U0→U5 ; U5→U14) ⇒ U0→U14
- [0,6,9]: (U0→U6 ; U6→U9) ⇒ U0→U9
- [0,6,13]: (U0→U6 ; U6→U13) ⇒ U0→U13
- [0,6,14]: (U0→U6 ; U6→U14) ⇒ U0→U14
- [0,9,13]: (U0→U9 ; U9→U13) ⇒ U0→U13
- [0,9,14]: (U0→U9 ; U9→U14) ⇒ U0→U14
- [0,13,14]: (U0→U13 ; U13→U14) ⇒ U0→U14
- [1,7,11]: (U1→U7 ; U7→U11) ⇒ U1→U11
- [1,7,15]: (U1→U7 ; U7→U15) ⇒ U1→U15
- [1,8,11]: (U1→U8 ; U8→U11) ⇒ U1→U11
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,5,9,13]
- [0,5,9,14]
- [0,5,13,14]
- [0,6,9,13]
- [0,6,9,14]
- [0,6,13,14]
- [0,9,13,14]
- [1,7,11,15]
- [1,8,11,15]
- [2,5,10,17]
- [2,7,10,17]
- [3,4,8,12]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: skipped: 4218 generators exceed --max-generators 4000

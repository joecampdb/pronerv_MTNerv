# homotopy.io export: Ace-VAL-NMe dipeptide (OpenMM) (`dipeptide-val`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 75 1-cells, 130 2-cells, 112 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U5
- U0 → U6
- U0 → U8
- U0 → U9
- U0 → U11
- U0 → U13
- U0 → U14
- U0 → U16
- U0 → U17
- U1 → U4
- U1 → U7
- U1 → U10
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,5,6]: (U0→U5 ; U5→U6) ⇒ U0→U6
- [0,5,8]: (U0→U5 ; U5→U8) ⇒ U0→U8
- [0,5,11]: (U0→U5 ; U5→U11) ⇒ U0→U11
- [0,5,13]: (U0→U5 ; U5→U13) ⇒ U0→U13
- [0,5,14]: (U0→U5 ; U5→U14) ⇒ U0→U14
- [0,5,17]: (U0→U5 ; U5→U17) ⇒ U0→U17
- [0,6,11]: (U0→U6 ; U6→U11) ⇒ U0→U11
- [0,6,14]: (U0→U6 ; U6→U14) ⇒ U0→U14
- [0,6,16]: (U0→U6 ; U6→U16) ⇒ U0→U16
- [0,6,17]: (U0→U6 ; U6→U17) ⇒ U0→U17
- [0,8,9]: (U0→U8 ; U8→U9) ⇒ U0→U9
- [0,8,11]: (U0→U8 ; U8→U11) ⇒ U0→U11
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,5,6,11]
- [0,5,6,14]
- [0,5,6,17]
- [0,5,8,11]
- [0,5,8,13]
- [0,5,8,14]
- [0,5,8,17]
- [0,5,11,13]
- [0,5,11,14]
- [0,5,11,17]
- [0,5,13,14]
- [0,5,14,17]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: skipped: 10333 generators exceed --max-generators 4000

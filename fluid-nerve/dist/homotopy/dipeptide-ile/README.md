# homotopy.io export: Ace-ILE-NMe dipeptide (OpenMM) (`dipeptide-ile`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 84 1-cells, 247 2-cells, 503 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U2
- U0 → U3
- U0 → U4
- U0 → U6
- U0 → U7
- U0 → U9
- U0 → U10
- U0 → U11
- U0 → U12
- U0 → U14
- U0 → U15
- U0 → U17
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,2,3]: (U0→U2 ; U2→U3) ⇒ U0→U3
- [0,2,4]: (U0→U2 ; U2→U4) ⇒ U0→U4
- [0,2,7]: (U0→U2 ; U2→U7) ⇒ U0→U7
- [0,2,9]: (U0→U2 ; U2→U9) ⇒ U0→U9
- [0,2,10]: (U0→U2 ; U2→U10) ⇒ U0→U10
- [0,2,11]: (U0→U2 ; U2→U11) ⇒ U0→U11
- [0,2,14]: (U0→U2 ; U2→U14) ⇒ U0→U14
- [0,2,15]: (U0→U2 ; U2→U15) ⇒ U0→U15
- [0,3,4]: (U0→U3 ; U3→U4) ⇒ U0→U4
- [0,3,6]: (U0→U3 ; U3→U6) ⇒ U0→U6
- [0,3,7]: (U0→U3 ; U3→U7) ⇒ U0→U7
- [0,3,9]: (U0→U3 ; U3→U9) ⇒ U0→U9
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,2,3,4]
- [0,2,3,7]
- [0,2,3,9]
- [0,2,3,10]
- [0,2,3,11]
- [0,2,3,14]
- [0,2,3,15]
- [0,2,4,7]
- [0,2,4,9]
- [0,2,4,10]
- [0,2,4,11]
- [0,2,4,14]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: skipped: 41206 generators exceed --max-generators 4000

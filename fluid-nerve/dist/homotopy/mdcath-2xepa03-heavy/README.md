# homotopy.io export: CATH domain 2xepA03 (mdCATH), heavy atoms (`mdcath-2xepa03-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 41 1-cells, 25 2-cells, 4 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U9
- U0 → U10
- U0 → U11
- U0 → U12
- U0 → U14
- U0 → U15
- U1 → U7
- U1 → U8
- U2 → U6
- U2 → U13
- U3 → U6
- U3 → U11
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,9,10]: (U0→U9 ; U9→U10) ⇒ U0→U10
- [0,9,14]: (U0→U9 ; U9→U14) ⇒ U0→U14
- [0,10,12]: (U0→U10 ; U10→U12) ⇒ U0→U12
- [0,10,15]: (U0→U10 ; U10→U15) ⇒ U0→U15
- [0,11,12]: (U0→U11 ; U11→U12) ⇒ U0→U12
- [0,11,14]: (U0→U11 ; U11→U14) ⇒ U0→U14
- [0,12,15]: (U0→U12 ; U12→U15) ⇒ U0→U15
- [3,6,12]: (U3→U6 ; U6→U12) ⇒ U3→U12
- [3,11,12]: (U3→U11 ; U11→U12) ⇒ U3→U12
- [4,10,17]: (U4→U10 ; U10→U17) ⇒ U4→U17
- [5,6,12]: (U5→U6 ; U6→U12) ⇒ U5→U12
- [5,6,15]: (U5→U6 ; U6→U15) ⇒ U5→U15
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,10,12,15]
- [5,6,12,15]
- [5,10,15,16]
- [7,10,16,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 88 0-cells, 288 1-cells, 294 2-cells, 96 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,9}
- {0} → {0,10}
- {0} → {0,11}
- {0} → {0,12}
- {0} → {0,14}
- {0} → {0,15}
- {0} → {0,9,10}
- {0} → {0,9,14}
- {0} → {0,10,12}
- {0} → {0,10,15}
- {0} → {0,11,12}
- {0} → {0,11,14}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,59]: ({0}→{0,9} ; {0,9}→{0,9,10}) ⇒ {0}→{0,9,10}
- [0,18,60]: ({0}→{0,9} ; {0,9}→{0,9,14}) ⇒ {0}→{0,9,14}
- [0,19,59]: ({0}→{0,10} ; {0,10}→{0,9,10}) ⇒ {0}→{0,9,10}
- [0,19,61]: ({0}→{0,10} ; {0,10}→{0,10,12}) ⇒ {0}→{0,10,12}
- [0,19,62]: ({0}→{0,10} ; {0,10}→{0,10,15}) ⇒ {0}→{0,10,15}
- [0,19,84]: ({0}→{0,10} ; {0,10}→{0,10,12,15}) ⇒ {0}→{0,10,12,15}
- [0,20,63]: ({0}→{0,11} ; {0,11}→{0,11,12}) ⇒ {0}→{0,11,12}
- [0,20,64]: ({0}→{0,11} ; {0,11}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,21,61]: ({0}→{0,12} ; {0,12}→{0,10,12}) ⇒ {0}→{0,10,12}
- [0,21,63]: ({0}→{0,12} ; {0,12}→{0,11,12}) ⇒ {0}→{0,11,12}
- [0,21,65]: ({0}→{0,12} ; {0,12}→{0,12,15}) ⇒ {0}→{0,12,15}
- [0,21,84]: ({0}→{0,12} ; {0,12}→{0,10,12,15}) ⇒ {0}→{0,10,12,15}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,19,61,84]
- [0,19,62,84]
- [0,21,61,84]
- [0,21,65,84]
- [0,23,62,84]
- [0,23,65,84]
- [5,34,69,85]
- [5,34,70,85]
- [5,37,73,86]
- [5,37,74,86]
- [5,38,69,85]
- [5,38,75,85]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

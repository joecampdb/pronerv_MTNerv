# homotopy.io export: Alanine dipeptide (mdshare) (`ala2`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 37 1-cells, 23 2-cells, 4 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U10
- U0 → U11
- U0 → U16
- U1 → U12
- U2 → U7
- U2 → U8
- U2 → U9
- U2 → U13
- U2 → U14
- U2 → U15
- U4 → U7
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,16]: (U0→U7 ; U7→U16) ⇒ U0→U16
- [0,10,11]: (U0→U10 ; U10→U11) ⇒ U0→U11
- [0,10,16]: (U0→U10 ; U10→U16) ⇒ U0→U16
- [0,11,16]: (U0→U11 ; U11→U16) ⇒ U0→U16
- [2,7,15]: (U2→U7 ; U7→U15) ⇒ U2→U15
- [2,8,13]: (U2→U8 ; U8→U13) ⇒ U2→U13
- [2,9,14]: (U2→U9 ; U9→U14) ⇒ U2→U14
- [2,9,15]: (U2→U9 ; U9→U15) ⇒ U2→U15
- [2,13,14]: (U2→U13 ; U13→U14) ⇒ U2→U14
- [2,14,15]: (U2→U14 ; U14→U15) ⇒ U2→U15
- [4,7,15]: (U4→U7 ; U7→U15) ⇒ U4→U15
- [4,7,16]: (U4→U7 ; U7→U16) ⇒ U4→U16
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,10,11,16]
- [2,9,14,15]
- [4,7,15,16]
- [6,10,11,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 82 0-cells, 268 1-cells, 282 2-cells, 96 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,10}
- {0} → {0,11}
- {0} → {0,16}
- {0} → {0,7,16}
- {0} → {0,10,11}
- {0} → {0,10,16}
- {0} → {0,11,16}
- {0} → {0,10,11,16}
- {1} → {1,12}
- {2} → {2,7}
- {2} → {2,8}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,55]: ({0}→{0,7} ; {0,7}→{0,7,16}) ⇒ {0}→{0,7,16}
- [0,19,56]: ({0}→{0,10} ; {0,10}→{0,10,11}) ⇒ {0}→{0,10,11}
- [0,19,57]: ({0}→{0,10} ; {0,10}→{0,10,16}) ⇒ {0}→{0,10,16}
- [0,19,78]: ({0}→{0,10} ; {0,10}→{0,10,11,16}) ⇒ {0}→{0,10,11,16}
- [0,20,56]: ({0}→{0,11} ; {0,11}→{0,10,11}) ⇒ {0}→{0,10,11}
- [0,20,58]: ({0}→{0,11} ; {0,11}→{0,11,16}) ⇒ {0}→{0,11,16}
- [0,20,78]: ({0}→{0,11} ; {0,11}→{0,10,11,16}) ⇒ {0}→{0,10,11,16}
- [0,21,55]: ({0}→{0,16} ; {0,16}→{0,7,16}) ⇒ {0}→{0,7,16}
- [0,21,57]: ({0}→{0,16} ; {0,16}→{0,10,16}) ⇒ {0}→{0,10,16}
- [0,21,58]: ({0}→{0,16} ; {0,16}→{0,11,16}) ⇒ {0}→{0,11,16}
- [0,21,78]: ({0}→{0,16} ; {0,16}→{0,10,11,16}) ⇒ {0}→{0,10,11,16}
- [0,56,78]: ({0}→{0,10,11} ; {0,10,11}→{0,10,11,16}) ⇒ {0}→{0,10,11,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,19,56,78]
- [0,19,57,78]
- [0,20,56,78]
- [0,20,58,78]
- [0,21,57,78]
- [0,21,58,78]
- [2,25,61,79]
- [2,25,62,79]
- [2,27,61,79]
- [2,27,64,79]
- [2,28,62,79]
- [2,28,64,79]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

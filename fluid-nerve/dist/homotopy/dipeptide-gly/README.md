# homotopy.io export: Ace-GLY-NMe dipeptide (OpenMM) (`dipeptide-gly`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 38 1-cells, 25 2-cells, 4 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U7
- U0 → U10
- U0 → U15
- U1 → U4
- U1 → U8
- U1 → U12
- U1 → U16
- U2 → U4
- U2 → U5
- U2 → U7
- U2 → U9
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,7]: (U0→U6 ; U6→U7) ⇒ U0→U7
- [0,7,15]: (U0→U7 ; U7→U15) ⇒ U0→U15
- [0,10,15]: (U0→U10 ; U10→U15) ⇒ U0→U15
- [1,4,12]: (U1→U4 ; U4→U12) ⇒ U1→U12
- [1,8,16]: (U1→U8 ; U8→U16) ⇒ U1→U16
- [1,12,16]: (U1→U12 ; U12→U16) ⇒ U1→U16
- [2,4,9]: (U2→U4 ; U4→U9) ⇒ U2→U9
- [2,4,11]: (U2→U4 ; U4→U11) ⇒ U2→U11
- [2,5,9]: (U2→U5 ; U5→U9) ⇒ U2→U9
- [2,5,14]: (U2→U5 ; U5→U14) ⇒ U2→U14
- [2,7,14]: (U2→U7 ; U7→U14) ⇒ U2→U14
- [2,9,11]: (U2→U9 ; U9→U11) ⇒ U2→U11
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,4,9,11]
- [2,5,9,14]
- [3,6,13,17]
- [5,7,14,15]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 85 0-cells, 282 1-cells, 294 2-cells, 96 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,7}
- {0} → {0,10}
- {0} → {0,15}
- {0} → {0,6,7}
- {0} → {0,7,15}
- {0} → {0,10,15}
- {1} → {1,4}
- {1} → {1,8}
- {1} → {1,12}
- {1} → {1,16}
- {1} → {1,4,12}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,56]: ({0}→{0,6} ; {0,6}→{0,6,7}) ⇒ {0}→{0,6,7}
- [0,19,56]: ({0}→{0,7} ; {0,7}→{0,6,7}) ⇒ {0}→{0,6,7}
- [0,19,57]: ({0}→{0,7} ; {0,7}→{0,7,15}) ⇒ {0}→{0,7,15}
- [0,20,58]: ({0}→{0,10} ; {0,10}→{0,10,15}) ⇒ {0}→{0,10,15}
- [0,21,57]: ({0}→{0,15} ; {0,15}→{0,7,15}) ⇒ {0}→{0,7,15}
- [0,21,58]: ({0}→{0,15} ; {0,15}→{0,10,15}) ⇒ {0}→{0,10,15}
- [1,22,59]: ({1}→{1,4} ; {1,4}→{1,4,12}) ⇒ {1}→{1,4,12}
- [1,23,60]: ({1}→{1,8} ; {1,8}→{1,8,16}) ⇒ {1}→{1,8,16}
- [1,24,59]: ({1}→{1,12} ; {1,12}→{1,4,12}) ⇒ {1}→{1,4,12}
- [1,24,61]: ({1}→{1,12} ; {1,12}→{1,12,16}) ⇒ {1}→{1,12,16}
- [1,25,60]: ({1}→{1,16} ; {1,16}→{1,8,16}) ⇒ {1}→{1,8,16}
- [1,25,61]: ({1}→{1,16} ; {1,16}→{1,12,16}) ⇒ {1}→{1,12,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,26,62,81]
- [2,26,63,81]
- [2,27,64,82]
- [2,27,65,82]
- [2,29,62,81]
- [2,29,64,82]
- [2,29,67,81]
- [2,29,68,82]
- [2,30,63,81]
- [2,30,67,81]
- [2,31,65,82]
- [2,31,68,82]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

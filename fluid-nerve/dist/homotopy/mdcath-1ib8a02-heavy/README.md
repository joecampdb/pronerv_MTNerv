# homotopy.io export: CATH domain 1ib8A02 (mdCATH), heavy atoms (`mdcath-1ib8a02-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 43 1-cells, 35 2-cells, 10 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U9
- U0 → U12
- U1 → U7
- U1 → U10
- U1 → U13
- U1 → U15
- U1 → U16
- U2 → U8
- U2 → U11
- U3 → U6
- U3 → U7
- U3 → U9
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,9,12]: (U0→U9 ; U9→U12) ⇒ U0→U12
- [1,7,16]: (U1→U7 ; U7→U16) ⇒ U1→U16
- [1,10,13]: (U1→U10 ; U10→U13) ⇒ U1→U13
- [1,10,15]: (U1→U10 ; U10→U15) ⇒ U1→U15
- [1,10,16]: (U1→U10 ; U10→U16) ⇒ U1→U16
- [1,13,15]: (U1→U13 ; U13→U15) ⇒ U1→U15
- [1,13,16]: (U1→U13 ; U13→U16) ⇒ U1→U16
- [1,15,16]: (U1→U15 ; U15→U16) ⇒ U1→U16
- [2,8,11]: (U2→U8 ; U8→U11) ⇒ U2→U11
- [3,6,10]: (U3→U6 ; U6→U10) ⇒ U3→U10
- [3,6,12]: (U3→U6 ; U6→U12) ⇒ U3→U12
- [3,7,10]: (U3→U7 ; U7→U10) ⇒ U3→U10
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [1,10,13,15]
- [1,10,13,16]
- [1,10,15,16]
- [1,13,15,16]
- [3,7,10,14]
- [3,9,12,17]
- [3,10,14,16]
- [7,10,14,16]
- [10,13,15,16]
- [10,14,15,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 106 0-cells, 436 1-cells, 570 2-cells, 240 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,9}
- {0} → {0,12}
- {0} → {0,9,12}
- {1} → {1,7}
- {1} → {1,10}
- {1} → {1,13}
- {1} → {1,15}
- {1} → {1,16}
- {1} → {1,7,16}
- {1} → {1,10,13}
- {1} → {1,10,15}
- {1} → {1,10,16}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,61]: ({0}→{0,9} ; {0,9}→{0,9,12}) ⇒ {0}→{0,9,12}
- [0,19,61]: ({0}→{0,12} ; {0,12}→{0,9,12}) ⇒ {0}→{0,9,12}
- [1,20,62]: ({1}→{1,7} ; {1,7}→{1,7,16}) ⇒ {1}→{1,7,16}
- [1,21,63]: ({1}→{1,10} ; {1,10}→{1,10,13}) ⇒ {1}→{1,10,13}
- [1,21,64]: ({1}→{1,10} ; {1,10}→{1,10,15}) ⇒ {1}→{1,10,15}
- [1,21,65]: ({1}→{1,10} ; {1,10}→{1,10,16}) ⇒ {1}→{1,10,16}
- [1,21,96]: ({1}→{1,10} ; {1,10}→{1,10,13,15}) ⇒ {1}→{1,10,13,15}
- [1,21,97]: ({1}→{1,10} ; {1,10}→{1,10,13,16}) ⇒ {1}→{1,10,13,16}
- [1,21,98]: ({1}→{1,10} ; {1,10}→{1,10,15,16}) ⇒ {1}→{1,10,15,16}
- [1,22,63]: ({1}→{1,13} ; {1,13}→{1,10,13}) ⇒ {1}→{1,10,13}
- [1,22,66]: ({1}→{1,13} ; {1,13}→{1,13,15}) ⇒ {1}→{1,13,15}
- [1,22,67]: ({1}→{1,13} ; {1,13}→{1,13,16}) ⇒ {1}→{1,13,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [1,21,63,96]
- [1,21,63,97]
- [1,21,64,96]
- [1,21,64,98]
- [1,21,65,97]
- [1,21,65,98]
- [1,22,63,96]
- [1,22,63,97]
- [1,22,66,96]
- [1,22,66,99]
- [1,22,67,97]
- [1,22,67,99]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

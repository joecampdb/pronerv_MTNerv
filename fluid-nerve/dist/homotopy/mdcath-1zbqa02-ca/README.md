# homotopy.io export: CATH domain 1zbqA02 (mdCATH), C-alpha (`mdcath-1zbqa02-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 40 1-cells, 23 2-cells, 3 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U10
- U0 → U11
- U0 → U12
- U0 → U17
- U1 → U9
- U1 → U13
- U1 → U15
- U2 → U7
- U2 → U8
- U2 → U14
- U2 → U16
- U3 → U7
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,10,17]: (U0→U10 ; U10→U17) ⇒ U0→U17
- [0,11,12]: (U0→U11 ; U11→U12) ⇒ U0→U12
- [0,11,17]: (U0→U11 ; U11→U17) ⇒ U0→U17
- [1,9,13]: (U1→U9 ; U9→U13) ⇒ U1→U13
- [1,9,15]: (U1→U9 ; U9→U15) ⇒ U1→U15
- [1,13,15]: (U1→U13 ; U13→U15) ⇒ U1→U15
- [2,7,16]: (U2→U7 ; U7→U16) ⇒ U2→U16
- [2,8,16]: (U2→U8 ; U8→U16) ⇒ U2→U16
- [3,7,10]: (U3→U7 ; U7→U10) ⇒ U3→U10
- [3,7,16]: (U3→U7 ; U7→U16) ⇒ U3→U16
- [3,8,16]: (U3→U8 ; U8→U16) ⇒ U3→U16
- [3,10,16]: (U3→U10 ; U10→U16) ⇒ U3→U16
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [1,9,13,15]
- [3,7,10,16]
- [5,6,13,14]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 84 0-cells, 260 1-cells, 246 2-cells, 72 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,10}
- {0} → {0,11}
- {0} → {0,12}
- {0} → {0,17}
- {0} → {0,10,17}
- {0} → {0,11,12}
- {0} → {0,11,17}
- {1} → {1,9}
- {1} → {1,13}
- {1} → {1,15}
- {1} → {1,9,13}
- {1} → {1,9,15}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,58]: ({0}→{0,10} ; {0,10}→{0,10,17}) ⇒ {0}→{0,10,17}
- [0,19,59]: ({0}→{0,11} ; {0,11}→{0,11,12}) ⇒ {0}→{0,11,12}
- [0,19,60]: ({0}→{0,11} ; {0,11}→{0,11,17}) ⇒ {0}→{0,11,17}
- [0,20,59]: ({0}→{0,12} ; {0,12}→{0,11,12}) ⇒ {0}→{0,11,12}
- [0,21,58]: ({0}→{0,17} ; {0,17}→{0,10,17}) ⇒ {0}→{0,10,17}
- [0,21,60]: ({0}→{0,17} ; {0,17}→{0,11,17}) ⇒ {0}→{0,11,17}
- [1,22,61]: ({1}→{1,9} ; {1,9}→{1,9,13}) ⇒ {1}→{1,9,13}
- [1,22,62]: ({1}→{1,9} ; {1,9}→{1,9,15}) ⇒ {1}→{1,9,15}
- [1,22,81]: ({1}→{1,9} ; {1,9}→{1,9,13,15}) ⇒ {1}→{1,9,13,15}
- [1,23,61]: ({1}→{1,13} ; {1,13}→{1,9,13}) ⇒ {1}→{1,9,13}
- [1,23,63]: ({1}→{1,13} ; {1,13}→{1,13,15}) ⇒ {1}→{1,13,15}
- [1,23,81]: ({1}→{1,13} ; {1,13}→{1,9,13,15}) ⇒ {1}→{1,9,13,15}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [1,22,61,81]
- [1,22,62,81]
- [1,23,61,81]
- [1,23,63,81]
- [1,24,62,81]
- [1,24,63,81]
- [3,29,66,82]
- [3,29,67,82]
- [3,31,66,82]
- [3,31,69,82]
- [3,32,67,82]
- [3,32,69,82]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

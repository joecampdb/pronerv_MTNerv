# homotopy.io export: CATH domain 3g5cA02 (mdCATH), heavy atoms (`mdcath-3g5ca02-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 39 1-cells, 21 2-cells, 1 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U7
- U0 → U12
- U0 → U15
- U0 → U16
- U1 → U8
- U1 → U9
- U1 → U13
- U2 → U10
- U2 → U11
- U2 → U14
- U3 → U7
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,16]: (U0→U6 ; U6→U16) ⇒ U0→U16
- [0,7,12]: (U0→U7 ; U7→U12) ⇒ U0→U12
- [0,7,16]: (U0→U7 ; U7→U16) ⇒ U0→U16
- [0,12,15]: (U0→U12 ; U12→U15) ⇒ U0→U15
- [1,8,9]: (U1→U8 ; U8→U9) ⇒ U1→U9
- [1,9,13]: (U1→U9 ; U9→U13) ⇒ U1→U13
- [2,10,11]: (U2→U10 ; U10→U11) ⇒ U2→U11
- [2,10,14]: (U2→U10 ; U10→U14) ⇒ U2→U14
- [3,9,17]: (U3→U9 ; U9→U17) ⇒ U3→U17
- [4,7,12]: (U4→U7 ; U7→U12) ⇒ U4→U12
- [4,8,9]: (U4→U8 ; U8→U9) ⇒ U4→U9
- [4,8,11]: (U4→U8 ; U8→U11) ⇒ U4→U11
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [5,10,12,15]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 79 0-cells, 218 1-cells, 162 2-cells, 24 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,7}
- {0} → {0,12}
- {0} → {0,15}
- {0} → {0,16}
- {0} → {0,6,16}
- {0} → {0,7,12}
- {0} → {0,7,16}
- {0} → {0,12,15}
- {1} → {1,8}
- {1} → {1,9}
- {1} → {1,13}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,57]: ({0}→{0,6} ; {0,6}→{0,6,16}) ⇒ {0}→{0,6,16}
- [0,19,58]: ({0}→{0,7} ; {0,7}→{0,7,12}) ⇒ {0}→{0,7,12}
- [0,19,59]: ({0}→{0,7} ; {0,7}→{0,7,16}) ⇒ {0}→{0,7,16}
- [0,20,58]: ({0}→{0,12} ; {0,12}→{0,7,12}) ⇒ {0}→{0,7,12}
- [0,20,60]: ({0}→{0,12} ; {0,12}→{0,12,15}) ⇒ {0}→{0,12,15}
- [0,21,60]: ({0}→{0,15} ; {0,15}→{0,12,15}) ⇒ {0}→{0,12,15}
- [0,22,57]: ({0}→{0,16} ; {0,16}→{0,6,16}) ⇒ {0}→{0,6,16}
- [0,22,59]: ({0}→{0,16} ; {0,16}→{0,7,16}) ⇒ {0}→{0,7,16}
- [1,23,61]: ({1}→{1,8} ; {1,8}→{1,8,9}) ⇒ {1}→{1,8,9}
- [1,24,61]: ({1}→{1,9} ; {1,9}→{1,8,9}) ⇒ {1}→{1,8,9}
- [1,24,62]: ({1}→{1,9} ; {1,9}→{1,9,13}) ⇒ {1}→{1,9,13}
- [1,25,62]: ({1}→{1,13} ; {1,13}→{1,9,13}) ⇒ {1}→{1,9,13}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [5,38,71,78]
- [5,38,73,78]
- [5,39,71,78]
- [5,39,74,78]
- [5,41,73,78]
- [5,41,74,78]
- [10,38,71,78]
- [10,38,73,78]
- [10,52,71,78]
- [10,52,77,78]
- [10,54,73,78]
- [10,54,77,78]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

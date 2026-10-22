# homotopy.io export: CATH domain 1ib8A02 (mdCATH), C-alpha (`mdcath-1ib8a02-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 41 1-cells, 27 2-cells, 5 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U9
- U0 → U10
- U0 → U12
- U1 → U11
- U1 → U13
- U1 → U14
- U2 → U6
- U2 → U7
- U2 → U8
- U2 → U17
- U3 → U9
- U3 → U10
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,9,10]: (U0→U9 ; U9→U10) ⇒ U0→U10
- [0,9,12]: (U0→U9 ; U9→U12) ⇒ U0→U12
- [1,11,13]: (U1→U11 ; U11→U13) ⇒ U1→U13
- [1,11,14]: (U1→U11 ; U11→U14) ⇒ U1→U14
- [1,13,14]: (U1→U13 ; U13→U14) ⇒ U1→U14
- [2,6,7]: (U2→U6 ; U6→U7) ⇒ U2→U7
- [2,6,8]: (U2→U6 ; U6→U8) ⇒ U2→U8
- [2,6,17]: (U2→U6 ; U6→U17) ⇒ U2→U17
- [2,8,17]: (U2→U8 ; U8→U17) ⇒ U2→U17
- [3,9,10]: (U3→U9 ; U9→U10) ⇒ U3→U10
- [3,9,11]: (U3→U9 ; U9→U11) ⇒ U3→U11
- [3,11,14]: (U3→U11 ; U11→U14) ⇒ U3→U14
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [1,11,13,14]
- [2,6,8,17]
- [4,8,13,16]
- [4,11,13,14]
- [4,11,13,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 91 0-cells, 314 1-cells, 342 2-cells, 120 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,9}
- {0} → {0,10}
- {0} → {0,12}
- {0} → {0,9,10}
- {0} → {0,9,12}
- {1} → {1,11}
- {1} → {1,13}
- {1} → {1,14}
- {1} → {1,11,13}
- {1} → {1,11,14}
- {1} → {1,13,14}
- {1} → {1,11,13,14}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,59]: ({0}→{0,9} ; {0,9}→{0,9,10}) ⇒ {0}→{0,9,10}
- [0,18,60]: ({0}→{0,9} ; {0,9}→{0,9,12}) ⇒ {0}→{0,9,12}
- [0,19,59]: ({0}→{0,10} ; {0,10}→{0,9,10}) ⇒ {0}→{0,9,10}
- [0,20,60]: ({0}→{0,12} ; {0,12}→{0,9,12}) ⇒ {0}→{0,9,12}
- [1,21,61]: ({1}→{1,11} ; {1,11}→{1,11,13}) ⇒ {1}→{1,11,13}
- [1,21,62]: ({1}→{1,11} ; {1,11}→{1,11,14}) ⇒ {1}→{1,11,14}
- [1,21,86]: ({1}→{1,11} ; {1,11}→{1,11,13,14}) ⇒ {1}→{1,11,13,14}
- [1,22,61]: ({1}→{1,13} ; {1,13}→{1,11,13}) ⇒ {1}→{1,11,13}
- [1,22,63]: ({1}→{1,13} ; {1,13}→{1,13,14}) ⇒ {1}→{1,13,14}
- [1,22,86]: ({1}→{1,13} ; {1,13}→{1,11,13,14}) ⇒ {1}→{1,11,13,14}
- [1,23,62]: ({1}→{1,14} ; {1,14}→{1,11,14}) ⇒ {1}→{1,11,14}
- [1,23,63]: ({1}→{1,14} ; {1,14}→{1,13,14}) ⇒ {1}→{1,13,14}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [1,21,61,86]
- [1,21,62,86]
- [1,22,61,86]
- [1,22,63,86]
- [1,23,62,86]
- [1,23,63,86]
- [2,24,65,87]
- [2,24,66,87]
- [2,26,65,87]
- [2,26,67,87]
- [2,27,66,87]
- [2,27,67,87]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

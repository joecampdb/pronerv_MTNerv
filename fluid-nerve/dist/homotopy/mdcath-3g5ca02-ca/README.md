# homotopy.io export: CATH domain 3g5cA02 (mdCATH), C-alpha (`mdcath-3g5ca02-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 41 1-cells, 26 2-cells, 2 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U9
- U0 → U12
- U0 → U16
- U1 → U8
- U1 → U11
- U2 → U10
- U2 → U13
- U2 → U14
- U3 → U7
- U3 → U8
- U3 → U15
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,9]: (U0→U7 ; U7→U9) ⇒ U0→U9
- [0,7,16]: (U0→U7 ; U7→U16) ⇒ U0→U16
- [0,9,12]: (U0→U9 ; U9→U12) ⇒ U0→U12
- [1,8,11]: (U1→U8 ; U8→U11) ⇒ U1→U11
- [2,10,13]: (U2→U10 ; U10→U13) ⇒ U2→U13
- [2,13,14]: (U2→U13 ; U13→U14) ⇒ U2→U14
- [3,7,15]: (U3→U7 ; U7→U15) ⇒ U3→U15
- [3,7,17]: (U3→U7 ; U7→U17) ⇒ U3→U17
- [3,8,17]: (U3→U8 ; U8→U17) ⇒ U3→U17
- [3,15,17]: (U3→U15 ; U15→U17) ⇒ U3→U17
- [4,7,9]: (U4→U7 ; U7→U9) ⇒ U4→U9
- [4,7,17]: (U4→U7 ; U7→U17) ⇒ U4→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [3,7,15,17]
- [4,9,10,13]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 87 0-cells, 266 1-cells, 228 2-cells, 48 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,9}
- {0} → {0,12}
- {0} → {0,16}
- {0} → {0,7,9}
- {0} → {0,7,16}
- {0} → {0,9,12}
- {1} → {1,8}
- {1} → {1,11}
- {1} → {1,8,11}
- {2} → {2,10}
- {2} → {2,13}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,59]: ({0}→{0,7} ; {0,7}→{0,7,9}) ⇒ {0}→{0,7,9}
- [0,18,60]: ({0}→{0,7} ; {0,7}→{0,7,16}) ⇒ {0}→{0,7,16}
- [0,19,59]: ({0}→{0,9} ; {0,9}→{0,7,9}) ⇒ {0}→{0,7,9}
- [0,19,61]: ({0}→{0,9} ; {0,9}→{0,9,12}) ⇒ {0}→{0,9,12}
- [0,20,61]: ({0}→{0,12} ; {0,12}→{0,9,12}) ⇒ {0}→{0,9,12}
- [0,21,60]: ({0}→{0,16} ; {0,16}→{0,7,16}) ⇒ {0}→{0,7,16}
- [1,22,62]: ({1}→{1,8} ; {1,8}→{1,8,11}) ⇒ {1}→{1,8,11}
- [1,23,62]: ({1}→{1,11} ; {1,11}→{1,8,11}) ⇒ {1}→{1,8,11}
- [2,24,63]: ({2}→{2,10} ; {2,10}→{2,10,13}) ⇒ {2}→{2,10,13}
- [2,25,63]: ({2}→{2,13} ; {2,13}→{2,10,13}) ⇒ {2}→{2,10,13}
- [2,25,64]: ({2}→{2,13} ; {2,13}→{2,13,14}) ⇒ {2}→{2,13,14}
- [2,26,64]: ({2}→{2,14} ; {2,14}→{2,13,14}) ⇒ {2}→{2,13,14}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [3,27,65,85]
- [3,27,66,85]
- [3,29,65,85]
- [3,29,68,85]
- [3,30,66,85]
- [3,30,68,85]
- [4,33,73,86]
- [4,33,74,86]
- [4,34,73,86]
- [4,34,76,86]
- [4,36,74,86]
- [4,36,76,86]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

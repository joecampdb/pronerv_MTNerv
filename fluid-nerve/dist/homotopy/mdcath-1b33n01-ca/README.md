# homotopy.io export: CATH domain 1b33N01 (mdCATH), C-alpha (`mdcath-1b33n01-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 39 1-cells, 23 2-cells, 3 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U8
- U0 → U11
- U0 → U14
- U2 → U9
- U2 → U10
- U2 → U12
- U2 → U17
- U3 → U9
- U3 → U13
- U3 → U15
- U4 → U6
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,11]: (U0→U7 ; U7→U11) ⇒ U0→U11
- [0,8,11]: (U0→U8 ; U8→U11) ⇒ U0→U11
- [0,8,14]: (U0→U8 ; U8→U14) ⇒ U0→U14
- [0,11,14]: (U0→U11 ; U11→U14) ⇒ U0→U14
- [2,9,12]: (U2→U9 ; U9→U12) ⇒ U2→U12
- [2,9,17]: (U2→U9 ; U9→U17) ⇒ U2→U17
- [2,10,12]: (U2→U10 ; U10→U12) ⇒ U2→U12
- [2,12,17]: (U2→U12 ; U12→U17) ⇒ U2→U17
- [3,9,13]: (U3→U9 ; U9→U13) ⇒ U3→U13
- [3,9,15]: (U3→U9 ; U9→U15) ⇒ U3→U15
- [3,13,15]: (U3→U13 ; U13→U15) ⇒ U3→U15
- [4,8,16]: (U4→U8 ; U8→U16) ⇒ U4→U16
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,8,11,14]
- [2,9,12,17]
- [3,9,13,15]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 83 0-cells, 258 1-cells, 246 2-cells, 72 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,8}
- {0} → {0,11}
- {0} → {0,14}
- {0} → {0,7,11}
- {0} → {0,8,11}
- {0} → {0,8,14}
- {0} → {0,11,14}
- {0} → {0,8,11,14}
- {2} → {2,9}
- {2} → {2,10}
- {2} → {2,12}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,57]: ({0}→{0,7} ; {0,7}→{0,7,11}) ⇒ {0}→{0,7,11}
- [0,19,58]: ({0}→{0,8} ; {0,8}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,19,59]: ({0}→{0,8} ; {0,8}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,19,80]: ({0}→{0,8} ; {0,8}→{0,8,11,14}) ⇒ {0}→{0,8,11,14}
- [0,20,57]: ({0}→{0,11} ; {0,11}→{0,7,11}) ⇒ {0}→{0,7,11}
- [0,20,58]: ({0}→{0,11} ; {0,11}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,20,60]: ({0}→{0,11} ; {0,11}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,20,80]: ({0}→{0,11} ; {0,11}→{0,8,11,14}) ⇒ {0}→{0,8,11,14}
- [0,21,59]: ({0}→{0,14} ; {0,14}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,21,60]: ({0}→{0,14} ; {0,14}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,21,80]: ({0}→{0,14} ; {0,14}→{0,8,11,14}) ⇒ {0}→{0,8,11,14}
- [0,58,80]: ({0}→{0,8,11} ; {0,8,11}→{0,8,11,14}) ⇒ {0}→{0,8,11,14}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,19,58,80]
- [0,19,59,80]
- [0,20,58,80]
- [0,20,60,80]
- [0,21,59,80]
- [0,21,60,80]
- [2,22,61,81]
- [2,22,62,81]
- [2,24,61,81]
- [2,24,64,81]
- [2,25,62,81]
- [2,25,64,81]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

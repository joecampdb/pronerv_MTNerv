# homotopy.io export: CATH domain 1kliL00 (mdCATH), C-alpha (`mdcath-1klil00-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 39 1-cells, 23 2-cells, 2 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U9
- U0 → U11
- U0 → U13
- U0 → U14
- U0 → U16
- U1 → U8
- U1 → U10
- U1 → U15
- U1 → U17
- U2 → U11
- U2 → U12
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,13]: (U0→U7 ; U7→U13) ⇒ U0→U13
- [0,7,16]: (U0→U7 ; U7→U16) ⇒ U0→U16
- [0,9,14]: (U0→U9 ; U9→U14) ⇒ U0→U14
- [0,9,16]: (U0→U9 ; U9→U16) ⇒ U0→U16
- [0,11,13]: (U0→U11 ; U11→U13) ⇒ U0→U13
- [0,11,14]: (U0→U11 ; U11→U14) ⇒ U0→U14
- [1,8,15]: (U1→U8 ; U8→U15) ⇒ U1→U15
- [1,8,17]: (U1→U8 ; U8→U17) ⇒ U1→U17
- [1,10,15]: (U1→U10 ; U10→U15) ⇒ U1→U15
- [1,15,17]: (U1→U15 ; U15→U17) ⇒ U1→U17
- [2,11,12]: (U2→U11 ; U11→U12) ⇒ U2→U12
- [4,7,16]: (U4→U7 ; U7→U16) ⇒ U4→U16
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [1,8,15,17]
- [5,8,14,15]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 82 0-cells, 244 1-cells, 210 2-cells, 48 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,9}
- {0} → {0,11}
- {0} → {0,13}
- {0} → {0,14}
- {0} → {0,16}
- {0} → {0,7,13}
- {0} → {0,7,16}
- {0} → {0,9,14}
- {0} → {0,9,16}
- {0} → {0,11,13}
- {0} → {0,11,14}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,57]: ({0}→{0,7} ; {0,7}→{0,7,13}) ⇒ {0}→{0,7,13}
- [0,18,58]: ({0}→{0,7} ; {0,7}→{0,7,16}) ⇒ {0}→{0,7,16}
- [0,19,59]: ({0}→{0,9} ; {0,9}→{0,9,14}) ⇒ {0}→{0,9,14}
- [0,19,60]: ({0}→{0,9} ; {0,9}→{0,9,16}) ⇒ {0}→{0,9,16}
- [0,20,61]: ({0}→{0,11} ; {0,11}→{0,11,13}) ⇒ {0}→{0,11,13}
- [0,20,62]: ({0}→{0,11} ; {0,11}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,21,57]: ({0}→{0,13} ; {0,13}→{0,7,13}) ⇒ {0}→{0,7,13}
- [0,21,61]: ({0}→{0,13} ; {0,13}→{0,11,13}) ⇒ {0}→{0,11,13}
- [0,22,59]: ({0}→{0,14} ; {0,14}→{0,9,14}) ⇒ {0}→{0,9,14}
- [0,22,62]: ({0}→{0,14} ; {0,14}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,23,58]: ({0}→{0,16} ; {0,16}→{0,7,16}) ⇒ {0}→{0,7,16}
- [0,23,60]: ({0}→{0,16} ; {0,16}→{0,9,16}) ⇒ {0}→{0,9,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [1,24,63,80]
- [1,24,64,80]
- [1,26,63,80]
- [1,26,66,80]
- [1,27,64,80]
- [1,27,66,80]
- [5,35,70,81]
- [5,35,71,81]
- [5,39,70,81]
- [5,39,76,81]
- [5,40,71,81]
- [5,40,76,81]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

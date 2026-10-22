# homotopy.io export: AT-AT (MD22 ab initio MD) (`sgdml-md22-at-at`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 47 1-cells, 53 2-cells, 31 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U5
- U0 → U9
- U0 → U11
- U0 → U14
- U1 → U6
- U1 → U12
- U1 → U16
- U2 → U7
- U2 → U10
- U2 → U13
- U3 → U5
- U3 → U6
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,5,11]: (U0→U5 ; U5→U11) ⇒ U0→U11
- [0,5,14]: (U0→U5 ; U5→U14) ⇒ U0→U14
- [0,9,14]: (U0→U9 ; U9→U14) ⇒ U0→U14
- [0,11,14]: (U0→U11 ; U11→U14) ⇒ U0→U14
- [1,6,12]: (U1→U6 ; U6→U12) ⇒ U1→U12
- [1,6,16]: (U1→U6 ; U6→U16) ⇒ U1→U16
- [1,12,16]: (U1→U12 ; U12→U16) ⇒ U1→U16
- [2,7,10]: (U2→U7 ; U7→U10) ⇒ U2→U10
- [2,7,13]: (U2→U7 ; U7→U13) ⇒ U2→U13
- [2,10,13]: (U2→U10 ; U10→U13) ⇒ U2→U13
- [3,5,8]: (U3→U5 ; U5→U8) ⇒ U3→U8
- [3,5,11]: (U3→U5 ; U5→U11) ⇒ U3→U11
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,5,11,14]
- [1,6,12,16]
- [2,7,10,13]
- [3,5,8,11]
- [3,5,8,15]
- [3,5,8,17]
- [3,5,11,15]
- [3,5,11,17]
- [3,5,15,17]
- [3,6,8,12]
- [3,6,8,15]
- [3,6,8,17]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 149 0-cells, 846 1-cells, 1434 2-cells, 744 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,5}
- {0} → {0,9}
- {0} → {0,11}
- {0} → {0,14}
- {0} → {0,5,11}
- {0} → {0,5,14}
- {0} → {0,9,14}
- {0} → {0,11,14}
- {0} → {0,5,11,14}
- {1} → {1,6}
- {1} → {1,12}
- {1} → {1,16}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,65]: ({0}→{0,5} ; {0,5}→{0,5,11}) ⇒ {0}→{0,5,11}
- [0,18,66]: ({0}→{0,5} ; {0,5}→{0,5,14}) ⇒ {0}→{0,5,14}
- [0,18,118]: ({0}→{0,5} ; {0,5}→{0,5,11,14}) ⇒ {0}→{0,5,11,14}
- [0,19,67]: ({0}→{0,9} ; {0,9}→{0,9,14}) ⇒ {0}→{0,9,14}
- [0,20,65]: ({0}→{0,11} ; {0,11}→{0,5,11}) ⇒ {0}→{0,5,11}
- [0,20,68]: ({0}→{0,11} ; {0,11}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,20,118]: ({0}→{0,11} ; {0,11}→{0,5,11,14}) ⇒ {0}→{0,5,11,14}
- [0,21,66]: ({0}→{0,14} ; {0,14}→{0,5,14}) ⇒ {0}→{0,5,14}
- [0,21,67]: ({0}→{0,14} ; {0,14}→{0,9,14}) ⇒ {0}→{0,9,14}
- [0,21,68]: ({0}→{0,14} ; {0,14}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,21,118]: ({0}→{0,14} ; {0,14}→{0,5,11,14}) ⇒ {0}→{0,5,11,14}
- [0,65,118]: ({0}→{0,5,11} ; {0,5,11}→{0,5,11,14}) ⇒ {0}→{0,5,11,14}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,65,118]
- [0,18,66,118]
- [0,20,65,118]
- [0,20,68,118]
- [0,21,66,118]
- [0,21,68,118]
- [1,22,69,119]
- [1,22,70,119]
- [1,23,69,119]
- [1,23,71,119]
- [1,24,70,119]
- [1,24,71,119]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

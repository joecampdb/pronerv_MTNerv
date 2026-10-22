# homotopy.io export: Ace-GLY-NMe dipeptide (OpenMM) (`dipeptide-gly`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 42 1-cells, 27 2-cells, 6 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U9
- U0 → U10
- U0 → U15
- U1 → U6
- U1 → U8
- U1 → U13
- U1 → U16
- U2 → U5
- U2 → U7
- U2 → U11
- U2 → U12
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,15]: (U0→U7 ; U7→U15) ⇒ U0→U15
- [0,10,15]: (U0→U10 ; U10→U15) ⇒ U0→U15
- [1,6,13]: (U1→U6 ; U6→U13) ⇒ U1→U13
- [1,13,16]: (U1→U13 ; U13→U16) ⇒ U1→U16
- [2,5,11]: (U2→U5 ; U5→U11) ⇒ U2→U11
- [2,5,12]: (U2→U5 ; U5→U12) ⇒ U2→U12
- [2,7,14]: (U2→U7 ; U7→U14) ⇒ U2→U14
- [2,7,17]: (U2→U7 ; U7→U17) ⇒ U2→U17
- [2,11,12]: (U2→U11 ; U11→U12) ⇒ U2→U12
- [2,11,14]: (U2→U11 ; U11→U14) ⇒ U2→U14
- [2,11,17]: (U2→U11 ; U11→U17) ⇒ U2→U17
- [2,12,17]: (U2→U12 ; U12→U17) ⇒ U2→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,5,11,12]
- [2,7,14,17]
- [2,11,14,17]
- [4,7,14,15]
- [4,11,14,15]
- [7,14,15,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 93 0-cells, 330 1-cells, 378 2-cells, 144 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,9}
- {0} → {0,10}
- {0} → {0,15}
- {0} → {0,7,15}
- {0} → {0,10,15}
- {1} → {1,6}
- {1} → {1,8}
- {1} → {1,13}
- {1} → {1,16}
- {1} → {1,6,13}
- {1} → {1,13,16}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,60]: ({0}→{0,7} ; {0,7}→{0,7,15}) ⇒ {0}→{0,7,15}
- [0,20,61]: ({0}→{0,10} ; {0,10}→{0,10,15}) ⇒ {0}→{0,10,15}
- [0,21,60]: ({0}→{0,15} ; {0,15}→{0,7,15}) ⇒ {0}→{0,7,15}
- [0,21,61]: ({0}→{0,15} ; {0,15}→{0,10,15}) ⇒ {0}→{0,10,15}
- [1,22,62]: ({1}→{1,6} ; {1,6}→{1,6,13}) ⇒ {1}→{1,6,13}
- [1,24,62]: ({1}→{1,13} ; {1,13}→{1,6,13}) ⇒ {1}→{1,6,13}
- [1,24,63]: ({1}→{1,13} ; {1,13}→{1,13,16}) ⇒ {1}→{1,13,16}
- [1,25,63]: ({1}→{1,16} ; {1,16}→{1,13,16}) ⇒ {1}→{1,13,16}
- [2,26,64]: ({2}→{2,5} ; {2,5}→{2,5,11}) ⇒ {2}→{2,5,11}
- [2,26,65]: ({2}→{2,5} ; {2,5}→{2,5,12}) ⇒ {2}→{2,5,12}
- [2,26,87]: ({2}→{2,5} ; {2,5}→{2,5,11,12}) ⇒ {2}→{2,5,11,12}
- [2,27,66]: ({2}→{2,7} ; {2,7}→{2,7,14}) ⇒ {2}→{2,7,14}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,26,64,87]
- [2,26,65,87]
- [2,27,66,88]
- [2,27,67,88]
- [2,28,64,87]
- [2,28,68,87]
- [2,28,69,89]
- [2,28,70,89]
- [2,29,65,87]
- [2,29,68,87]
- [2,30,66,88]
- [2,30,69,89]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

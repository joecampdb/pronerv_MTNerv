# homotopy.io export: Ace-GLY-NMe dipeptide (OpenMM) (`dipeptide-gly`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 41 1-cells, 27 2-cells, 4 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U8
- U0 → U10
- U0 → U14
- U1 → U7
- U1 → U12
- U1 → U16
- U2 → U5
- U2 → U6
- U2 → U11
- U2 → U13
- U2 → U15
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,14]: (U0→U6 ; U6→U14) ⇒ U0→U14
- [0,8,14]: (U0→U8 ; U8→U14) ⇒ U0→U14
- [0,10,14]: (U0→U10 ; U10→U14) ⇒ U0→U14
- [1,7,12]: (U1→U7 ; U7→U12) ⇒ U1→U12
- [1,12,16]: (U1→U12 ; U12→U16) ⇒ U1→U16
- [2,5,11]: (U2→U5 ; U5→U11) ⇒ U2→U11
- [2,5,13]: (U2→U5 ; U5→U13) ⇒ U2→U13
- [2,6,15]: (U2→U6 ; U6→U15) ⇒ U2→U15
- [2,11,13]: (U2→U11 ; U11→U13) ⇒ U2→U13
- [2,11,15]: (U2→U11 ; U11→U15) ⇒ U2→U15
- [2,13,17]: (U2→U13 ; U13→U17) ⇒ U2→U17
- [2,15,17]: (U2→U15 ; U15→U17) ⇒ U2→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,5,11,13]
- [4,6,14,15]
- [4,10,14,15]
- [4,11,14,15]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 90 0-cells, 300 1-cells, 306 2-cells, 96 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,8}
- {0} → {0,10}
- {0} → {0,14}
- {0} → {0,6,14}
- {0} → {0,8,14}
- {0} → {0,10,14}
- {1} → {1,7}
- {1} → {1,12}
- {1} → {1,16}
- {1} → {1,7,12}
- {1} → {1,12,16}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,59]: ({0}→{0,6} ; {0,6}→{0,6,14}) ⇒ {0}→{0,6,14}
- [0,19,60]: ({0}→{0,8} ; {0,8}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,20,61]: ({0}→{0,10} ; {0,10}→{0,10,14}) ⇒ {0}→{0,10,14}
- [0,21,59]: ({0}→{0,14} ; {0,14}→{0,6,14}) ⇒ {0}→{0,6,14}
- [0,21,60]: ({0}→{0,14} ; {0,14}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,21,61]: ({0}→{0,14} ; {0,14}→{0,10,14}) ⇒ {0}→{0,10,14}
- [1,22,62]: ({1}→{1,7} ; {1,7}→{1,7,12}) ⇒ {1}→{1,7,12}
- [1,23,62]: ({1}→{1,12} ; {1,12}→{1,7,12}) ⇒ {1}→{1,7,12}
- [1,23,63]: ({1}→{1,12} ; {1,12}→{1,12,16}) ⇒ {1}→{1,12,16}
- [1,24,63]: ({1}→{1,16} ; {1,16}→{1,12,16}) ⇒ {1}→{1,12,16}
- [2,25,64]: ({2}→{2,5} ; {2,5}→{2,5,11}) ⇒ {2}→{2,5,11}
- [2,25,65]: ({2}→{2,5} ; {2,5}→{2,5,13}) ⇒ {2}→{2,5,13}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,25,64,86]
- [2,25,65,86]
- [2,27,64,86]
- [2,27,67,86]
- [2,28,65,86]
- [2,28,67,86]
- [4,33,72,87]
- [4,33,73,87]
- [4,34,74,88]
- [4,34,75,88]
- [4,35,76,89]
- [4,35,77,89]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

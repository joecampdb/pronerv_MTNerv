# homotopy.io export: CATH domain 4a0tA01 (mdCATH), C-alpha (`mdcath-4a0ta01-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 38 1-cells, 19 2-cells, 1 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U9
- U0 → U12
- U0 → U14
- U0 → U15
- U1 → U10
- U1 → U11
- U2 → U6
- U2 → U9
- U2 → U16
- U2 → U17
- U3 → U7
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,14]: (U0→U8 ; U8→U14) ⇒ U0→U14
- [0,9,15]: (U0→U9 ; U9→U15) ⇒ U0→U15
- [0,12,14]: (U0→U12 ; U12→U14) ⇒ U0→U14
- [1,10,11]: (U1→U10 ; U10→U11) ⇒ U1→U11
- [2,6,9]: (U2→U6 ; U6→U9) ⇒ U2→U9
- [2,6,16]: (U2→U6 ; U6→U16) ⇒ U2→U16
- [2,9,16]: (U2→U9 ; U9→U16) ⇒ U2→U16
- [2,9,17]: (U2→U9 ; U9→U17) ⇒ U2→U17
- [2,16,17]: (U2→U16 ; U16→U17) ⇒ U2→U17
- [3,7,10]: (U3→U7 ; U7→U10) ⇒ U3→U10
- [3,8,13]: (U3→U8 ; U8→U13) ⇒ U3→U13
- [4,12,14]: (U4→U12 ; U12→U14) ⇒ U4→U14
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,6,9,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 76 0-cells, 204 1-cells, 150 2-cells, 24 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,12}
- {0} → {0,14}
- {0} → {0,15}
- {0} → {0,8,14}
- {0} → {0,9,15}
- {0} → {0,12,14}
- {1} → {1,10}
- {1} → {1,11}
- {1} → {1,10,11}
- {2} → {2,6}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,56]: ({0}→{0,8} ; {0,8}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,19,57]: ({0}→{0,9} ; {0,9}→{0,9,15}) ⇒ {0}→{0,9,15}
- [0,20,58]: ({0}→{0,12} ; {0,12}→{0,12,14}) ⇒ {0}→{0,12,14}
- [0,21,56]: ({0}→{0,14} ; {0,14}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,21,58]: ({0}→{0,14} ; {0,14}→{0,12,14}) ⇒ {0}→{0,12,14}
- [0,22,57]: ({0}→{0,15} ; {0,15}→{0,9,15}) ⇒ {0}→{0,9,15}
- [1,23,59]: ({1}→{1,10} ; {1,10}→{1,10,11}) ⇒ {1}→{1,10,11}
- [1,24,59]: ({1}→{1,11} ; {1,11}→{1,10,11}) ⇒ {1}→{1,10,11}
- [2,25,60]: ({2}→{2,6} ; {2,6}→{2,6,9}) ⇒ {2}→{2,6,9}
- [2,25,61]: ({2}→{2,6} ; {2,6}→{2,6,16}) ⇒ {2}→{2,6,16}
- [2,25,75]: ({2}→{2,6} ; {2,6}→{2,6,9,16}) ⇒ {2}→{2,6,9,16}
- [2,26,60]: ({2}→{2,9} ; {2,9}→{2,6,9}) ⇒ {2}→{2,6,9}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,25,60,75]
- [2,25,61,75]
- [2,26,60,75]
- [2,26,62,75]
- [2,27,61,75]
- [2,27,62,75]
- [6,25,60,75]
- [6,25,61,75]
- [6,41,60,75]
- [6,41,73,75]
- [6,43,61,75]
- [6,43,73,75]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

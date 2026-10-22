# homotopy.io export: CATH domain 4dczA00 (mdCATH), C-alpha (`mdcath-4dcza00-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 40 1-cells, 23 2-cells, 1 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U10
- U0 → U11
- U0 → U15
- U1 → U7
- U1 → U9
- U1 → U13
- U1 → U16
- U2 → U12
- U2 → U14
- U2 → U17
- U3 → U7
- U3 → U8
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,10,15]: (U0→U10 ; U10→U15) ⇒ U0→U15
- [0,11,15]: (U0→U11 ; U11→U15) ⇒ U0→U15
- [1,7,16]: (U1→U7 ; U7→U16) ⇒ U1→U16
- [1,9,13]: (U1→U9 ; U9→U13) ⇒ U1→U13
- [1,13,16]: (U1→U13 ; U13→U16) ⇒ U1→U16
- [2,12,14]: (U2→U12 ; U12→U14) ⇒ U2→U14
- [2,14,17]: (U2→U14 ; U14→U17) ⇒ U2→U17
- [3,8,10]: (U3→U8 ; U8→U10) ⇒ U3→U10
- [4,6,11]: (U4→U6 ; U6→U11) ⇒ U4→U11
- [4,6,14]: (U4→U6 ; U6→U14) ⇒ U4→U14
- [4,8,13]: (U4→U8 ; U8→U13) ⇒ U4→U13
- [4,8,15]: (U4→U8 ; U8→U15) ⇒ U4→U15
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [4,6,11,14]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 82 0-cells, 232 1-cells, 174 2-cells, 24 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,10}
- {0} → {0,11}
- {0} → {0,15}
- {0} → {0,10,15}
- {0} → {0,11,15}
- {1} → {1,7}
- {1} → {1,9}
- {1} → {1,13}
- {1} → {1,16}
- {1} → {1,7,16}
- {1} → {1,9,13}
- {1} → {1,13,16}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,58]: ({0}→{0,10} ; {0,10}→{0,10,15}) ⇒ {0}→{0,10,15}
- [0,19,59]: ({0}→{0,11} ; {0,11}→{0,11,15}) ⇒ {0}→{0,11,15}
- [0,20,58]: ({0}→{0,15} ; {0,15}→{0,10,15}) ⇒ {0}→{0,10,15}
- [0,20,59]: ({0}→{0,15} ; {0,15}→{0,11,15}) ⇒ {0}→{0,11,15}
- [1,21,60]: ({1}→{1,7} ; {1,7}→{1,7,16}) ⇒ {1}→{1,7,16}
- [1,22,61]: ({1}→{1,9} ; {1,9}→{1,9,13}) ⇒ {1}→{1,9,13}
- [1,23,61]: ({1}→{1,13} ; {1,13}→{1,9,13}) ⇒ {1}→{1,9,13}
- [1,23,62]: ({1}→{1,13} ; {1,13}→{1,13,16}) ⇒ {1}→{1,13,16}
- [1,24,60]: ({1}→{1,16} ; {1,16}→{1,7,16}) ⇒ {1}→{1,7,16}
- [1,24,62]: ({1}→{1,16} ; {1,16}→{1,13,16}) ⇒ {1}→{1,13,16}
- [2,25,63]: ({2}→{2,12} ; {2,12}→{2,12,14}) ⇒ {2}→{2,12,14}
- [2,26,63]: ({2}→{2,14} ; {2,14}→{2,12,14}) ⇒ {2}→{2,12,14}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [4,31,66,81]
- [4,31,67,81]
- [4,34,66,81]
- [4,34,72,81]
- [4,37,67,81]
- [4,37,72,81]
- [6,31,66,81]
- [6,31,67,81]
- [6,40,66,81]
- [6,40,75,81]
- [6,41,67,81]
- [6,41,75,81]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

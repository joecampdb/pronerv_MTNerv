# homotopy.io export: CATH domain 4dczA00 (mdCATH), heavy atoms (`mdcath-4dcza00-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 40 1-cells, 26 2-cells, 3 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U12
- U0 → U13
- U0 → U14
- U1 → U9
- U1 → U11
- U1 → U15
- U2 → U10
- U2 → U16
- U3 → U8
- U3 → U9
- U3 → U11
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,12]: (U0→U8 ; U8→U12) ⇒ U0→U12
- [0,8,13]: (U0→U8 ; U8→U13) ⇒ U0→U13
- [0,12,14]: (U0→U12 ; U12→U14) ⇒ U0→U14
- [1,9,11]: (U1→U9 ; U9→U11) ⇒ U1→U11
- [1,11,15]: (U1→U11 ; U11→U15) ⇒ U1→U15
- [2,10,16]: (U2→U10 ; U10→U16) ⇒ U2→U16
- [3,8,11]: (U3→U8 ; U8→U11) ⇒ U3→U11
- [3,8,13]: (U3→U8 ; U8→U13) ⇒ U3→U13
- [3,8,17]: (U3→U8 ; U8→U17) ⇒ U3→U17
- [3,9,11]: (U3→U9 ; U9→U11) ⇒ U3→U11
- [3,9,17]: (U3→U9 ; U9→U17) ⇒ U3→U17
- [3,11,17]: (U3→U11 ; U11→U17) ⇒ U3→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [3,8,11,17]
- [3,8,13,17]
- [3,9,11,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 87 0-cells, 278 1-cells, 264 2-cells, 72 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,12}
- {0} → {0,13}
- {0} → {0,14}
- {0} → {0,8,12}
- {0} → {0,8,13}
- {0} → {0,12,14}
- {1} → {1,9}
- {1} → {1,11}
- {1} → {1,15}
- {1} → {1,9,11}
- {1} → {1,11,15}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,58]: ({0}→{0,8} ; {0,8}→{0,8,12}) ⇒ {0}→{0,8,12}
- [0,18,59]: ({0}→{0,8} ; {0,8}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,19,58]: ({0}→{0,12} ; {0,12}→{0,8,12}) ⇒ {0}→{0,8,12}
- [0,19,60]: ({0}→{0,12} ; {0,12}→{0,12,14}) ⇒ {0}→{0,12,14}
- [0,20,59]: ({0}→{0,13} ; {0,13}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,21,60]: ({0}→{0,14} ; {0,14}→{0,12,14}) ⇒ {0}→{0,12,14}
- [1,22,61]: ({1}→{1,9} ; {1,9}→{1,9,11}) ⇒ {1}→{1,9,11}
- [1,23,61]: ({1}→{1,11} ; {1,11}→{1,9,11}) ⇒ {1}→{1,9,11}
- [1,23,62]: ({1}→{1,11} ; {1,11}→{1,11,15}) ⇒ {1}→{1,11,15}
- [1,24,62]: ({1}→{1,15} ; {1,15}→{1,11,15}) ⇒ {1}→{1,11,15}
- [2,25,63]: ({2}→{2,10} ; {2,10}→{2,10,16}) ⇒ {2}→{2,10,16}
- [2,26,63]: ({2}→{2,16} ; {2,16}→{2,10,16}) ⇒ {2}→{2,10,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [3,27,64,84]
- [3,27,65,85]
- [3,27,66,84]
- [3,27,66,85]
- [3,28,67,86]
- [3,28,68,86]
- [3,29,64,84]
- [3,29,67,86]
- [3,29,69,84]
- [3,29,69,86]
- [3,30,65,85]
- [3,30,70,85]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

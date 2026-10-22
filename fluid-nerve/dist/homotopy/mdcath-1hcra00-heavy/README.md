# homotopy.io export: CATH domain 1hcrA00 (mdCATH), heavy atoms (`mdcath-1hcra00-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 38 1-cells, 19 2-cells, 2 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U13
- U0 → U14
- U0 → U16
- U1 → U7
- U1 → U12
- U1 → U17
- U2 → U10
- U2 → U11
- U2 → U15
- U3 → U7
- U3 → U8
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,13]: (U0→U8 ; U8→U13) ⇒ U0→U13
- [0,8,16]: (U0→U8 ; U8→U16) ⇒ U0→U16
- [0,13,14]: (U0→U13 ; U13→U14) ⇒ U0→U14
- [0,13,16]: (U0→U13 ; U13→U16) ⇒ U0→U16
- [1,7,12]: (U1→U7 ; U7→U12) ⇒ U1→U12
- [1,7,17]: (U1→U7 ; U7→U17) ⇒ U1→U17
- [1,12,17]: (U1→U12 ; U12→U17) ⇒ U1→U17
- [2,10,15]: (U2→U10 ; U10→U15) ⇒ U2→U15
- [2,11,15]: (U2→U11 ; U11→U15) ⇒ U2→U15
- [3,7,17]: (U3→U7 ; U7→U17) ⇒ U3→U17
- [3,8,16]: (U3→U8 ; U8→U16) ⇒ U3→U16
- [3,9,17]: (U3→U9 ; U9→U17) ⇒ U3→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,8,13,16]
- [1,7,12,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 77 0-cells, 218 1-cells, 186 2-cells, 48 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,13}
- {0} → {0,14}
- {0} → {0,16}
- {0} → {0,8,13}
- {0} → {0,8,16}
- {0} → {0,13,14}
- {0} → {0,13,16}
- {0} → {0,8,13,16}
- {1} → {1,7}
- {1} → {1,12}
- {1} → {1,17}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,56]: ({0}→{0,8} ; {0,8}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,18,57]: ({0}→{0,8} ; {0,8}→{0,8,16}) ⇒ {0}→{0,8,16}
- [0,18,75]: ({0}→{0,8} ; {0,8}→{0,8,13,16}) ⇒ {0}→{0,8,13,16}
- [0,19,56]: ({0}→{0,13} ; {0,13}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,19,58]: ({0}→{0,13} ; {0,13}→{0,13,14}) ⇒ {0}→{0,13,14}
- [0,19,59]: ({0}→{0,13} ; {0,13}→{0,13,16}) ⇒ {0}→{0,13,16}
- [0,19,75]: ({0}→{0,13} ; {0,13}→{0,8,13,16}) ⇒ {0}→{0,8,13,16}
- [0,20,58]: ({0}→{0,14} ; {0,14}→{0,13,14}) ⇒ {0}→{0,13,14}
- [0,21,57]: ({0}→{0,16} ; {0,16}→{0,8,16}) ⇒ {0}→{0,8,16}
- [0,21,59]: ({0}→{0,16} ; {0,16}→{0,13,16}) ⇒ {0}→{0,13,16}
- [0,21,75]: ({0}→{0,16} ; {0,16}→{0,8,13,16}) ⇒ {0}→{0,8,13,16}
- [0,56,75]: ({0}→{0,8,13} ; {0,8,13}→{0,8,13,16}) ⇒ {0}→{0,8,13,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,56,75]
- [0,18,57,75]
- [0,19,56,75]
- [0,19,59,75]
- [0,21,57,75]
- [0,21,59,75]
- [1,22,60,76]
- [1,22,61,76]
- [1,23,60,76]
- [1,23,62,76]
- [1,24,61,76]
- [1,24,62,76]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

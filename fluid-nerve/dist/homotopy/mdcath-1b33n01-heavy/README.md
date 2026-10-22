# homotopy.io export: CATH domain 1b33N01 (mdCATH), heavy atoms (`mdcath-1b33n01-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 36 1-cells, 14 2-cells, 1 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U12
- U0 → U14
- U0 → U15
- U1 → U5
- U1 → U16
- U2 → U8
- U2 → U9
- U2 → U10
- U3 → U5
- U3 → U7
- U3 → U11
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,12]: (U0→U6 ; U6→U12) ⇒ U0→U12
- [0,6,14]: (U0→U6 ; U6→U14) ⇒ U0→U14
- [0,12,14]: (U0→U12 ; U12→U14) ⇒ U0→U14
- [1,5,16]: (U1→U5 ; U5→U16) ⇒ U1→U16
- [3,7,14]: (U3→U7 ; U7→U14) ⇒ U3→U14
- [3,13,14]: (U3→U13 ; U13→U14) ⇒ U3→U14
- [3,13,17]: (U3→U13 ; U13→U17) ⇒ U3→U17
- [4,6,12]: (U4→U6 ; U6→U12) ⇒ U4→U12
- [5,11,16]: (U5→U11 ; U11→U16) ⇒ U5→U16
- [6,10,13]: (U6→U10 ; U10→U13) ⇒ U6→U13
- [6,12,14]: (U6→U12 ; U12→U14) ⇒ U6→U14
- [6,13,14]: (U6→U13 ; U13→U14) ⇒ U6→U14
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,6,12,14]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 69 0-cells, 170 1-cells, 120 2-cells, 24 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,12}
- {0} → {0,14}
- {0} → {0,15}
- {0} → {0,6,12}
- {0} → {0,6,14}
- {0} → {0,12,14}
- {0} → {0,6,12,14}
- {1} → {1,5}
- {1} → {1,16}
- {1} → {1,5,16}
- {2} → {2,8}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,54]: ({0}→{0,6} ; {0,6}→{0,6,12}) ⇒ {0}→{0,6,12}
- [0,18,55]: ({0}→{0,6} ; {0,6}→{0,6,14}) ⇒ {0}→{0,6,14}
- [0,18,68]: ({0}→{0,6} ; {0,6}→{0,6,12,14}) ⇒ {0}→{0,6,12,14}
- [0,19,54]: ({0}→{0,12} ; {0,12}→{0,6,12}) ⇒ {0}→{0,6,12}
- [0,19,56]: ({0}→{0,12} ; {0,12}→{0,12,14}) ⇒ {0}→{0,12,14}
- [0,19,68]: ({0}→{0,12} ; {0,12}→{0,6,12,14}) ⇒ {0}→{0,6,12,14}
- [0,20,55]: ({0}→{0,14} ; {0,14}→{0,6,14}) ⇒ {0}→{0,6,14}
- [0,20,56]: ({0}→{0,14} ; {0,14}→{0,12,14}) ⇒ {0}→{0,12,14}
- [0,20,68]: ({0}→{0,14} ; {0,14}→{0,6,12,14}) ⇒ {0}→{0,6,12,14}
- [0,54,68]: ({0}→{0,6,12} ; {0,6,12}→{0,6,12,14}) ⇒ {0}→{0,6,12,14}
- [0,55,68]: ({0}→{0,6,14} ; {0,6,14}→{0,6,12,14}) ⇒ {0}→{0,6,12,14}
- [0,56,68]: ({0}→{0,12,14} ; {0,12,14}→{0,6,12,14}) ⇒ {0}→{0,6,12,14}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,54,68]
- [0,18,55,68]
- [0,19,54,68]
- [0,19,56,68]
- [0,20,55,68]
- [0,20,56,68]
- [6,18,54,68]
- [6,18,55,68]
- [6,40,54,68]
- [6,40,64,68]
- [6,42,55,68]
- [6,42,64,68]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

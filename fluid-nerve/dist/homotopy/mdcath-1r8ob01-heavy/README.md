# homotopy.io export: CATH domain 1r8oB01 (mdCATH), heavy atoms (`mdcath-1r8ob01-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 42 1-cells, 25 2-cells, 1 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U8
- U0 → U9
- U0 → U12
- U0 → U13
- U0 → U14
- U1 → U6
- U1 → U10
- U1 → U11
- U1 → U16
- U2 → U5
- U2 → U10
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,12]: (U0→U7 ; U7→U12) ⇒ U0→U12
- [0,8,13]: (U0→U8 ; U8→U13) ⇒ U0→U13
- [0,9,13]: (U0→U9 ; U9→U13) ⇒ U0→U13
- [0,9,14]: (U0→U9 ; U9→U14) ⇒ U0→U14
- [0,12,14]: (U0→U12 ; U12→U14) ⇒ U0→U14
- [1,6,16]: (U1→U6 ; U6→U16) ⇒ U1→U16
- [1,10,16]: (U1→U10 ; U10→U16) ⇒ U1→U16
- [1,11,16]: (U1→U11 ; U11→U16) ⇒ U1→U16
- [2,5,15]: (U2→U5 ; U5→U15) ⇒ U2→U15
- [2,10,15]: (U2→U10 ; U10→U15) ⇒ U2→U15
- [3,6,17]: (U3→U6 ; U6→U17) ⇒ U3→U17
- [3,7,17]: (U3→U7 ; U7→U17) ⇒ U3→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [4,6,12,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 86 0-cells, 248 1-cells, 186 2-cells, 24 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,12}
- {0} → {0,13}
- {0} → {0,14}
- {0} → {0,7,12}
- {0} → {0,8,13}
- {0} → {0,9,13}
- {0} → {0,9,14}
- {0} → {0,12,14}
- {1} → {1,6}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,60]: ({0}→{0,7} ; {0,7}→{0,7,12}) ⇒ {0}→{0,7,12}
- [0,19,61]: ({0}→{0,8} ; {0,8}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,20,62]: ({0}→{0,9} ; {0,9}→{0,9,13}) ⇒ {0}→{0,9,13}
- [0,20,63]: ({0}→{0,9} ; {0,9}→{0,9,14}) ⇒ {0}→{0,9,14}
- [0,21,60]: ({0}→{0,12} ; {0,12}→{0,7,12}) ⇒ {0}→{0,7,12}
- [0,21,64]: ({0}→{0,12} ; {0,12}→{0,12,14}) ⇒ {0}→{0,12,14}
- [0,22,61]: ({0}→{0,13} ; {0,13}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,22,62]: ({0}→{0,13} ; {0,13}→{0,9,13}) ⇒ {0}→{0,9,13}
- [0,23,63]: ({0}→{0,14} ; {0,14}→{0,9,14}) ⇒ {0}→{0,9,14}
- [0,23,64]: ({0}→{0,14} ; {0,14}→{0,12,14}) ⇒ {0}→{0,12,14}
- [1,24,65]: ({1}→{1,6} ; {1,6}→{1,6,16}) ⇒ {1}→{1,6,16}
- [1,25,66]: ({1}→{1,10} ; {1,10}→{1,10,16}) ⇒ {1}→{1,10,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [4,34,72,85]
- [4,34,73,85]
- [4,36,72,85]
- [4,36,77,85]
- [4,39,73,85]
- [4,39,77,85]
- [6,34,72,85]
- [6,34,73,85]
- [6,44,72,85]
- [6,44,82,85]
- [6,45,73,85]
- [6,45,82,85]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

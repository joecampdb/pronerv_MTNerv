# homotopy.io export: CATH domain 2d46A00 (mdCATH), C-alpha (`mdcath-2d46a00-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 43 1-cells, 29 2-cells, 3 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U12
- U0 → U14
- U0 → U16
- U1 → U7
- U1 → U9
- U1 → U13
- U2 → U6
- U2 → U10
- U2 → U11
- U2 → U15
- U3 → U7
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,14]: (U0→U8 ; U8→U14) ⇒ U0→U14
- [0,8,16]: (U0→U8 ; U8→U16) ⇒ U0→U16
- [0,12,14]: (U0→U12 ; U12→U14) ⇒ U0→U14
- [0,14,16]: (U0→U14 ; U14→U16) ⇒ U0→U16
- [1,7,9]: (U1→U7 ; U7→U9) ⇒ U1→U9
- [1,9,13]: (U1→U9 ; U9→U13) ⇒ U1→U13
- [2,6,15]: (U2→U6 ; U6→U15) ⇒ U2→U15
- [2,10,11]: (U2→U10 ; U10→U11) ⇒ U2→U11
- [2,11,15]: (U2→U11 ; U11→U15) ⇒ U2→U15
- [3,7,17]: (U3→U7 ; U7→U17) ⇒ U3→U17
- [3,8,17]: (U3→U8 ; U8→U17) ⇒ U3→U17
- [3,9,17]: (U3→U9 ; U9→U17) ⇒ U3→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,8,14,16]
- [4,11,12,14]
- [5,6,13,15]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 93 0-cells, 302 1-cells, 282 2-cells, 72 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,12}
- {0} → {0,14}
- {0} → {0,16}
- {0} → {0,8,14}
- {0} → {0,8,16}
- {0} → {0,12,14}
- {0} → {0,14,16}
- {0} → {0,8,14,16}
- {1} → {1,7}
- {1} → {1,9}
- {1} → {1,13}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,61]: ({0}→{0,8} ; {0,8}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,18,62]: ({0}→{0,8} ; {0,8}→{0,8,16}) ⇒ {0}→{0,8,16}
- [0,18,90]: ({0}→{0,8} ; {0,8}→{0,8,14,16}) ⇒ {0}→{0,8,14,16}
- [0,19,63]: ({0}→{0,12} ; {0,12}→{0,12,14}) ⇒ {0}→{0,12,14}
- [0,20,61]: ({0}→{0,14} ; {0,14}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,20,63]: ({0}→{0,14} ; {0,14}→{0,12,14}) ⇒ {0}→{0,12,14}
- [0,20,64]: ({0}→{0,14} ; {0,14}→{0,14,16}) ⇒ {0}→{0,14,16}
- [0,20,90]: ({0}→{0,14} ; {0,14}→{0,8,14,16}) ⇒ {0}→{0,8,14,16}
- [0,21,62]: ({0}→{0,16} ; {0,16}→{0,8,16}) ⇒ {0}→{0,8,16}
- [0,21,64]: ({0}→{0,16} ; {0,16}→{0,14,16}) ⇒ {0}→{0,14,16}
- [0,21,90]: ({0}→{0,16} ; {0,16}→{0,8,14,16}) ⇒ {0}→{0,8,14,16}
- [0,61,90]: ({0}→{0,8,14} ; {0,8,14}→{0,8,14,16}) ⇒ {0}→{0,8,14,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,61,90]
- [0,18,62,90]
- [0,20,61,90]
- [0,20,64,90]
- [0,21,62,90]
- [0,21,64,90]
- [4,34,74,91]
- [4,34,75,91]
- [4,35,74,91]
- [4,35,76,91]
- [4,36,75,91]
- [4,36,76,91]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

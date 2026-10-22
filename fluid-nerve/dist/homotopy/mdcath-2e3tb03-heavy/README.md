# homotopy.io export: CATH domain 2e3tB03 (mdCATH), heavy atoms (`mdcath-2e3tb03-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 56 1-cells, 69 2-cells, 38 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U11
- U0 → U14
- U1 → U7
- U1 → U10
- U2 → U6
- U2 → U9
- U2 → U15
- U2 → U16
- U3 → U6
- U3 → U7
- U3 → U8
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,11]: (U0→U8 ; U8→U11) ⇒ U0→U11
- [0,8,14]: (U0→U8 ; U8→U14) ⇒ U0→U14
- [0,11,14]: (U0→U11 ; U11→U14) ⇒ U0→U14
- [1,7,10]: (U1→U7 ; U7→U10) ⇒ U1→U10
- [2,6,9]: (U2→U6 ; U6→U9) ⇒ U2→U9
- [2,6,15]: (U2→U6 ; U6→U15) ⇒ U2→U15
- [2,6,16]: (U2→U6 ; U6→U16) ⇒ U2→U16
- [2,9,15]: (U2→U9 ; U9→U15) ⇒ U2→U15
- [2,9,16]: (U2→U9 ; U9→U16) ⇒ U2→U16
- [2,15,16]: (U2→U15 ; U15→U16) ⇒ U2→U16
- [3,6,12]: (U3→U6 ; U6→U12) ⇒ U3→U12
- [3,6,17]: (U3→U6 ; U6→U17) ⇒ U3→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,8,11,14]
- [2,6,9,15]
- [2,6,9,16]
- [2,6,15,16]
- [2,9,15,16]
- [3,6,12,17]
- [3,8,12,13]
- [3,8,12,17]
- [3,8,13,17]
- [3,12,13,17]
- [4,8,9,12]
- [4,8,9,16]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 181 0-cells, 1058 1-cells, 1782 2-cells, 912 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,11}
- {0} → {0,14}
- {0} → {0,8,11}
- {0} → {0,8,14}
- {0} → {0,11,14}
- {0} → {0,8,11,14}
- {1} → {1,7}
- {1} → {1,10}
- {1} → {1,7,10}
- {2} → {2,6}
- {2} → {2,9}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,74]: ({0}→{0,8} ; {0,8}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,18,75]: ({0}→{0,8} ; {0,8}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,18,143]: ({0}→{0,8} ; {0,8}→{0,8,11,14}) ⇒ {0}→{0,8,11,14}
- [0,19,74]: ({0}→{0,11} ; {0,11}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,19,76]: ({0}→{0,11} ; {0,11}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,19,143]: ({0}→{0,11} ; {0,11}→{0,8,11,14}) ⇒ {0}→{0,8,11,14}
- [0,20,75]: ({0}→{0,14} ; {0,14}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,20,76]: ({0}→{0,14} ; {0,14}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,20,143]: ({0}→{0,14} ; {0,14}→{0,8,11,14}) ⇒ {0}→{0,8,11,14}
- [0,74,143]: ({0}→{0,8,11} ; {0,8,11}→{0,8,11,14}) ⇒ {0}→{0,8,11,14}
- [0,75,143]: ({0}→{0,8,14} ; {0,8,14}→{0,8,11,14}) ⇒ {0}→{0,8,11,14}
- [0,76,143]: ({0}→{0,11,14} ; {0,11,14}→{0,8,11,14}) ⇒ {0}→{0,8,11,14}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,74,143]
- [0,18,75,143]
- [0,19,74,143]
- [0,19,76,143]
- [0,20,75,143]
- [0,20,76,143]
- [2,23,78,144]
- [2,23,78,145]
- [2,23,79,144]
- [2,23,79,146]
- [2,23,80,145]
- [2,23,80,146]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

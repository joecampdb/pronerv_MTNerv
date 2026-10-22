# homotopy.io export: CATH domain 2e3tB03 (mdCATH), C-alpha (`mdcath-2e3tb03-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 51 1-cells, 47 2-cells, 13 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U4
- U0 → U6
- U0 → U11
- U0 → U14
- U0 → U15
- U1 → U5
- U1 → U9
- U2 → U7
- U2 → U10
- U2 → U16
- U3 → U5
- U3 → U6
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,4,11]: (U0→U4 ; U4→U11) ⇒ U0→U11
- [0,4,14]: (U0→U4 ; U4→U14) ⇒ U0→U14
- [0,6,14]: (U0→U6 ; U6→U14) ⇒ U0→U14
- [0,6,15]: (U0→U6 ; U6→U15) ⇒ U0→U15
- [0,11,14]: (U0→U11 ; U11→U14) ⇒ U0→U14
- [0,11,15]: (U0→U11 ; U11→U15) ⇒ U0→U15
- [0,14,15]: (U0→U14 ; U14→U15) ⇒ U0→U15
- [1,5,9]: (U1→U5 ; U5→U9) ⇒ U1→U9
- [2,7,10]: (U2→U7 ; U7→U10) ⇒ U2→U10
- [2,10,16]: (U2→U10 ; U10→U16) ⇒ U2→U16
- [3,5,13]: (U3→U5 ; U5→U13) ⇒ U3→U13
- [3,6,13]: (U3→U6 ; U6→U13) ⇒ U3→U13
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,4,11,14]
- [0,6,14,15]
- [0,11,14,15]
- [3,6,13,17]
- [4,6,14,17]
- [4,7,10,12]
- [4,8,10,11]
- [4,8,10,16]
- [4,8,11,14]
- [4,12,14,17]
- [6,11,14,15]
- [6,13,14,17]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 129 0-cells, 566 1-cells, 750 2-cells, 312 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,4}
- {0} → {0,6}
- {0} → {0,11}
- {0} → {0,14}
- {0} → {0,15}
- {0} → {0,4,11}
- {0} → {0,4,14}
- {0} → {0,6,14}
- {0} → {0,6,15}
- {0} → {0,11,14}
- {0} → {0,11,15}
- {0} → {0,14,15}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,69]: ({0}→{0,4} ; {0,4}→{0,4,11}) ⇒ {0}→{0,4,11}
- [0,18,70]: ({0}→{0,4} ; {0,4}→{0,4,14}) ⇒ {0}→{0,4,14}
- [0,18,116]: ({0}→{0,4} ; {0,4}→{0,4,11,14}) ⇒ {0}→{0,4,11,14}
- [0,19,71]: ({0}→{0,6} ; {0,6}→{0,6,14}) ⇒ {0}→{0,6,14}
- [0,19,72]: ({0}→{0,6} ; {0,6}→{0,6,15}) ⇒ {0}→{0,6,15}
- [0,19,117]: ({0}→{0,6} ; {0,6}→{0,6,14,15}) ⇒ {0}→{0,6,14,15}
- [0,20,69]: ({0}→{0,11} ; {0,11}→{0,4,11}) ⇒ {0}→{0,4,11}
- [0,20,73]: ({0}→{0,11} ; {0,11}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,20,74]: ({0}→{0,11} ; {0,11}→{0,11,15}) ⇒ {0}→{0,11,15}
- [0,20,116]: ({0}→{0,11} ; {0,11}→{0,4,11,14}) ⇒ {0}→{0,4,11,14}
- [0,20,118]: ({0}→{0,11} ; {0,11}→{0,11,14,15}) ⇒ {0}→{0,11,14,15}
- [0,21,70]: ({0}→{0,14} ; {0,14}→{0,4,14}) ⇒ {0}→{0,4,14}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,69,116]
- [0,18,70,116]
- [0,19,71,117]
- [0,19,72,117]
- [0,20,69,116]
- [0,20,73,116]
- [0,20,73,118]
- [0,20,74,118]
- [0,21,70,116]
- [0,21,71,117]
- [0,21,73,116]
- [0,21,73,118]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

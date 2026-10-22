# homotopy.io export: CATH domain 1i5xA00 (mdCATH), C-alpha (`mdcath-1i5xa00-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 48 1-cells, 40 2-cells, 9 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U10
- U0 → U12
- U0 → U13
- U0 → U15
- U1 → U6
- U1 → U11
- U1 → U14
- U2 → U7
- U2 → U8
- U2 → U9
- U2 → U17
- U3 → U7
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,10,12]: (U0→U10 ; U10→U12) ⇒ U0→U12
- [0,10,15]: (U0→U10 ; U10→U15) ⇒ U0→U15
- [0,12,13]: (U0→U12 ; U12→U13) ⇒ U0→U13
- [1,6,14]: (U1→U6 ; U6→U14) ⇒ U1→U14
- [1,11,14]: (U1→U11 ; U11→U14) ⇒ U1→U14
- [2,7,8]: (U2→U7 ; U7→U8) ⇒ U2→U8
- [2,7,17]: (U2→U7 ; U7→U17) ⇒ U2→U17
- [2,8,9]: (U2→U8 ; U8→U9) ⇒ U2→U9
- [2,8,17]: (U2→U8 ; U8→U17) ⇒ U2→U17
- [2,9,17]: (U2→U9 ; U9→U17) ⇒ U2→U17
- [3,7,8]: (U3→U7 ; U7→U8) ⇒ U3→U8
- [3,8,10]: (U3→U8 ; U8→U10) ⇒ U3→U10
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,7,8,17]
- [2,8,9,17]
- [3,8,10,15]
- [4,8,9,17]
- [4,10,12,16]
- [4,11,12,16]
- [4,11,14,16]
- [5,11,12,16]
- [5,12,13,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 115 0-cells, 462 1-cells, 564 2-cells, 216 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,10}
- {0} → {0,12}
- {0} → {0,13}
- {0} → {0,15}
- {0} → {0,10,12}
- {0} → {0,10,15}
- {0} → {0,12,13}
- {1} → {1,6}
- {1} → {1,11}
- {1} → {1,14}
- {1} → {1,6,14}
- {1} → {1,11,14}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,66]: ({0}→{0,10} ; {0,10}→{0,10,12}) ⇒ {0}→{0,10,12}
- [0,18,67]: ({0}→{0,10} ; {0,10}→{0,10,15}) ⇒ {0}→{0,10,15}
- [0,19,66]: ({0}→{0,12} ; {0,12}→{0,10,12}) ⇒ {0}→{0,10,12}
- [0,19,68]: ({0}→{0,12} ; {0,12}→{0,12,13}) ⇒ {0}→{0,12,13}
- [0,20,68]: ({0}→{0,13} ; {0,13}→{0,12,13}) ⇒ {0}→{0,12,13}
- [0,21,67]: ({0}→{0,15} ; {0,15}→{0,10,15}) ⇒ {0}→{0,10,15}
- [1,22,69]: ({1}→{1,6} ; {1,6}→{1,6,14}) ⇒ {1}→{1,6,14}
- [1,23,70]: ({1}→{1,11} ; {1,11}→{1,11,14}) ⇒ {1}→{1,11,14}
- [1,24,69]: ({1}→{1,14} ; {1,14}→{1,6,14}) ⇒ {1}→{1,6,14}
- [1,24,70]: ({1}→{1,14} ; {1,14}→{1,11,14}) ⇒ {1}→{1,11,14}
- [2,25,71]: ({2}→{2,7} ; {2,7}→{2,7,8}) ⇒ {2}→{2,7,8}
- [2,25,72]: ({2}→{2,7} ; {2,7}→{2,7,17}) ⇒ {2}→{2,7,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,25,71,106]
- [2,25,72,106]
- [2,26,71,106]
- [2,26,73,107]
- [2,26,74,106]
- [2,26,74,107]
- [2,27,73,107]
- [2,27,75,107]
- [2,28,72,106]
- [2,28,74,106]
- [2,28,74,107]
- [2,28,75,107]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

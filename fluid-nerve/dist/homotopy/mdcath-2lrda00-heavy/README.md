# homotopy.io export: CATH domain 2lrdA00 (mdCATH), heavy atoms (`mdcath-2lrda00-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 47 1-cells, 40 2-cells, 11 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U7
- U0 → U8
- U0 → U11
- U0 → U14
- U0 → U17
- U1 → U9
- U1 → U10
- U1 → U15
- U2 → U6
- U2 → U9
- U2 → U12
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,11]: (U0→U6 ; U6→U11) ⇒ U0→U11
- [0,7,8]: (U0→U7 ; U7→U8) ⇒ U0→U8
- [0,7,11]: (U0→U7 ; U7→U11) ⇒ U0→U11
- [0,7,14]: (U0→U7 ; U7→U14) ⇒ U0→U14
- [0,7,17]: (U0→U7 ; U7→U17) ⇒ U0→U17
- [0,8,14]: (U0→U8 ; U8→U14) ⇒ U0→U14
- [0,8,17]: (U0→U8 ; U8→U17) ⇒ U0→U17
- [0,11,17]: (U0→U11 ; U11→U17) ⇒ U0→U17
- [0,14,17]: (U0→U14 ; U14→U17) ⇒ U0→U17
- [1,9,15]: (U1→U9 ; U9→U15) ⇒ U1→U15
- [1,10,15]: (U1→U10 ; U10→U15) ⇒ U1→U15
- [2,6,12]: (U2→U6 ; U6→U12) ⇒ U2→U12
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,7,8,14]
- [0,7,8,17]
- [0,7,11,17]
- [0,7,14,17]
- [0,8,14,17]
- [3,10,13,16]
- [5,9,12,15]
- [5,10,13,15]
- [5,11,13,17]
- [7,8,14,17]
- [7,11,13,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 116 0-cells, 488 1-cells, 636 2-cells, 264 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,7}
- {0} → {0,8}
- {0} → {0,11}
- {0} → {0,14}
- {0} → {0,17}
- {0} → {0,6,11}
- {0} → {0,7,8}
- {0} → {0,7,11}
- {0} → {0,7,14}
- {0} → {0,7,17}
- {0} → {0,8,14}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,65]: ({0}→{0,6} ; {0,6}→{0,6,11}) ⇒ {0}→{0,6,11}
- [0,19,66]: ({0}→{0,7} ; {0,7}→{0,7,8}) ⇒ {0}→{0,7,8}
- [0,19,67]: ({0}→{0,7} ; {0,7}→{0,7,11}) ⇒ {0}→{0,7,11}
- [0,19,68]: ({0}→{0,7} ; {0,7}→{0,7,14}) ⇒ {0}→{0,7,14}
- [0,19,69]: ({0}→{0,7} ; {0,7}→{0,7,17}) ⇒ {0}→{0,7,17}
- [0,19,105]: ({0}→{0,7} ; {0,7}→{0,7,8,14}) ⇒ {0}→{0,7,8,14}
- [0,19,106]: ({0}→{0,7} ; {0,7}→{0,7,8,17}) ⇒ {0}→{0,7,8,17}
- [0,19,107]: ({0}→{0,7} ; {0,7}→{0,7,11,17}) ⇒ {0}→{0,7,11,17}
- [0,19,108]: ({0}→{0,7} ; {0,7}→{0,7,14,17}) ⇒ {0}→{0,7,14,17}
- [0,20,66]: ({0}→{0,8} ; {0,8}→{0,7,8}) ⇒ {0}→{0,7,8}
- [0,20,70]: ({0}→{0,8} ; {0,8}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,20,71]: ({0}→{0,8} ; {0,8}→{0,8,17}) ⇒ {0}→{0,8,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,19,66,105]
- [0,19,66,106]
- [0,19,67,107]
- [0,19,68,105]
- [0,19,68,108]
- [0,19,69,106]
- [0,19,69,107]
- [0,19,69,108]
- [0,20,66,105]
- [0,20,66,106]
- [0,20,70,105]
- [0,20,70,109]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

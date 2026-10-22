# homotopy.io export: CATH domain 1a92A00 (mdCATH), heavy atoms (`mdcath-1a92a00-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 47 1-cells, 37 2-cells, 8 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U7
- U0 → U8
- U0 → U9
- U0 → U14
- U0 → U15
- U0 → U16
- U0 → U17
- U1 → U10
- U1 → U11
- U2 → U5
- U2 → U9
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,15]: (U0→U6 ; U6→U15) ⇒ U0→U15
- [0,7,15]: (U0→U7 ; U7→U15) ⇒ U0→U15
- [0,7,16]: (U0→U7 ; U7→U16) ⇒ U0→U16
- [0,7,17]: (U0→U7 ; U7→U17) ⇒ U0→U17
- [0,8,9]: (U0→U8 ; U8→U9) ⇒ U0→U9
- [0,8,16]: (U0→U8 ; U8→U16) ⇒ U0→U16
- [0,8,17]: (U0→U8 ; U8→U17) ⇒ U0→U17
- [0,9,14]: (U0→U9 ; U9→U14) ⇒ U0→U14
- [0,9,17]: (U0→U9 ; U9→U17) ⇒ U0→U17
- [0,14,15]: (U0→U14 ; U14→U15) ⇒ U0→U15
- [0,15,17]: (U0→U15 ; U15→U17) ⇒ U0→U17
- [0,16,17]: (U0→U16 ; U16→U17) ⇒ U0→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,7,15,17]
- [0,7,16,17]
- [0,8,9,17]
- [0,8,16,17]
- [3,7,16,17]
- [3,8,16,17]
- [5,9,12,14]
- [7,8,16,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 110 0-cells, 428 1-cells, 510 2-cells, 192 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,7}
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,14}
- {0} → {0,15}
- {0} → {0,16}
- {0} → {0,17}
- {0} → {0,6,15}
- {0} → {0,7,15}
- {0} → {0,7,16}
- {0} → {0,7,17}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,65]: ({0}→{0,6} ; {0,6}→{0,6,15}) ⇒ {0}→{0,6,15}
- [0,19,66]: ({0}→{0,7} ; {0,7}→{0,7,15}) ⇒ {0}→{0,7,15}
- [0,19,67]: ({0}→{0,7} ; {0,7}→{0,7,16}) ⇒ {0}→{0,7,16}
- [0,19,68]: ({0}→{0,7} ; {0,7}→{0,7,17}) ⇒ {0}→{0,7,17}
- [0,19,102]: ({0}→{0,7} ; {0,7}→{0,7,15,17}) ⇒ {0}→{0,7,15,17}
- [0,19,103]: ({0}→{0,7} ; {0,7}→{0,7,16,17}) ⇒ {0}→{0,7,16,17}
- [0,20,69]: ({0}→{0,8} ; {0,8}→{0,8,9}) ⇒ {0}→{0,8,9}
- [0,20,70]: ({0}→{0,8} ; {0,8}→{0,8,16}) ⇒ {0}→{0,8,16}
- [0,20,71]: ({0}→{0,8} ; {0,8}→{0,8,17}) ⇒ {0}→{0,8,17}
- [0,20,104]: ({0}→{0,8} ; {0,8}→{0,8,9,17}) ⇒ {0}→{0,8,9,17}
- [0,20,105]: ({0}→{0,8} ; {0,8}→{0,8,16,17}) ⇒ {0}→{0,8,16,17}
- [0,21,69]: ({0}→{0,9} ; {0,9}→{0,8,9}) ⇒ {0}→{0,8,9}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,19,66,102]
- [0,19,67,103]
- [0,19,68,102]
- [0,19,68,103]
- [0,20,69,104]
- [0,20,70,105]
- [0,20,71,104]
- [0,20,71,105]
- [0,21,69,104]
- [0,21,73,104]
- [0,23,66,102]
- [0,23,75,102]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

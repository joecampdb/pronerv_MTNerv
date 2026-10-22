# homotopy.io export: CATH domain 1e5wA04 (mdCATH), heavy atoms (`mdcath-1e5wa04-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 45 1-cells, 33 2-cells, 5 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U8
- U0 → U9
- U0 → U12
- U0 → U13
- U0 → U15
- U0 → U17
- U1 → U7
- U1 → U10
- U1 → U14
- U2 → U6
- U2 → U9
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,15]: (U0→U6 ; U6→U15) ⇒ U0→U15
- [0,8,12]: (U0→U8 ; U8→U12) ⇒ U0→U12
- [0,8,13]: (U0→U8 ; U8→U13) ⇒ U0→U13
- [0,8,17]: (U0→U8 ; U8→U17) ⇒ U0→U17
- [0,9,12]: (U0→U9 ; U9→U12) ⇒ U0→U12
- [0,9,15]: (U0→U9 ; U9→U15) ⇒ U0→U15
- [0,12,15]: (U0→U12 ; U12→U15) ⇒ U0→U15
- [0,12,17]: (U0→U12 ; U12→U17) ⇒ U0→U17
- [0,13,15]: (U0→U13 ; U13→U15) ⇒ U0→U15
- [0,13,17]: (U0→U13 ; U13→U17) ⇒ U0→U17
- [0,15,17]: (U0→U15 ; U15→U17) ⇒ U0→U17
- [1,7,10]: (U1→U7 ; U7→U10) ⇒ U1→U10
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,8,12,17]
- [0,8,13,17]
- [0,9,12,15]
- [1,7,10,14]
- [5,8,16,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 101 0-cells, 358 1-cells, 378 2-cells, 120 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,12}
- {0} → {0,13}
- {0} → {0,15}
- {0} → {0,17}
- {0} → {0,6,15}
- {0} → {0,8,12}
- {0} → {0,8,13}
- {0} → {0,8,17}
- {0} → {0,9,12}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,63]: ({0}→{0,6} ; {0,6}→{0,6,15}) ⇒ {0}→{0,6,15}
- [0,19,64]: ({0}→{0,8} ; {0,8}→{0,8,12}) ⇒ {0}→{0,8,12}
- [0,19,65]: ({0}→{0,8} ; {0,8}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,19,66]: ({0}→{0,8} ; {0,8}→{0,8,17}) ⇒ {0}→{0,8,17}
- [0,19,96]: ({0}→{0,8} ; {0,8}→{0,8,12,17}) ⇒ {0}→{0,8,12,17}
- [0,19,97]: ({0}→{0,8} ; {0,8}→{0,8,13,17}) ⇒ {0}→{0,8,13,17}
- [0,20,67]: ({0}→{0,9} ; {0,9}→{0,9,12}) ⇒ {0}→{0,9,12}
- [0,20,68]: ({0}→{0,9} ; {0,9}→{0,9,15}) ⇒ {0}→{0,9,15}
- [0,20,98]: ({0}→{0,9} ; {0,9}→{0,9,12,15}) ⇒ {0}→{0,9,12,15}
- [0,21,64]: ({0}→{0,12} ; {0,12}→{0,8,12}) ⇒ {0}→{0,8,12}
- [0,21,67]: ({0}→{0,12} ; {0,12}→{0,9,12}) ⇒ {0}→{0,9,12}
- [0,21,69]: ({0}→{0,12} ; {0,12}→{0,12,15}) ⇒ {0}→{0,12,15}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,19,64,96]
- [0,19,65,97]
- [0,19,66,96]
- [0,19,66,97]
- [0,20,67,98]
- [0,20,68,98]
- [0,21,64,96]
- [0,21,67,98]
- [0,21,69,98]
- [0,21,70,96]
- [0,22,65,97]
- [0,22,72,97]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

# homotopy.io export: CATH domain 1l6hA00 (mdCATH), heavy atoms (`mdcath-1l6ha00-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 44 1-cells, 32 2-cells, 6 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U8
- U0 → U11
- U0 → U12
- U0 → U13
- U0 → U17
- U1 → U9
- U1 → U10
- U1 → U14
- U2 → U7
- U2 → U8
- U3 → U16
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,12]: (U0→U6 ; U6→U12) ⇒ U0→U12
- [0,6,13]: (U0→U6 ; U6→U13) ⇒ U0→U13
- [0,8,11]: (U0→U8 ; U8→U11) ⇒ U0→U11
- [0,8,17]: (U0→U8 ; U8→U17) ⇒ U0→U17
- [0,11,13]: (U0→U11 ; U11→U13) ⇒ U0→U13
- [0,11,17]: (U0→U11 ; U11→U17) ⇒ U0→U17
- [0,12,13]: (U0→U12 ; U12→U13) ⇒ U0→U13
- [0,12,17]: (U0→U12 ; U12→U17) ⇒ U0→U17
- [1,9,14]: (U1→U9 ; U9→U14) ⇒ U1→U14
- [1,10,14]: (U1→U10 ; U10→U14) ⇒ U1→U14
- [4,7,15]: (U4→U7 ; U7→U15) ⇒ U4→U15
- [4,10,14]: (U4→U10 ; U10→U14) ⇒ U4→U14
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,6,12,13]
- [0,8,11,17]
- [4,10,14,15]
- [5,7,11,15]
- [5,9,13,16]
- [6,9,13,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 100 0-cells, 364 1-cells, 408 2-cells, 144 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,8}
- {0} → {0,11}
- {0} → {0,12}
- {0} → {0,13}
- {0} → {0,17}
- {0} → {0,6,12}
- {0} → {0,6,13}
- {0} → {0,8,11}
- {0} → {0,8,17}
- {0} → {0,11,13}
- {0} → {0,11,17}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,62]: ({0}→{0,6} ; {0,6}→{0,6,12}) ⇒ {0}→{0,6,12}
- [0,18,63]: ({0}→{0,6} ; {0,6}→{0,6,13}) ⇒ {0}→{0,6,13}
- [0,18,94]: ({0}→{0,6} ; {0,6}→{0,6,12,13}) ⇒ {0}→{0,6,12,13}
- [0,19,64]: ({0}→{0,8} ; {0,8}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,19,65]: ({0}→{0,8} ; {0,8}→{0,8,17}) ⇒ {0}→{0,8,17}
- [0,19,95]: ({0}→{0,8} ; {0,8}→{0,8,11,17}) ⇒ {0}→{0,8,11,17}
- [0,20,64]: ({0}→{0,11} ; {0,11}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,20,66]: ({0}→{0,11} ; {0,11}→{0,11,13}) ⇒ {0}→{0,11,13}
- [0,20,67]: ({0}→{0,11} ; {0,11}→{0,11,17}) ⇒ {0}→{0,11,17}
- [0,20,95]: ({0}→{0,11} ; {0,11}→{0,8,11,17}) ⇒ {0}→{0,8,11,17}
- [0,21,62]: ({0}→{0,12} ; {0,12}→{0,6,12}) ⇒ {0}→{0,6,12}
- [0,21,68]: ({0}→{0,12} ; {0,12}→{0,12,13}) ⇒ {0}→{0,12,13}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,62,94]
- [0,18,63,94]
- [0,19,64,95]
- [0,19,65,95]
- [0,20,64,95]
- [0,20,67,95]
- [0,21,62,94]
- [0,21,68,94]
- [0,22,63,94]
- [0,22,68,94]
- [0,23,65,95]
- [0,23,67,95]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

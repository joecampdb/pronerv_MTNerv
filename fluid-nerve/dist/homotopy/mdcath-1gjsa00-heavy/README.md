# homotopy.io export: CATH domain 1gjsA00 (mdCATH), heavy atoms (`mdcath-1gjsa00-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 46 1-cells, 35 2-cells, 7 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U5
- U0 → U10
- U0 → U12
- U0 → U15
- U1 → U7
- U1 → U9
- U2 → U6
- U2 → U8
- U2 → U11
- U2 → U17
- U3 → U7
- U3 → U14
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,5,12]: (U0→U5 ; U5→U12) ⇒ U0→U12
- [0,5,15]: (U0→U5 ; U5→U15) ⇒ U0→U15
- [0,10,12]: (U0→U10 ; U10→U12) ⇒ U0→U12
- [0,10,15]: (U0→U10 ; U10→U15) ⇒ U0→U15
- [0,12,15]: (U0→U12 ; U12→U15) ⇒ U0→U15
- [1,7,9]: (U1→U7 ; U7→U9) ⇒ U1→U9
- [2,6,11]: (U2→U6 ; U6→U11) ⇒ U2→U11
- [2,6,17]: (U2→U6 ; U6→U17) ⇒ U2→U17
- [2,11,17]: (U2→U11 ; U11→U17) ⇒ U2→U17
- [3,7,16]: (U3→U7 ; U7→U16) ⇒ U3→U16
- [3,14,16]: (U3→U14 ; U14→U16) ⇒ U3→U16
- [4,8,9]: (U4→U8 ; U8→U9) ⇒ U4→U9
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,5,12,15]
- [0,10,12,15]
- [2,6,11,17]
- [4,10,12,13]
- [5,7,13,16]
- [5,12,13,16]
- [5,14,15,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 106 0-cells, 400 1-cells, 462 2-cells, 168 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,5}
- {0} → {0,10}
- {0} → {0,12}
- {0} → {0,15}
- {0} → {0,5,12}
- {0} → {0,5,15}
- {0} → {0,10,12}
- {0} → {0,10,15}
- {0} → {0,12,15}
- {0} → {0,5,12,15}
- {0} → {0,10,12,15}
- {1} → {1,7}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,64]: ({0}→{0,5} ; {0,5}→{0,5,12}) ⇒ {0}→{0,5,12}
- [0,18,65]: ({0}→{0,5} ; {0,5}→{0,5,15}) ⇒ {0}→{0,5,15}
- [0,18,99]: ({0}→{0,5} ; {0,5}→{0,5,12,15}) ⇒ {0}→{0,5,12,15}
- [0,19,66]: ({0}→{0,10} ; {0,10}→{0,10,12}) ⇒ {0}→{0,10,12}
- [0,19,67]: ({0}→{0,10} ; {0,10}→{0,10,15}) ⇒ {0}→{0,10,15}
- [0,19,100]: ({0}→{0,10} ; {0,10}→{0,10,12,15}) ⇒ {0}→{0,10,12,15}
- [0,20,64]: ({0}→{0,12} ; {0,12}→{0,5,12}) ⇒ {0}→{0,5,12}
- [0,20,66]: ({0}→{0,12} ; {0,12}→{0,10,12}) ⇒ {0}→{0,10,12}
- [0,20,68]: ({0}→{0,12} ; {0,12}→{0,12,15}) ⇒ {0}→{0,12,15}
- [0,20,99]: ({0}→{0,12} ; {0,12}→{0,5,12,15}) ⇒ {0}→{0,5,12,15}
- [0,20,100]: ({0}→{0,12} ; {0,12}→{0,10,12,15}) ⇒ {0}→{0,10,12,15}
- [0,21,65]: ({0}→{0,15} ; {0,15}→{0,5,15}) ⇒ {0}→{0,5,15}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,64,99]
- [0,18,65,99]
- [0,19,66,100]
- [0,19,67,100]
- [0,20,64,99]
- [0,20,66,100]
- [0,20,68,99]
- [0,20,68,100]
- [0,21,65,99]
- [0,21,67,100]
- [0,21,68,99]
- [0,21,68,100]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

# homotopy.io export: CATH domain 2lrdA00 (mdCATH), C-alpha (`mdcath-2lrda00-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 37 1-cells, 19 2-cells, 1 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U8
- U0 → U10
- U0 → U11
- U0 → U17
- U1 → U9
- U2 → U12
- U2 → U15
- U2 → U16
- U3 → U6
- U3 → U10
- U3 → U17
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,11]: (U0→U6 ; U6→U11) ⇒ U0→U11
- [0,6,17]: (U0→U6 ; U6→U17) ⇒ U0→U17
- [0,8,11]: (U0→U8 ; U8→U11) ⇒ U0→U11
- [0,10,17]: (U0→U10 ; U10→U17) ⇒ U0→U17
- [2,12,15]: (U2→U12 ; U12→U15) ⇒ U2→U15
- [3,6,17]: (U3→U6 ; U6→U17) ⇒ U3→U17
- [3,10,17]: (U3→U10 ; U10→U17) ⇒ U3→U17
- [4,6,13]: (U4→U6 ; U6→U13) ⇒ U4→U13
- [4,7,12]: (U4→U7 ; U7→U12) ⇒ U4→U12
- [4,7,13]: (U4→U7 ; U7→U13) ⇒ U4→U13
- [4,9,14]: (U4→U9 ; U9→U14) ⇒ U4→U14
- [4,12,13]: (U4→U12 ; U12→U13) ⇒ U4→U13
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [4,7,12,13]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 75 0-cells, 202 1-cells, 150 2-cells, 24 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,8}
- {0} → {0,10}
- {0} → {0,11}
- {0} → {0,17}
- {0} → {0,6,11}
- {0} → {0,6,17}
- {0} → {0,8,11}
- {0} → {0,10,17}
- {1} → {1,9}
- {2} → {2,12}
- {2} → {2,15}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,55]: ({0}→{0,6} ; {0,6}→{0,6,11}) ⇒ {0}→{0,6,11}
- [0,18,56]: ({0}→{0,6} ; {0,6}→{0,6,17}) ⇒ {0}→{0,6,17}
- [0,19,57]: ({0}→{0,8} ; {0,8}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,20,58]: ({0}→{0,10} ; {0,10}→{0,10,17}) ⇒ {0}→{0,10,17}
- [0,21,55]: ({0}→{0,11} ; {0,11}→{0,6,11}) ⇒ {0}→{0,6,11}
- [0,21,57]: ({0}→{0,11} ; {0,11}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,22,56]: ({0}→{0,17} ; {0,17}→{0,6,17}) ⇒ {0}→{0,6,17}
- [0,22,58]: ({0}→{0,17} ; {0,17}→{0,10,17}) ⇒ {0}→{0,10,17}
- [2,24,59]: ({2}→{2,12} ; {2,12}→{2,12,15}) ⇒ {2}→{2,12,15}
- [2,25,59]: ({2}→{2,15} ; {2,15}→{2,12,15}) ⇒ {2}→{2,12,15}
- [3,27,60]: ({3}→{3,6} ; {3,6}→{3,6,17}) ⇒ {3}→{3,6,17}
- [3,28,61]: ({3}→{3,10} ; {3,10}→{3,10,17}) ⇒ {3}→{3,10,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [4,31,63,74]
- [4,31,64,74]
- [4,33,63,74]
- [4,33,66,74]
- [4,34,64,74]
- [4,34,66,74]
- [7,31,63,74]
- [7,31,64,74]
- [7,44,63,74]
- [7,44,72,74]
- [7,45,64,74]
- [7,45,72,74]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

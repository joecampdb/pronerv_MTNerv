# homotopy.io export: CATH domain 1x4pA00 (mdCATH), heavy atoms (`mdcath-1x4pa00-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 39 1-cells, 19 2-cells, 2 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U9
- U0 → U10
- U0 → U11
- U0 → U16
- U1 → U7
- U1 → U8
- U2 → U12
- U2 → U14
- U2 → U15
- U2 → U17
- U3 → U6
- U3 → U10
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,9,11]: (U0→U9 ; U9→U11) ⇒ U0→U11
- [0,10,16]: (U0→U10 ; U10→U16) ⇒ U0→U16
- [0,11,16]: (U0→U11 ; U11→U16) ⇒ U0→U16
- [2,12,14]: (U2→U12 ; U12→U14) ⇒ U2→U14
- [2,12,17]: (U2→U12 ; U12→U17) ⇒ U2→U17
- [2,14,17]: (U2→U14 ; U14→U17) ⇒ U2→U17
- [4,7,13]: (U4→U7 ; U7→U13) ⇒ U4→U13
- [5,6,14]: (U5→U6 ; U6→U14) ⇒ U5→U14
- [5,6,16]: (U5→U6 ; U6→U16) ⇒ U5→U16
- [5,7,11]: (U5→U7 ; U7→U11) ⇒ U5→U11
- [5,8,17]: (U5→U8 ; U8→U17) ⇒ U5→U17
- [5,11,16]: (U5→U11 ; U11→U16) ⇒ U5→U16
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,12,14,17]
- [5,6,14,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 78 0-cells, 220 1-cells, 186 2-cells, 48 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,9}
- {0} → {0,10}
- {0} → {0,11}
- {0} → {0,16}
- {0} → {0,9,11}
- {0} → {0,10,16}
- {0} → {0,11,16}
- {1} → {1,7}
- {1} → {1,8}
- {2} → {2,12}
- {2} → {2,14}
- {2} → {2,15}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,57]: ({0}→{0,9} ; {0,9}→{0,9,11}) ⇒ {0}→{0,9,11}
- [0,19,58]: ({0}→{0,10} ; {0,10}→{0,10,16}) ⇒ {0}→{0,10,16}
- [0,20,57]: ({0}→{0,11} ; {0,11}→{0,9,11}) ⇒ {0}→{0,9,11}
- [0,20,59]: ({0}→{0,11} ; {0,11}→{0,11,16}) ⇒ {0}→{0,11,16}
- [0,21,58]: ({0}→{0,16} ; {0,16}→{0,10,16}) ⇒ {0}→{0,10,16}
- [0,21,59]: ({0}→{0,16} ; {0,16}→{0,11,16}) ⇒ {0}→{0,11,16}
- [2,24,60]: ({2}→{2,12} ; {2,12}→{2,12,14}) ⇒ {2}→{2,12,14}
- [2,24,61]: ({2}→{2,12} ; {2,12}→{2,12,17}) ⇒ {2}→{2,12,17}
- [2,24,76]: ({2}→{2,12} ; {2,12}→{2,12,14,17}) ⇒ {2}→{2,12,14,17}
- [2,25,60]: ({2}→{2,14} ; {2,14}→{2,12,14}) ⇒ {2}→{2,12,14}
- [2,25,62]: ({2}→{2,14} ; {2,14}→{2,14,17}) ⇒ {2}→{2,14,17}
- [2,25,76]: ({2}→{2,14} ; {2,14}→{2,12,14,17}) ⇒ {2}→{2,12,14,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,24,60,76]
- [2,24,61,76]
- [2,25,60,76]
- [2,25,62,76]
- [2,27,61,76]
- [2,27,62,76]
- [5,34,64,77]
- [5,34,65,77]
- [5,38,64,77]
- [5,38,69,77]
- [5,39,65,77]
- [5,39,69,77]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

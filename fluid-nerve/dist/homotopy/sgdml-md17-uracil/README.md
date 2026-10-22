# homotopy.io export: uracil (MD17 ab initio MD) (`sgdml-md17-uracil`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 11 1-cells, 2 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U15
- U0 → U16
- U2 → U17
- U5 → U16
- U6 → U14
- U6 → U15
- U6 → U17
- U7 → U15
- U12 → U16
- U14 → U17
- U15 → U17

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [6,14,17]: (U6→U14 ; U14→U17) ⇒ U6→U17
- [6,15,17]: (U6→U15 ; U15→U17) ⇒ U6→U17

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 31 0-cells, 34 1-cells, 12 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,15}
- {0} → {0,16}
- {2} → {2,17}
- {5} → {5,16}
- {6} → {6,14}
- {6} → {6,15}
- {6} → {6,17}
- {6} → {6,14,17}
- {6} → {6,15,17}
- {7} → {7,15}
- {12} → {12,16}
- {14} → {6,14}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [6,22,29]: ({6}→{6,14} ; {6,14}→{6,14,17}) ⇒ {6}→{6,14,17}
- [6,23,30]: ({6}→{6,15} ; {6,15}→{6,15,17}) ⇒ {6}→{6,15,17}
- [6,24,29]: ({6}→{6,17} ; {6,17}→{6,14,17}) ⇒ {6}→{6,14,17}
- [6,24,30]: ({6}→{6,17} ; {6,17}→{6,15,17}) ⇒ {6}→{6,15,17}
- [14,22,29]: ({14}→{6,14} ; {6,14}→{6,14,17}) ⇒ {14}→{6,14,17}
- [14,27,29]: ({14}→{14,17} ; {14,17}→{6,14,17}) ⇒ {14}→{6,14,17}
- [15,23,30]: ({15}→{6,15} ; {6,15}→{6,15,17}) ⇒ {15}→{6,15,17}
- [15,28,30]: ({15}→{15,17} ; {15,17}→{6,15,17}) ⇒ {15}→{6,15,17}
- [17,24,29]: ({17}→{6,17} ; {6,17}→{6,14,17}) ⇒ {17}→{6,14,17}
- [17,24,30]: ({17}→{6,17} ; {6,17}→{6,15,17}) ⇒ {17}→{6,15,17}
- [17,27,29]: ({17}→{14,17} ; {14,17}→{6,14,17}) ⇒ {17}→{6,14,17}
- [17,28,30]: ({17}→{15,17} ; {15,17}→{6,15,17}) ⇒ {17}→{6,15,17}

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

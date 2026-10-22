# homotopy.io export: CATH domain 1hcrA00 (mdCATH), C-alpha (`mdcath-1hcra00-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 34 1-cells, 13 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U10
- U0 → U12
- U0 → U13
- U0 → U17
- U1 → U9
- U1 → U11
- U1 → U15
- U2 → U14
- U2 → U16
- U3 → U8
- U3 → U9
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,13]: (U0→U8 ; U8→U13) ⇒ U0→U13
- [0,10,17]: (U0→U10 ; U10→U17) ⇒ U0→U17
- [0,12,13]: (U0→U12 ; U12→U13) ⇒ U0→U13
- [0,12,17]: (U0→U12 ; U12→U17) ⇒ U0→U17
- [1,11,15]: (U1→U11 ; U11→U15) ⇒ U1→U15
- [2,14,16]: (U2→U14 ; U14→U16) ⇒ U2→U16
- [3,8,13]: (U3→U8 ; U8→U13) ⇒ U3→U13
- [4,11,15]: (U4→U11 ; U11→U15) ⇒ U4→U15
- [6,12,13]: (U6→U12 ; U12→U13) ⇒ U6→U13
- [7,10,17]: (U7→U10 ; U10→U17) ⇒ U7→U17
- [7,12,17]: (U7→U12 ; U12→U17) ⇒ U7→U17
- [7,14,16]: (U7→U14 ; U14→U16) ⇒ U7→U16
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 65 0-cells, 146 1-cells, 78 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,10}
- {0} → {0,12}
- {0} → {0,13}
- {0} → {0,17}
- {0} → {0,8,13}
- {0} → {0,10,17}
- {0} → {0,12,13}
- {0} → {0,12,17}
- {1} → {1,9}
- {1} → {1,11}
- {1} → {1,15}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,52]: ({0}→{0,8} ; {0,8}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,19,53]: ({0}→{0,10} ; {0,10}→{0,10,17}) ⇒ {0}→{0,10,17}
- [0,20,54]: ({0}→{0,12} ; {0,12}→{0,12,13}) ⇒ {0}→{0,12,13}
- [0,20,55]: ({0}→{0,12} ; {0,12}→{0,12,17}) ⇒ {0}→{0,12,17}
- [0,21,52]: ({0}→{0,13} ; {0,13}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,21,54]: ({0}→{0,13} ; {0,13}→{0,12,13}) ⇒ {0}→{0,12,13}
- [0,22,53]: ({0}→{0,17} ; {0,17}→{0,10,17}) ⇒ {0}→{0,10,17}
- [0,22,55]: ({0}→{0,17} ; {0,17}→{0,12,17}) ⇒ {0}→{0,12,17}
- [1,24,56]: ({1}→{1,11} ; {1,11}→{1,11,15}) ⇒ {1}→{1,11,15}
- [1,25,56]: ({1}→{1,15} ; {1,15}→{1,11,15}) ⇒ {1}→{1,11,15}
- [2,26,57]: ({2}→{2,14} ; {2,14}→{2,14,16}) ⇒ {2}→{2,14,16}
- [2,27,57]: ({2}→{2,16} ; {2,16}→{2,14,16}) ⇒ {2}→{2,14,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

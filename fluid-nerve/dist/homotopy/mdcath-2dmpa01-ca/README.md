# homotopy.io export: CATH domain 2dmpA01 (mdCATH), C-alpha (`mdcath-2dmpa01-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 38 1-cells, 20 2-cells, 1 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U9
- U0 → U12
- U0 → U14
- U0 → U16
- U1 → U7
- U1 → U10
- U2 → U15
- U2 → U17
- U3 → U7
- U3 → U8
- U3 → U13
- U4 → U9
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,9,16]: (U0→U9 ; U9→U16) ⇒ U0→U16
- [0,12,14]: (U0→U12 ; U12→U14) ⇒ U0→U14
- [0,14,16]: (U0→U14 ; U14→U16) ⇒ U0→U16
- [2,15,17]: (U2→U15 ; U15→U17) ⇒ U2→U17
- [3,8,13]: (U3→U8 ; U8→U13) ⇒ U3→U13
- [4,9,16]: (U4→U9 ; U9→U16) ⇒ U4→U16
- [4,10,11]: (U4→U10 ; U10→U11) ⇒ U4→U11
- [4,11,16]: (U4→U11 ; U11→U16) ⇒ U4→U16
- [5,8,13]: (U5→U8 ; U8→U13) ⇒ U5→U13
- [5,8,15]: (U5→U8 ; U8→U15) ⇒ U5→U15
- [5,8,17]: (U5→U8 ; U8→U17) ⇒ U5→U17
- [5,12,14]: (U5→U12 ; U12→U14) ⇒ U5→U14
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [5,8,15,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 77 0-cells, 210 1-cells, 156 2-cells, 24 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,9}
- {0} → {0,12}
- {0} → {0,14}
- {0} → {0,16}
- {0} → {0,9,16}
- {0} → {0,12,14}
- {0} → {0,14,16}
- {1} → {1,7}
- {1} → {1,10}
- {2} → {2,15}
- {2} → {2,17}
- {2} → {2,15,17}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,56]: ({0}→{0,9} ; {0,9}→{0,9,16}) ⇒ {0}→{0,9,16}
- [0,19,57]: ({0}→{0,12} ; {0,12}→{0,12,14}) ⇒ {0}→{0,12,14}
- [0,20,57]: ({0}→{0,14} ; {0,14}→{0,12,14}) ⇒ {0}→{0,12,14}
- [0,20,58]: ({0}→{0,14} ; {0,14}→{0,14,16}) ⇒ {0}→{0,14,16}
- [0,21,56]: ({0}→{0,16} ; {0,16}→{0,9,16}) ⇒ {0}→{0,9,16}
- [0,21,58]: ({0}→{0,16} ; {0,16}→{0,14,16}) ⇒ {0}→{0,14,16}
- [2,24,59]: ({2}→{2,15} ; {2,15}→{2,15,17}) ⇒ {2}→{2,15,17}
- [2,25,59]: ({2}→{2,17} ; {2,17}→{2,15,17}) ⇒ {2}→{2,15,17}
- [3,27,60]: ({3}→{3,8} ; {3,8}→{3,8,13}) ⇒ {3}→{3,8,13}
- [3,28,60]: ({3}→{3,13} ; {3,13}→{3,8,13}) ⇒ {3}→{3,8,13}
- [4,29,61]: ({4}→{4,9} ; {4,9}→{4,9,16}) ⇒ {4}→{4,9,16}
- [4,30,62]: ({4}→{4,10} ; {4,10}→{4,10,11}) ⇒ {4}→{4,10,11}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [5,33,65,76]
- [5,33,66,76]
- [5,37,65,76]
- [5,37,70,76]
- [5,38,66,76]
- [5,38,70,76]
- [8,33,65,76]
- [8,33,66,76]
- [8,46,65,76]
- [8,46,75,76]
- [8,47,66,76]
- [8,47,75,76]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

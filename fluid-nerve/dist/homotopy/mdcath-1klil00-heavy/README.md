# homotopy.io export: CATH domain 1kliL00 (mdCATH), heavy atoms (`mdcath-1klil00-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 38 1-cells, 21 2-cells, 3 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U8
- U0 → U9
- U0 → U14
- U0 → U17
- U1 → U11
- U1 → U12
- U1 → U15
- U2 → U9
- U2 → U10
- U2 → U13
- U2 → U16
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,14]: (U0→U8 ; U8→U14) ⇒ U0→U14
- [0,8,17]: (U0→U8 ; U8→U17) ⇒ U0→U17
- [0,14,17]: (U0→U14 ; U14→U17) ⇒ U0→U17
- [1,11,12]: (U1→U11 ; U11→U12) ⇒ U1→U12
- [1,11,15]: (U1→U11 ; U11→U15) ⇒ U1→U15
- [2,9,13]: (U2→U9 ; U9→U13) ⇒ U2→U13
- [2,9,16]: (U2→U9 ; U9→U16) ⇒ U2→U16
- [2,10,16]: (U2→U10 ; U10→U16) ⇒ U2→U16
- [2,13,16]: (U2→U13 ; U13→U16) ⇒ U2→U16
- [3,9,13]: (U3→U9 ; U9→U13) ⇒ U3→U13
- [4,8,14]: (U4→U8 ; U8→U14) ⇒ U4→U14
- [4,11,14]: (U4→U11 ; U11→U14) ⇒ U4→U14
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,8,14,17]
- [2,9,13,16]
- [5,10,12,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 80 0-cells, 244 1-cells, 234 2-cells, 72 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,14}
- {0} → {0,17}
- {0} → {0,8,14}
- {0} → {0,8,17}
- {0} → {0,14,17}
- {0} → {0,8,14,17}
- {1} → {1,11}
- {1} → {1,12}
- {1} → {1,15}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,19,56]: ({0}→{0,8} ; {0,8}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,19,57]: ({0}→{0,8} ; {0,8}→{0,8,17}) ⇒ {0}→{0,8,17}
- [0,19,77]: ({0}→{0,8} ; {0,8}→{0,8,14,17}) ⇒ {0}→{0,8,14,17}
- [0,21,56]: ({0}→{0,14} ; {0,14}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,21,58]: ({0}→{0,14} ; {0,14}→{0,14,17}) ⇒ {0}→{0,14,17}
- [0,21,77]: ({0}→{0,14} ; {0,14}→{0,8,14,17}) ⇒ {0}→{0,8,14,17}
- [0,22,57]: ({0}→{0,17} ; {0,17}→{0,8,17}) ⇒ {0}→{0,8,17}
- [0,22,58]: ({0}→{0,17} ; {0,17}→{0,14,17}) ⇒ {0}→{0,14,17}
- [0,22,77]: ({0}→{0,17} ; {0,17}→{0,8,14,17}) ⇒ {0}→{0,8,14,17}
- [0,56,77]: ({0}→{0,8,14} ; {0,8,14}→{0,8,14,17}) ⇒ {0}→{0,8,14,17}
- [0,57,77]: ({0}→{0,8,17} ; {0,8,17}→{0,8,14,17}) ⇒ {0}→{0,8,14,17}
- [0,58,77]: ({0}→{0,14,17} ; {0,14,17}→{0,8,14,17}) ⇒ {0}→{0,8,14,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,19,56,77]
- [0,19,57,77]
- [0,21,56,77]
- [0,21,58,77]
- [0,22,57,77]
- [0,22,58,77]
- [2,26,61,78]
- [2,26,62,78]
- [2,28,61,78]
- [2,28,64,78]
- [2,29,62,78]
- [2,29,64,78]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

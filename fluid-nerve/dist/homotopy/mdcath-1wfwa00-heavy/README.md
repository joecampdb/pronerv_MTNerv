# homotopy.io export: CATH domain 1wfwA00 (mdCATH), heavy atoms (`mdcath-1wfwa00-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 39 1-cells, 23 2-cells, 2 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U9
- U0 → U11
- U0 → U14
- U0 → U17
- U1 → U7
- U1 → U15
- U2 → U12
- U2 → U13
- U3 → U7
- U3 → U8
- U3 → U10
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,9]: (U0→U8 ; U8→U9) ⇒ U0→U9
- [0,8,14]: (U0→U8 ; U8→U14) ⇒ U0→U14
- [0,11,14]: (U0→U11 ; U11→U14) ⇒ U0→U14
- [0,11,17]: (U0→U11 ; U11→U17) ⇒ U0→U17
- [0,14,17]: (U0→U14 ; U14→U17) ⇒ U0→U17
- [1,7,15]: (U1→U7 ; U7→U15) ⇒ U1→U15
- [2,12,13]: (U2→U12 ; U12→U13) ⇒ U2→U13
- [3,7,10]: (U3→U7 ; U7→U10) ⇒ U3→U10
- [3,8,16]: (U3→U8 ; U8→U16) ⇒ U3→U16
- [3,10,16]: (U3→U10 ; U10→U16) ⇒ U3→U16
- [4,11,13]: (U4→U11 ; U11→U13) ⇒ U4→U13
- [4,11,17]: (U4→U11 ; U11→U17) ⇒ U4→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,11,14,17]
- [5,10,14,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 82 0-cells, 244 1-cells, 210 2-cells, 48 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,11}
- {0} → {0,14}
- {0} → {0,17}
- {0} → {0,8,9}
- {0} → {0,8,14}
- {0} → {0,11,14}
- {0} → {0,11,17}
- {0} → {0,14,17}
- {0} → {0,11,14,17}
- {1} → {1,7}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,57]: ({0}→{0,8} ; {0,8}→{0,8,9}) ⇒ {0}→{0,8,9}
- [0,18,58]: ({0}→{0,8} ; {0,8}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,19,57]: ({0}→{0,9} ; {0,9}→{0,8,9}) ⇒ {0}→{0,8,9}
- [0,20,59]: ({0}→{0,11} ; {0,11}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,20,60]: ({0}→{0,11} ; {0,11}→{0,11,17}) ⇒ {0}→{0,11,17}
- [0,20,80]: ({0}→{0,11} ; {0,11}→{0,11,14,17}) ⇒ {0}→{0,11,14,17}
- [0,21,58]: ({0}→{0,14} ; {0,14}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,21,59]: ({0}→{0,14} ; {0,14}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,21,61]: ({0}→{0,14} ; {0,14}→{0,14,17}) ⇒ {0}→{0,14,17}
- [0,21,80]: ({0}→{0,14} ; {0,14}→{0,11,14,17}) ⇒ {0}→{0,11,14,17}
- [0,22,60]: ({0}→{0,17} ; {0,17}→{0,11,17}) ⇒ {0}→{0,11,17}
- [0,22,61]: ({0}→{0,17} ; {0,17}→{0,14,17}) ⇒ {0}→{0,14,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,20,59,80]
- [0,20,60,80]
- [0,21,59,80]
- [0,21,61,80]
- [0,22,60,80]
- [0,22,61,80]
- [5,34,69,81]
- [5,34,71,81]
- [5,37,69,81]
- [5,37,74,81]
- [5,39,71,81]
- [5,39,74,81]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

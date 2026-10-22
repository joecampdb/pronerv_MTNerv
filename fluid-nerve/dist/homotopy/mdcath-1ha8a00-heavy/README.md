# homotopy.io export: CATH domain 1ha8A00 (mdCATH), heavy atoms (`mdcath-1ha8a00-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 39 1-cells, 21 2-cells, 2 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U10
- U0 → U15
- U0 → U16
- U0 → U17
- U1 → U9
- U1 → U11
- U2 → U7
- U2 → U8
- U2 → U13
- U3 → U9
- U3 → U14
- U4 → U7
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,10,16]: (U0→U10 ; U10→U16) ⇒ U0→U16
- [0,10,17]: (U0→U10 ; U10→U17) ⇒ U0→U17
- [0,15,17]: (U0→U15 ; U15→U17) ⇒ U0→U17
- [0,16,17]: (U0→U16 ; U16→U17) ⇒ U0→U17
- [1,9,11]: (U1→U9 ; U9→U11) ⇒ U1→U11
- [3,9,14]: (U3→U9 ; U9→U14) ⇒ U3→U14
- [4,7,8]: (U4→U7 ; U7→U8) ⇒ U4→U8
- [4,7,11]: (U4→U7 ; U7→U11) ⇒ U4→U11
- [4,8,17]: (U4→U8 ; U8→U17) ⇒ U4→U17
- [4,10,12]: (U4→U10 ; U10→U12) ⇒ U4→U12
- [4,10,17]: (U4→U10 ; U10→U17) ⇒ U4→U17
- [4,12,14]: (U4→U12 ; U12→U14) ⇒ U4→U14
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,10,16,17]
- [6,8,15,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 80 0-cells, 232 1-cells, 198 2-cells, 48 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,10}
- {0} → {0,15}
- {0} → {0,16}
- {0} → {0,17}
- {0} → {0,10,16}
- {0} → {0,10,17}
- {0} → {0,15,17}
- {0} → {0,16,17}
- {0} → {0,10,16,17}
- {1} → {1,9}
- {1} → {1,11}
- {1} → {1,9,11}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,57]: ({0}→{0,10} ; {0,10}→{0,10,16}) ⇒ {0}→{0,10,16}
- [0,18,58]: ({0}→{0,10} ; {0,10}→{0,10,17}) ⇒ {0}→{0,10,17}
- [0,18,78]: ({0}→{0,10} ; {0,10}→{0,10,16,17}) ⇒ {0}→{0,10,16,17}
- [0,19,59]: ({0}→{0,15} ; {0,15}→{0,15,17}) ⇒ {0}→{0,15,17}
- [0,20,57]: ({0}→{0,16} ; {0,16}→{0,10,16}) ⇒ {0}→{0,10,16}
- [0,20,60]: ({0}→{0,16} ; {0,16}→{0,16,17}) ⇒ {0}→{0,16,17}
- [0,20,78]: ({0}→{0,16} ; {0,16}→{0,10,16,17}) ⇒ {0}→{0,10,16,17}
- [0,21,58]: ({0}→{0,17} ; {0,17}→{0,10,17}) ⇒ {0}→{0,10,17}
- [0,21,59]: ({0}→{0,17} ; {0,17}→{0,15,17}) ⇒ {0}→{0,15,17}
- [0,21,60]: ({0}→{0,17} ; {0,17}→{0,16,17}) ⇒ {0}→{0,16,17}
- [0,21,78]: ({0}→{0,17} ; {0,17}→{0,10,16,17}) ⇒ {0}→{0,10,16,17}
- [0,57,78]: ({0}→{0,10,16} ; {0,10,16}→{0,10,16,17}) ⇒ {0}→{0,10,16,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,57,78]
- [0,18,58,78]
- [0,20,57,78]
- [0,20,60,78]
- [0,21,58,78]
- [0,21,60,78]
- [6,39,72,79]
- [6,39,73,79]
- [6,41,72,79]
- [6,41,74,79]
- [6,42,73,79]
- [6,42,74,79]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

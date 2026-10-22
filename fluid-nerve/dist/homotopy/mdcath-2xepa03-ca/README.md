# homotopy.io export: CATH domain 2xepA03 (mdCATH), C-alpha (`mdcath-2xepa03-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 39 1-cells, 20 2-cells, 2 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U9
- U0 → U10
- U0 → U14
- U0 → U15
- U0 → U17
- U1 → U7
- U1 → U8
- U1 → U11
- U2 → U9
- U2 → U12
- U2 → U16
- U3 → U10
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,9,14]: (U0→U9 ; U9→U14) ⇒ U0→U14
- [0,9,17]: (U0→U9 ; U9→U17) ⇒ U0→U17
- [0,10,15]: (U0→U10 ; U10→U15) ⇒ U0→U15
- [0,10,17]: (U0→U10 ; U10→U17) ⇒ U0→U17
- [2,9,12]: (U2→U9 ; U9→U12) ⇒ U2→U12
- [2,9,16]: (U2→U9 ; U9→U16) ⇒ U2→U16
- [2,12,16]: (U2→U12 ; U12→U16) ⇒ U2→U16
- [3,10,13]: (U3→U10 ; U10→U13) ⇒ U3→U13
- [4,8,16]: (U4→U8 ; U8→U16) ⇒ U4→U16
- [4,9,16]: (U4→U9 ; U9→U16) ⇒ U4→U16
- [4,9,17]: (U4→U9 ; U9→U17) ⇒ U4→U17
- [4,10,17]: (U4→U10 ; U10→U17) ⇒ U4→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,9,12,16]
- [4,9,16,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 79 0-cells, 226 1-cells, 192 2-cells, 48 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,9}
- {0} → {0,10}
- {0} → {0,14}
- {0} → {0,15}
- {0} → {0,17}
- {0} → {0,9,14}
- {0} → {0,9,17}
- {0} → {0,10,15}
- {0} → {0,10,17}
- {1} → {1,7}
- {1} → {1,8}
- {1} → {1,11}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,57]: ({0}→{0,9} ; {0,9}→{0,9,14}) ⇒ {0}→{0,9,14}
- [0,18,58]: ({0}→{0,9} ; {0,9}→{0,9,17}) ⇒ {0}→{0,9,17}
- [0,19,59]: ({0}→{0,10} ; {0,10}→{0,10,15}) ⇒ {0}→{0,10,15}
- [0,19,60]: ({0}→{0,10} ; {0,10}→{0,10,17}) ⇒ {0}→{0,10,17}
- [0,20,57]: ({0}→{0,14} ; {0,14}→{0,9,14}) ⇒ {0}→{0,9,14}
- [0,21,59]: ({0}→{0,15} ; {0,15}→{0,10,15}) ⇒ {0}→{0,10,15}
- [0,22,58]: ({0}→{0,17} ; {0,17}→{0,9,17}) ⇒ {0}→{0,9,17}
- [0,22,60]: ({0}→{0,17} ; {0,17}→{0,10,17}) ⇒ {0}→{0,10,17}
- [2,26,61]: ({2}→{2,9} ; {2,9}→{2,9,12}) ⇒ {2}→{2,9,12}
- [2,26,62]: ({2}→{2,9} ; {2,9}→{2,9,16}) ⇒ {2}→{2,9,16}
- [2,26,77]: ({2}→{2,9} ; {2,9}→{2,9,12,16}) ⇒ {2}→{2,9,12,16}
- [2,27,61]: ({2}→{2,12} ; {2,12}→{2,9,12}) ⇒ {2}→{2,9,12}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,26,61,77]
- [2,26,62,77]
- [2,27,61,77]
- [2,27,63,77]
- [2,28,62,77]
- [2,28,63,77]
- [4,33,66,78]
- [4,33,67,78]
- [4,36,66,78]
- [4,36,70,78]
- [4,37,67,78]
- [4,37,70,78]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

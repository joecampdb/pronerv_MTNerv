# homotopy.io export: CATH domain 5b1aJ00 (mdCATH), C-alpha (`mdcath-5b1aj00-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 38 1-cells, 20 2-cells, 2 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U13
- U0 → U14
- U0 → U16
- U1 → U9
- U1 → U11
- U2 → U10
- U2 → U12
- U3 → U9
- U3 → U10
- U3 → U15
- U4 → U7
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,13,14]: (U0→U13 ; U13→U14) ⇒ U0→U14
- [0,13,16]: (U0→U13 ; U13→U16) ⇒ U0→U16
- [2,10,12]: (U2→U10 ; U10→U12) ⇒ U2→U12
- [3,9,15]: (U3→U9 ; U9→U15) ⇒ U3→U15
- [4,7,13]: (U4→U7 ; U7→U13) ⇒ U4→U13
- [4,11,17]: (U4→U11 ; U11→U17) ⇒ U4→U17
- [4,13,17]: (U4→U13 ; U13→U17) ⇒ U4→U17
- [5,6,15]: (U5→U6 ; U6→U15) ⇒ U5→U15
- [5,6,16]: (U5→U6 ; U6→U16) ⇒ U5→U16
- [5,8,12]: (U5→U8 ; U8→U12) ⇒ U5→U12
- [5,10,12]: (U5→U10 ; U10→U12) ⇒ U5→U12
- [5,15,16]: (U5→U15 ; U15→U16) ⇒ U5→U16
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [5,6,15,16]
- [6,13,16,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 78 0-cells, 224 1-cells, 192 2-cells, 48 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,13}
- {0} → {0,14}
- {0} → {0,16}
- {0} → {0,13,14}
- {0} → {0,13,16}
- {1} → {1,9}
- {1} → {1,11}
- {2} → {2,10}
- {2} → {2,12}
- {2} → {2,10,12}
- {3} → {3,9}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,19,56]: ({0}→{0,13} ; {0,13}→{0,13,14}) ⇒ {0}→{0,13,14}
- [0,19,57]: ({0}→{0,13} ; {0,13}→{0,13,16}) ⇒ {0}→{0,13,16}
- [0,20,56]: ({0}→{0,14} ; {0,14}→{0,13,14}) ⇒ {0}→{0,13,14}
- [0,21,57]: ({0}→{0,16} ; {0,16}→{0,13,16}) ⇒ {0}→{0,13,16}
- [2,24,58]: ({2}→{2,10} ; {2,10}→{2,10,12}) ⇒ {2}→{2,10,12}
- [2,25,58]: ({2}→{2,12} ; {2,12}→{2,10,12}) ⇒ {2}→{2,10,12}
- [3,26,59]: ({3}→{3,9} ; {3,9}→{3,9,15}) ⇒ {3}→{3,9,15}
- [3,28,59]: ({3}→{3,15} ; {3,15}→{3,9,15}) ⇒ {3}→{3,9,15}
- [4,29,60]: ({4}→{4,7} ; {4,7}→{4,7,13}) ⇒ {4}→{4,7,13}
- [4,30,61]: ({4}→{4,11} ; {4,11}→{4,11,17}) ⇒ {4}→{4,11,17}
- [4,31,60]: ({4}→{4,13} ; {4,13}→{4,7,13}) ⇒ {4}→{4,7,13}
- [4,31,62]: ({4}→{4,13} ; {4,13}→{4,13,17}) ⇒ {4}→{4,13,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [5,33,63,76]
- [5,33,64,76]
- [5,37,63,76]
- [5,37,67,76]
- [5,38,64,76]
- [5,38,67,76]
- [6,33,63,76]
- [6,33,64,76]
- [6,41,70,77]
- [6,41,71,77]
- [6,42,63,76]
- [6,42,72,76]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

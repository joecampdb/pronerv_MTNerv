# homotopy.io export: CATH domain 2j8gA03 (mdCATH), C-alpha (`mdcath-2j8ga03-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 43 1-cells, 30 2-cells, 4 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U9
- U0 → U11
- U0 → U12
- U1 → U10
- U1 → U14
- U2 → U8
- U2 → U13
- U2 → U16
- U2 → U17
- U3 → U6
- U3 → U7
- U3 → U9
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,9,12]: (U0→U9 ; U9→U12) ⇒ U0→U12
- [0,11,12]: (U0→U11 ; U11→U12) ⇒ U0→U12
- [1,10,14]: (U1→U10 ; U10→U14) ⇒ U1→U14
- [2,8,17]: (U2→U8 ; U8→U17) ⇒ U2→U17
- [2,13,16]: (U2→U13 ; U13→U16) ⇒ U2→U16
- [2,13,17]: (U2→U13 ; U13→U17) ⇒ U2→U17
- [2,16,17]: (U2→U16 ; U16→U17) ⇒ U2→U17
- [3,6,15]: (U3→U6 ; U6→U15) ⇒ U3→U15
- [3,7,9]: (U3→U7 ; U7→U9) ⇒ U3→U9
- [3,7,15]: (U3→U7 ; U7→U15) ⇒ U3→U15
- [3,9,15]: (U3→U9 ; U9→U15) ⇒ U3→U15
- [4,7,10]: (U4→U7 ; U7→U10) ⇒ U4→U10
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,13,16,17]
- [3,7,9,15]
- [4,8,13,17]
- [5,13,16,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 95 0-cells, 322 1-cells, 324 2-cells, 96 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,9}
- {0} → {0,11}
- {0} → {0,12}
- {0} → {0,9,12}
- {0} → {0,11,12}
- {1} → {1,10}
- {1} → {1,14}
- {1} → {1,10,14}
- {2} → {2,8}
- {2} → {2,13}
- {2} → {2,16}
- {2} → {2,17}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,61]: ({0}→{0,9} ; {0,9}→{0,9,12}) ⇒ {0}→{0,9,12}
- [0,19,62]: ({0}→{0,11} ; {0,11}→{0,11,12}) ⇒ {0}→{0,11,12}
- [0,20,61]: ({0}→{0,12} ; {0,12}→{0,9,12}) ⇒ {0}→{0,9,12}
- [0,20,62]: ({0}→{0,12} ; {0,12}→{0,11,12}) ⇒ {0}→{0,11,12}
- [1,21,63]: ({1}→{1,10} ; {1,10}→{1,10,14}) ⇒ {1}→{1,10,14}
- [1,22,63]: ({1}→{1,14} ; {1,14}→{1,10,14}) ⇒ {1}→{1,10,14}
- [2,23,64]: ({2}→{2,8} ; {2,8}→{2,8,17}) ⇒ {2}→{2,8,17}
- [2,24,65]: ({2}→{2,13} ; {2,13}→{2,13,16}) ⇒ {2}→{2,13,16}
- [2,24,66]: ({2}→{2,13} ; {2,13}→{2,13,17}) ⇒ {2}→{2,13,17}
- [2,24,91]: ({2}→{2,13} ; {2,13}→{2,13,16,17}) ⇒ {2}→{2,13,16,17}
- [2,25,65]: ({2}→{2,16} ; {2,16}→{2,13,16}) ⇒ {2}→{2,13,16}
- [2,25,67]: ({2}→{2,16} ; {2,16}→{2,16,17}) ⇒ {2}→{2,16,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,24,65,91]
- [2,24,66,91]
- [2,25,65,91]
- [2,25,67,91]
- [2,26,66,91]
- [2,26,67,91]
- [3,28,69,92]
- [3,28,70,92]
- [3,29,69,92]
- [3,29,71,92]
- [3,30,70,92]
- [3,30,71,92]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

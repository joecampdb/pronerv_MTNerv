# homotopy.io export: CATH domain 4a0tA01 (mdCATH), heavy atoms (`mdcath-4a0ta01-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 43 1-cells, 30 2-cells, 5 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U9
- U0 → U10
- U0 → U17
- U1 → U7
- U1 → U11
- U1 → U14
- U2 → U6
- U2 → U10
- U2 → U15
- U2 → U16
- U3 → U7
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,17]: (U0→U8 ; U8→U17) ⇒ U0→U17
- [0,10,17]: (U0→U10 ; U10→U17) ⇒ U0→U17
- [1,7,14]: (U1→U7 ; U7→U14) ⇒ U1→U14
- [1,11,14]: (U1→U11 ; U11→U14) ⇒ U1→U14
- [2,6,10]: (U2→U6 ; U6→U10) ⇒ U2→U10
- [2,6,16]: (U2→U6 ; U6→U16) ⇒ U2→U16
- [2,10,15]: (U2→U10 ; U10→U15) ⇒ U2→U15
- [2,10,16]: (U2→U10 ; U10→U16) ⇒ U2→U16
- [2,15,16]: (U2→U15 ; U15→U16) ⇒ U2→U16
- [3,7,12]: (U3→U7 ; U7→U12) ⇒ U3→U12
- [3,8,12]: (U3→U8 ; U8→U12) ⇒ U3→U12
- [3,8,13]: (U3→U8 ; U8→U13) ⇒ U3→U13
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,6,10,16]
- [2,10,15,16]
- [3,8,12,13]
- [4,8,12,17]
- [4,11,14,15]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 96 0-cells, 336 1-cells, 360 2-cells, 120 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,10}
- {0} → {0,17}
- {0} → {0,8,17}
- {0} → {0,10,17}
- {1} → {1,7}
- {1} → {1,11}
- {1} → {1,14}
- {1} → {1,7,14}
- {1} → {1,11,14}
- {2} → {2,6}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,61]: ({0}→{0,8} ; {0,8}→{0,8,17}) ⇒ {0}→{0,8,17}
- [0,20,62]: ({0}→{0,10} ; {0,10}→{0,10,17}) ⇒ {0}→{0,10,17}
- [0,21,61]: ({0}→{0,17} ; {0,17}→{0,8,17}) ⇒ {0}→{0,8,17}
- [0,21,62]: ({0}→{0,17} ; {0,17}→{0,10,17}) ⇒ {0}→{0,10,17}
- [1,22,63]: ({1}→{1,7} ; {1,7}→{1,7,14}) ⇒ {1}→{1,7,14}
- [1,23,64]: ({1}→{1,11} ; {1,11}→{1,11,14}) ⇒ {1}→{1,11,14}
- [1,24,63]: ({1}→{1,14} ; {1,14}→{1,7,14}) ⇒ {1}→{1,7,14}
- [1,24,64]: ({1}→{1,14} ; {1,14}→{1,11,14}) ⇒ {1}→{1,11,14}
- [2,25,65]: ({2}→{2,6} ; {2,6}→{2,6,10}) ⇒ {2}→{2,6,10}
- [2,25,66]: ({2}→{2,6} ; {2,6}→{2,6,16}) ⇒ {2}→{2,6,16}
- [2,25,91]: ({2}→{2,6} ; {2,6}→{2,6,10,16}) ⇒ {2}→{2,6,10,16}
- [2,26,65]: ({2}→{2,10} ; {2,10}→{2,6,10}) ⇒ {2}→{2,6,10}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,25,65,91]
- [2,25,66,91]
- [2,26,65,91]
- [2,26,67,92]
- [2,26,68,91]
- [2,26,68,92]
- [2,27,67,92]
- [2,27,69,92]
- [2,28,66,91]
- [2,28,68,91]
- [2,28,68,92]
- [2,28,69,92]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

# homotopy.io export: Chignolin CLN025 (128-run subset) (`cln025`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 42 1-cells, 24 2-cells, 1 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U10
- U0 → U12
- U0 → U15
- U1 → U6
- U1 → U11
- U1 → U13
- U1 → U17
- U2 → U8
- U2 → U9
- U2 → U14
- U2 → U16
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,15]: (U0→U7 ; U7→U15) ⇒ U0→U15
- [0,10,12]: (U0→U10 ; U10→U12) ⇒ U0→U12
- [1,6,17]: (U1→U6 ; U6→U17) ⇒ U1→U17
- [1,11,13]: (U1→U11 ; U11→U13) ⇒ U1→U13
- [1,11,17]: (U1→U11 ; U11→U17) ⇒ U1→U17
- [2,8,14]: (U2→U8 ; U8→U14) ⇒ U2→U14
- [2,9,16]: (U2→U9 ; U9→U16) ⇒ U2→U16
- [2,14,16]: (U2→U14 ; U14→U16) ⇒ U2→U16
- [3,7,15]: (U3→U7 ; U7→U15) ⇒ U3→U15
- [3,7,16]: (U3→U7 ; U7→U16) ⇒ U3→U16
- [3,9,16]: (U3→U9 ; U9→U16) ⇒ U3→U16
- [3,15,16]: (U3→U15 ; U15→U16) ⇒ U3→U16
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [3,7,15,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 85 0-cells, 242 1-cells, 180 2-cells, 24 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,10}
- {0} → {0,12}
- {0} → {0,15}
- {0} → {0,7,15}
- {0} → {0,10,12}
- {1} → {1,6}
- {1} → {1,11}
- {1} → {1,13}
- {1} → {1,17}
- {1} → {1,6,17}
- {1} → {1,11,13}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,60]: ({0}→{0,7} ; {0,7}→{0,7,15}) ⇒ {0}→{0,7,15}
- [0,19,61]: ({0}→{0,10} ; {0,10}→{0,10,12}) ⇒ {0}→{0,10,12}
- [0,20,61]: ({0}→{0,12} ; {0,12}→{0,10,12}) ⇒ {0}→{0,10,12}
- [0,21,60]: ({0}→{0,15} ; {0,15}→{0,7,15}) ⇒ {0}→{0,7,15}
- [1,22,62]: ({1}→{1,6} ; {1,6}→{1,6,17}) ⇒ {1}→{1,6,17}
- [1,23,63]: ({1}→{1,11} ; {1,11}→{1,11,13}) ⇒ {1}→{1,11,13}
- [1,23,64]: ({1}→{1,11} ; {1,11}→{1,11,17}) ⇒ {1}→{1,11,17}
- [1,24,63]: ({1}→{1,13} ; {1,13}→{1,11,13}) ⇒ {1}→{1,11,13}
- [1,25,62]: ({1}→{1,17} ; {1,17}→{1,6,17}) ⇒ {1}→{1,6,17}
- [1,25,64]: ({1}→{1,17} ; {1,17}→{1,11,17}) ⇒ {1}→{1,11,17}
- [2,26,65]: ({2}→{2,8} ; {2,8}→{2,8,14}) ⇒ {2}→{2,8,14}
- [2,27,66]: ({2}→{2,9} ; {2,9}→{2,9,16}) ⇒ {2}→{2,9,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [3,30,68,84]
- [3,30,69,84]
- [3,32,68,84]
- [3,32,71,84]
- [3,33,69,84]
- [3,33,71,84]
- [7,30,68,84]
- [7,30,69,84]
- [7,50,68,84]
- [7,50,83,84]
- [7,51,69,84]
- [7,51,83,84]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

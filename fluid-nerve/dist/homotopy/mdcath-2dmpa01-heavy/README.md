# homotopy.io export: CATH domain 2dmpA01 (mdCATH), heavy atoms (`mdcath-2dmpa01-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 45 1-cells, 32 2-cells, 4 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U9
- U0 → U11
- U0 → U12
- U0 → U15
- U1 → U10
- U1 → U14
- U2 → U6
- U2 → U13
- U3 → U6
- U3 → U7
- U3 → U8
- U3 → U16
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,9,12]: (U0→U9 ; U9→U12) ⇒ U0→U12
- [0,11,15]: (U0→U11 ; U11→U15) ⇒ U0→U15
- [0,12,15]: (U0→U12 ; U12→U15) ⇒ U0→U15
- [1,10,14]: (U1→U10 ; U10→U14) ⇒ U1→U14
- [2,6,13]: (U2→U6 ; U6→U13) ⇒ U2→U13
- [3,6,17]: (U3→U6 ; U6→U17) ⇒ U3→U17
- [3,7,16]: (U3→U7 ; U7→U16) ⇒ U3→U16
- [3,8,16]: (U3→U8 ; U8→U16) ⇒ U3→U16
- [3,8,17]: (U3→U8 ; U8→U17) ⇒ U3→U17
- [3,16,17]: (U3→U16 ; U16→U17) ⇒ U3→U17
- [4,7,14]: (U4→U7 ; U7→U14) ⇒ U4→U14
- [4,7,16]: (U4→U7 ; U7→U16) ⇒ U4→U16
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [3,8,16,17]
- [4,7,14,16]
- [4,8,15,16]
- [5,12,13,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 99 0-cells, 338 1-cells, 336 2-cells, 96 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,9}
- {0} → {0,11}
- {0} → {0,12}
- {0} → {0,15}
- {0} → {0,9,12}
- {0} → {0,11,15}
- {0} → {0,12,15}
- {1} → {1,10}
- {1} → {1,14}
- {1} → {1,10,14}
- {2} → {2,6}
- {2} → {2,13}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,63]: ({0}→{0,9} ; {0,9}→{0,9,12}) ⇒ {0}→{0,9,12}
- [0,19,64]: ({0}→{0,11} ; {0,11}→{0,11,15}) ⇒ {0}→{0,11,15}
- [0,20,63]: ({0}→{0,12} ; {0,12}→{0,9,12}) ⇒ {0}→{0,9,12}
- [0,20,65]: ({0}→{0,12} ; {0,12}→{0,12,15}) ⇒ {0}→{0,12,15}
- [0,21,64]: ({0}→{0,15} ; {0,15}→{0,11,15}) ⇒ {0}→{0,11,15}
- [0,21,65]: ({0}→{0,15} ; {0,15}→{0,12,15}) ⇒ {0}→{0,12,15}
- [1,22,66]: ({1}→{1,10} ; {1,10}→{1,10,14}) ⇒ {1}→{1,10,14}
- [1,23,66]: ({1}→{1,14} ; {1,14}→{1,10,14}) ⇒ {1}→{1,10,14}
- [2,24,67]: ({2}→{2,6} ; {2,6}→{2,6,13}) ⇒ {2}→{2,6,13}
- [2,25,67]: ({2}→{2,13} ; {2,13}→{2,6,13}) ⇒ {2}→{2,6,13}
- [3,26,68]: ({3}→{3,6} ; {3,6}→{3,6,17}) ⇒ {3}→{3,6,17}
- [3,27,69]: ({3}→{3,7} ; {3,7}→{3,7,16}) ⇒ {3}→{3,7,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [3,28,70,95]
- [3,28,71,95]
- [3,29,70,95]
- [3,29,72,95]
- [3,30,71,95]
- [3,30,72,95]
- [4,31,73,96]
- [4,31,74,96]
- [4,32,75,97]
- [4,32,76,97]
- [4,35,73,96]
- [4,35,80,96]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

# homotopy.io export: CATH domain 1wpbG01 (mdCATH), heavy atoms (`mdcath-1wpbg01-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 46 1-cells, 38 2-cells, 10 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U11
- U0 → U12
- U0 → U16
- U1 → U6
- U1 → U9
- U1 → U10
- U1 → U15
- U2 → U8
- U2 → U13
- U3 → U6
- U3 → U7
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,11]: (U0→U7 ; U7→U11) ⇒ U0→U11
- [0,7,12]: (U0→U7 ; U7→U12) ⇒ U0→U12
- [0,12,16]: (U0→U12 ; U12→U16) ⇒ U0→U16
- [1,6,9]: (U1→U6 ; U6→U9) ⇒ U1→U9
- [1,6,10]: (U1→U6 ; U6→U10) ⇒ U1→U10
- [1,6,15]: (U1→U6 ; U6→U15) ⇒ U1→U15
- [1,9,10]: (U1→U9 ; U9→U10) ⇒ U1→U10
- [1,9,15]: (U1→U9 ; U9→U15) ⇒ U1→U15
- [1,10,15]: (U1→U10 ; U10→U15) ⇒ U1→U15
- [2,8,13]: (U2→U8 ; U8→U13) ⇒ U2→U13
- [3,6,10]: (U3→U6 ; U6→U10) ⇒ U3→U10
- [3,6,17]: (U3→U6 ; U6→U17) ⇒ U3→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [1,6,9,10]
- [1,6,9,15]
- [1,6,10,15]
- [1,9,10,15]
- [3,6,10,17]
- [3,7,14,17]
- [5,8,13,14]
- [6,7,12,17]
- [6,9,10,15]
- [6,10,15,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 112 0-cells, 460 1-cells, 588 2-cells, 240 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,11}
- {0} → {0,12}
- {0} → {0,16}
- {0} → {0,7,11}
- {0} → {0,7,12}
- {0} → {0,12,16}
- {1} → {1,6}
- {1} → {1,9}
- {1} → {1,10}
- {1} → {1,15}
- {1} → {1,6,9}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,64]: ({0}→{0,7} ; {0,7}→{0,7,11}) ⇒ {0}→{0,7,11}
- [0,18,65]: ({0}→{0,7} ; {0,7}→{0,7,12}) ⇒ {0}→{0,7,12}
- [0,19,64]: ({0}→{0,11} ; {0,11}→{0,7,11}) ⇒ {0}→{0,7,11}
- [0,20,65]: ({0}→{0,12} ; {0,12}→{0,7,12}) ⇒ {0}→{0,7,12}
- [0,20,66]: ({0}→{0,12} ; {0,12}→{0,12,16}) ⇒ {0}→{0,12,16}
- [0,21,66]: ({0}→{0,16} ; {0,16}→{0,12,16}) ⇒ {0}→{0,12,16}
- [1,22,67]: ({1}→{1,6} ; {1,6}→{1,6,9}) ⇒ {1}→{1,6,9}
- [1,22,68]: ({1}→{1,6} ; {1,6}→{1,6,10}) ⇒ {1}→{1,6,10}
- [1,22,69]: ({1}→{1,6} ; {1,6}→{1,6,15}) ⇒ {1}→{1,6,15}
- [1,22,102]: ({1}→{1,6} ; {1,6}→{1,6,9,10}) ⇒ {1}→{1,6,9,10}
- [1,22,103]: ({1}→{1,6} ; {1,6}→{1,6,9,15}) ⇒ {1}→{1,6,9,15}
- [1,22,104]: ({1}→{1,6} ; {1,6}→{1,6,10,15}) ⇒ {1}→{1,6,10,15}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [1,22,67,102]
- [1,22,67,103]
- [1,22,68,102]
- [1,22,68,104]
- [1,22,69,103]
- [1,22,69,104]
- [1,23,67,102]
- [1,23,67,103]
- [1,23,70,102]
- [1,23,70,105]
- [1,23,71,103]
- [1,23,71,105]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

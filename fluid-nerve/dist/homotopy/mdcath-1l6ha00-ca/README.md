# homotopy.io export: CATH domain 1l6hA00 (mdCATH), C-alpha (`mdcath-1l6ha00-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 39 1-cells, 20 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U10
- U0 → U15
- U0 → U16
- U1 → U7
- U1 → U9
- U1 → U11
- U2 → U12
- U2 → U13
- U3 → U8
- U3 → U14
- U3 → U17
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,10]: (U0→U8 ; U8→U10) ⇒ U0→U10
- [0,10,15]: (U0→U10 ; U10→U15) ⇒ U0→U15
- [0,15,16]: (U0→U15 ; U15→U16) ⇒ U0→U16
- [1,7,11]: (U1→U7 ; U7→U11) ⇒ U1→U11
- [2,12,13]: (U2→U12 ; U12→U13) ⇒ U2→U13
- [3,8,17]: (U3→U8 ; U8→U17) ⇒ U3→U17
- [3,14,17]: (U3→U14 ; U14→U17) ⇒ U3→U17
- [4,7,11]: (U4→U7 ; U7→U11) ⇒ U4→U11
- [4,10,11]: (U4→U10 ; U10→U11) ⇒ U4→U11
- [4,10,15]: (U4→U10 ; U10→U15) ⇒ U4→U15
- [4,12,13]: (U4→U12 ; U12→U13) ⇒ U4→U13
- [4,12,15]: (U4→U12 ; U12→U15) ⇒ U4→U15
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 77 0-cells, 198 1-cells, 120 2-cells, 0 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,10}
- {0} → {0,15}
- {0} → {0,16}
- {0} → {0,8,10}
- {0} → {0,10,15}
- {0} → {0,15,16}
- {1} → {1,7}
- {1} → {1,9}
- {1} → {1,11}
- {1} → {1,7,11}
- {2} → {2,12}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,57]: ({0}→{0,8} ; {0,8}→{0,8,10}) ⇒ {0}→{0,8,10}
- [0,19,57]: ({0}→{0,10} ; {0,10}→{0,8,10}) ⇒ {0}→{0,8,10}
- [0,19,58]: ({0}→{0,10} ; {0,10}→{0,10,15}) ⇒ {0}→{0,10,15}
- [0,20,58]: ({0}→{0,15} ; {0,15}→{0,10,15}) ⇒ {0}→{0,10,15}
- [0,20,59]: ({0}→{0,15} ; {0,15}→{0,15,16}) ⇒ {0}→{0,15,16}
- [0,21,59]: ({0}→{0,16} ; {0,16}→{0,15,16}) ⇒ {0}→{0,15,16}
- [1,22,60]: ({1}→{1,7} ; {1,7}→{1,7,11}) ⇒ {1}→{1,7,11}
- [1,24,60]: ({1}→{1,11} ; {1,11}→{1,7,11}) ⇒ {1}→{1,7,11}
- [2,25,61]: ({2}→{2,12} ; {2,12}→{2,12,13}) ⇒ {2}→{2,12,13}
- [2,26,61]: ({2}→{2,13} ; {2,13}→{2,12,13}) ⇒ {2}→{2,12,13}
- [3,27,62]: ({3}→{3,8} ; {3,8}→{3,8,17}) ⇒ {3}→{3,8,17}
- [3,28,63]: ({3}→{3,14} ; {3,14}→{3,14,17}) ⇒ {3}→{3,14,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

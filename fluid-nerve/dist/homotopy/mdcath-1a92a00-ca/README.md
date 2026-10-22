# homotopy.io export: CATH domain 1a92A00 (mdCATH), C-alpha (`mdcath-1a92a00-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 43 1-cells, 28 2-cells, 2 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U8
- U0 → U9
- U0 → U11
- U0 → U14
- U1 → U10
- U1 → U12
- U2 → U7
- U2 → U9
- U2 → U13
- U2 → U17
- U3 → U8
- U3 → U10
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,8,11]: (U0→U8 ; U8→U11) ⇒ U0→U11
- [0,8,14]: (U0→U8 ; U8→U14) ⇒ U0→U14
- [0,9,14]: (U0→U9 ; U9→U14) ⇒ U0→U14
- [1,10,12]: (U1→U10 ; U10→U12) ⇒ U1→U12
- [2,7,13]: (U2→U7 ; U7→U13) ⇒ U2→U13
- [2,7,17]: (U2→U7 ; U7→U17) ⇒ U2→U17
- [2,9,17]: (U2→U9 ; U9→U17) ⇒ U2→U17
- [2,13,17]: (U2→U13 ; U13→U17) ⇒ U2→U17
- [3,8,16]: (U3→U8 ; U8→U16) ⇒ U3→U16
- [3,10,16]: (U3→U10 ; U10→U16) ⇒ U3→U16
- [4,7,13]: (U4→U7 ; U7→U13) ⇒ U4→U13
- [4,7,15]: (U4→U7 ; U7→U15) ⇒ U4→U15
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,7,13,17]
- [4,7,13,15]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 91 0-cells, 282 1-cells, 240 2-cells, 48 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,11}
- {0} → {0,14}
- {0} → {0,8,11}
- {0} → {0,8,14}
- {0} → {0,9,14}
- {1} → {1,10}
- {1} → {1,12}
- {1} → {1,10,12}
- {2} → {2,7}
- {2} → {2,9}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,61]: ({0}→{0,8} ; {0,8}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,18,62]: ({0}→{0,8} ; {0,8}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,19,63]: ({0}→{0,9} ; {0,9}→{0,9,14}) ⇒ {0}→{0,9,14}
- [0,20,61]: ({0}→{0,11} ; {0,11}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,21,62]: ({0}→{0,14} ; {0,14}→{0,8,14}) ⇒ {0}→{0,8,14}
- [0,21,63]: ({0}→{0,14} ; {0,14}→{0,9,14}) ⇒ {0}→{0,9,14}
- [1,22,64]: ({1}→{1,10} ; {1,10}→{1,10,12}) ⇒ {1}→{1,10,12}
- [1,23,64]: ({1}→{1,12} ; {1,12}→{1,10,12}) ⇒ {1}→{1,10,12}
- [2,24,65]: ({2}→{2,7} ; {2,7}→{2,7,13}) ⇒ {2}→{2,7,13}
- [2,24,66]: ({2}→{2,7} ; {2,7}→{2,7,17}) ⇒ {2}→{2,7,17}
- [2,24,89]: ({2}→{2,7} ; {2,7}→{2,7,13,17}) ⇒ {2}→{2,7,13,17}
- [2,25,67]: ({2}→{2,9} ; {2,9}→{2,9,17}) ⇒ {2}→{2,9,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [2,24,65,89]
- [2,24,66,89]
- [2,26,65,89]
- [2,26,68,89]
- [2,27,66,89]
- [2,27,68,89]
- [4,31,71,90]
- [4,31,72,90]
- [4,33,71,90]
- [4,33,74,90]
- [4,34,72,90]
- [4,34,74,90]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

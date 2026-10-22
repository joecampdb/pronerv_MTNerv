# homotopy.io export: CATH domain 1i5xA00 (mdCATH), heavy atoms (`mdcath-1i5xa00-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 44 1-cells, 32 2-cells, 8 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U11
- U0 → U13
- U0 → U14
- U0 → U15
- U1 → U6
- U1 → U8
- U1 → U16
- U1 → U17
- U2 → U9
- U2 → U10
- U2 → U12
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,13]: (U0→U7 ; U7→U13) ⇒ U0→U13
- [0,7,15]: (U0→U7 ; U7→U15) ⇒ U0→U15
- [0,11,14]: (U0→U11 ; U11→U14) ⇒ U0→U14
- [0,13,14]: (U0→U13 ; U13→U14) ⇒ U0→U14
- [1,6,16]: (U1→U6 ; U6→U16) ⇒ U1→U16
- [1,8,16]: (U1→U8 ; U8→U16) ⇒ U1→U16
- [1,8,17]: (U1→U8 ; U8→U17) ⇒ U1→U17
- [1,16,17]: (U1→U16 ; U16→U17) ⇒ U1→U17
- [2,9,10]: (U2→U9 ; U9→U10) ⇒ U2→U10
- [2,9,12]: (U2→U9 ; U9→U12) ⇒ U2→U12
- [3,9,10]: (U3→U9 ; U9→U10) ⇒ U3→U10
- [4,7,13]: (U4→U7 ; U7→U13) ⇒ U4→U13
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [1,8,16,17]
- [5,6,8,16]
- [5,6,8,17]
- [5,6,12,17]
- [5,6,16,17]
- [5,8,13,17]
- [5,8,16,17]
- [6,8,16,17]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 102 0-cells, 392 1-cells, 480 2-cells, 192 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,11}
- {0} → {0,13}
- {0} → {0,14}
- {0} → {0,15}
- {0} → {0,7,13}
- {0} → {0,7,15}
- {0} → {0,11,14}
- {0} → {0,13,14}
- {1} → {1,6}
- {1} → {1,8}
- {1} → {1,16}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,62]: ({0}→{0,7} ; {0,7}→{0,7,13}) ⇒ {0}→{0,7,13}
- [0,18,63]: ({0}→{0,7} ; {0,7}→{0,7,15}) ⇒ {0}→{0,7,15}
- [0,19,64]: ({0}→{0,11} ; {0,11}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,20,62]: ({0}→{0,13} ; {0,13}→{0,7,13}) ⇒ {0}→{0,7,13}
- [0,20,65]: ({0}→{0,13} ; {0,13}→{0,13,14}) ⇒ {0}→{0,13,14}
- [0,21,64]: ({0}→{0,14} ; {0,14}→{0,11,14}) ⇒ {0}→{0,11,14}
- [0,21,65]: ({0}→{0,14} ; {0,14}→{0,13,14}) ⇒ {0}→{0,13,14}
- [0,22,63]: ({0}→{0,15} ; {0,15}→{0,7,15}) ⇒ {0}→{0,7,15}
- [1,23,66]: ({1}→{1,6} ; {1,6}→{1,6,16}) ⇒ {1}→{1,6,16}
- [1,24,67]: ({1}→{1,8} ; {1,8}→{1,8,16}) ⇒ {1}→{1,8,16}
- [1,24,68]: ({1}→{1,8} ; {1,8}→{1,8,17}) ⇒ {1}→{1,8,17}
- [1,24,94]: ({1}→{1,8} ; {1,8}→{1,8,16,17}) ⇒ {1}→{1,8,16,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [1,24,67,94]
- [1,24,68,94]
- [1,25,67,94]
- [1,25,69,94]
- [1,26,68,94]
- [1,26,69,94]
- [5,37,75,95]
- [5,37,75,96]
- [5,37,76,97]
- [5,37,77,95]
- [5,37,77,98]
- [5,37,78,96]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

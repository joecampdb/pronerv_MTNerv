# homotopy.io export: CATH domain 1v1hF01 (mdCATH), C-alpha (`mdcath-1v1hf01-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 45 1-cells, 36 2-cells, 8 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U8
- U0 → U9
- U0 → U10
- U0 → U13
- U0 → U15
- U0 → U17
- U1 → U7
- U1 → U14
- U2 → U11
- U2 → U12
- U2 → U16
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,9]: (U0→U6 ; U6→U9) ⇒ U0→U9
- [0,6,10]: (U0→U6 ; U6→U10) ⇒ U0→U10
- [0,6,17]: (U0→U6 ; U6→U17) ⇒ U0→U17
- [0,8,13]: (U0→U8 ; U8→U13) ⇒ U0→U13
- [0,8,15]: (U0→U8 ; U8→U15) ⇒ U0→U15
- [0,9,13]: (U0→U9 ; U9→U13) ⇒ U0→U13
- [0,9,17]: (U0→U9 ; U9→U17) ⇒ U0→U17
- [0,10,15]: (U0→U10 ; U10→U15) ⇒ U0→U15
- [0,10,17]: (U0→U10 ; U10→U17) ⇒ U0→U17
- [0,13,15]: (U0→U13 ; U13→U15) ⇒ U0→U15
- [0,15,17]: (U0→U15 ; U15→U17) ⇒ U0→U17
- [1,7,14]: (U1→U7 ; U7→U14) ⇒ U1→U14
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,6,9,17]
- [0,6,10,17]
- [0,8,13,15]
- [0,10,15,17]
- [2,11,12,16]
- [3,6,11,16]
- [4,6,10,17]
- [4,6,12,16]

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 107 0-cells, 418 1-cells, 504 2-cells, 192 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,8}
- {0} → {0,9}
- {0} → {0,10}
- {0} → {0,13}
- {0} → {0,15}
- {0} → {0,17}
- {0} → {0,6,9}
- {0} → {0,6,10}
- {0} → {0,6,17}
- {0} → {0,8,13}
- {0} → {0,8,15}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,63]: ({0}→{0,6} ; {0,6}→{0,6,9}) ⇒ {0}→{0,6,9}
- [0,18,64]: ({0}→{0,6} ; {0,6}→{0,6,10}) ⇒ {0}→{0,6,10}
- [0,18,65]: ({0}→{0,6} ; {0,6}→{0,6,17}) ⇒ {0}→{0,6,17}
- [0,18,99]: ({0}→{0,6} ; {0,6}→{0,6,9,17}) ⇒ {0}→{0,6,9,17}
- [0,18,100]: ({0}→{0,6} ; {0,6}→{0,6,10,17}) ⇒ {0}→{0,6,10,17}
- [0,19,66]: ({0}→{0,8} ; {0,8}→{0,8,13}) ⇒ {0}→{0,8,13}
- [0,19,67]: ({0}→{0,8} ; {0,8}→{0,8,15}) ⇒ {0}→{0,8,15}
- [0,19,101]: ({0}→{0,8} ; {0,8}→{0,8,13,15}) ⇒ {0}→{0,8,13,15}
- [0,20,63]: ({0}→{0,9} ; {0,9}→{0,6,9}) ⇒ {0}→{0,6,9}
- [0,20,68]: ({0}→{0,9} ; {0,9}→{0,9,13}) ⇒ {0}→{0,9,13}
- [0,20,69]: ({0}→{0,9} ; {0,9}→{0,9,17}) ⇒ {0}→{0,9,17}
- [0,20,99]: ({0}→{0,9} ; {0,9}→{0,6,9,17}) ⇒ {0}→{0,6,9,17}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,63,99]
- [0,18,64,100]
- [0,18,65,99]
- [0,18,65,100]
- [0,19,66,101]
- [0,19,67,101]
- [0,20,63,99]
- [0,20,69,99]
- [0,21,64,100]
- [0,21,70,102]
- [0,21,71,100]
- [0,21,71,102]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

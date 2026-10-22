# homotopy.io export: CATH domain 2ckkA02 (mdCATH), C-alpha (`mdcath-2ckka02-ca`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 52 1-cells, 48 2-cells, 16 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U7
- U0 → U8
- U0 → U11
- U0 → U12
- U0 → U16
- U0 → U17
- U1 → U6
- U1 → U9
- U1 → U10
- U1 → U13
- U2 → U5
- U3 → U6
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,7,11]: (U0→U7 ; U7→U11) ⇒ U0→U11
- [0,7,16]: (U0→U7 ; U7→U16) ⇒ U0→U16
- [0,7,17]: (U0→U7 ; U7→U17) ⇒ U0→U17
- [0,8,11]: (U0→U8 ; U8→U11) ⇒ U0→U11
- [0,8,12]: (U0→U8 ; U8→U12) ⇒ U0→U12
- [0,8,17]: (U0→U8 ; U8→U17) ⇒ U0→U17
- [0,11,16]: (U0→U11 ; U11→U16) ⇒ U0→U16
- [0,11,17]: (U0→U11 ; U11→U17) ⇒ U0→U17
- [1,6,9]: (U1→U6 ; U6→U9) ⇒ U1→U9
- [1,6,13]: (U1→U6 ; U6→U13) ⇒ U1→U13
- [1,9,13]: (U1→U9 ; U9→U13) ⇒ U1→U13
- [1,10,13]: (U1→U10 ; U10→U13) ⇒ U1→U13
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,7,11,16]
- [0,7,11,17]
- [0,8,11,17]
- [1,6,9,13]
- [4,8,11,17]
- [4,10,13,17]
- [5,7,14,15]
- [6,7,11,15]
- [6,7,11,17]
- [6,7,15,17]
- [6,11,13,15]
- [6,11,13,17]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 134 0-cells, 616 1-cells, 864 2-cells, 384 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,7}
- {0} → {0,8}
- {0} → {0,11}
- {0} → {0,12}
- {0} → {0,16}
- {0} → {0,17}
- {0} → {0,7,11}
- {0} → {0,7,16}
- {0} → {0,7,17}
- {0} → {0,8,11}
- {0} → {0,8,12}
- {0} → {0,8,17}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,70]: ({0}→{0,7} ; {0,7}→{0,7,11}) ⇒ {0}→{0,7,11}
- [0,18,71]: ({0}→{0,7} ; {0,7}→{0,7,16}) ⇒ {0}→{0,7,16}
- [0,18,72]: ({0}→{0,7} ; {0,7}→{0,7,17}) ⇒ {0}→{0,7,17}
- [0,18,118]: ({0}→{0,7} ; {0,7}→{0,7,11,16}) ⇒ {0}→{0,7,11,16}
- [0,18,119]: ({0}→{0,7} ; {0,7}→{0,7,11,17}) ⇒ {0}→{0,7,11,17}
- [0,19,73]: ({0}→{0,8} ; {0,8}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,19,74]: ({0}→{0,8} ; {0,8}→{0,8,12}) ⇒ {0}→{0,8,12}
- [0,19,75]: ({0}→{0,8} ; {0,8}→{0,8,17}) ⇒ {0}→{0,8,17}
- [0,19,120]: ({0}→{0,8} ; {0,8}→{0,8,11,17}) ⇒ {0}→{0,8,11,17}
- [0,20,70]: ({0}→{0,11} ; {0,11}→{0,7,11}) ⇒ {0}→{0,7,11}
- [0,20,73]: ({0}→{0,11} ; {0,11}→{0,8,11}) ⇒ {0}→{0,8,11}
- [0,20,76]: ({0}→{0,11} ; {0,11}→{0,11,16}) ⇒ {0}→{0,11,16}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,70,118]
- [0,18,70,119]
- [0,18,71,118]
- [0,18,72,119]
- [0,19,73,120]
- [0,19,75,120]
- [0,20,70,118]
- [0,20,70,119]
- [0,20,73,120]
- [0,20,76,118]
- [0,20,77,119]
- [0,20,77,120]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

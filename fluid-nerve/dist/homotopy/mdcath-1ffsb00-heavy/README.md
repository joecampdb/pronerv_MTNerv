# homotopy.io export: CATH domain 1ffsB00 (mdCATH), heavy atoms (`mdcath-1ffsb00-heavy`)

Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).
Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.

## base: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 18 0-cells, 51 1-cells, 59 2-cells, 30 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: U0, U1, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11 …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- U0 → U6
- U0 → U7
- U0 → U8
- U0 → U15
- U0 → U16
- U0 → U17
- U1 → U5
- U1 → U11
- U1 → U14
- U2 → U9
- U3 → U5
- U3 → U6
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,6,7]: (U0→U6 ; U6→U7) ⇒ U0→U7
- [0,6,8]: (U0→U6 ; U6→U8) ⇒ U0→U8
- [0,6,15]: (U0→U6 ; U6→U15) ⇒ U0→U15
- [0,6,16]: (U0→U6 ; U6→U16) ⇒ U0→U16
- [0,6,17]: (U0→U6 ; U6→U17) ⇒ U0→U17
- [0,7,15]: (U0→U7 ; U7→U15) ⇒ U0→U15
- [0,7,17]: (U0→U7 ; U7→U17) ⇒ U0→U17
- [0,8,15]: (U0→U8 ; U8→U15) ⇒ U0→U15
- [0,8,16]: (U0→U8 ; U8→U16) ⇒ U0→U16
- [0,8,17]: (U0→U8 ; U8→U17) ⇒ U0→U17
- [0,15,16]: (U0→U15 ; U15→U16) ⇒ U0→U16
- [0,15,17]: (U0→U15 ; U15→U17) ⇒ U0→U17
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,6,7,15]
- [0,6,7,17]
- [0,6,8,15]
- [0,6,8,16]
- [0,6,15,16]
- [0,6,15,17]
- [0,7,15,17]
- [0,8,15,16]
- [0,8,15,17]
- [1,5,11,14]
- [3,6,10,16]
- [4,8,10,13]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

## poset: ok

### Click script (homotopy.io, https://beta.homotopy.io)

Signature size: 158 0-cells, 876 1-cells, 1434 2-cells, 720 3-cells.

**0-cells.** Press `A` (Add) once per vertex and rename: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11} …

**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:
- {0} → {0,6}
- {0} → {0,7}
- {0} → {0,8}
- {0} → {0,15}
- {0} → {0,16}
- {0} → {0,17}
- {0} → {0,6,7}
- {0} → {0,6,8}
- {0} → {0,6,15}
- {0} → {0,6,16}
- {0} → {0,6,17}
- {0} → {0,7,15}
- …

**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k (the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`.
- [0,18,69]: ({0}→{0,6} ; {0,6}→{0,6,7}) ⇒ {0}→{0,6,7}
- [0,18,70]: ({0}→{0,6} ; {0,6}→{0,6,8}) ⇒ {0}→{0,6,8}
- [0,18,71]: ({0}→{0,6} ; {0,6}→{0,6,15}) ⇒ {0}→{0,6,15}
- [0,18,72]: ({0}→{0,6} ; {0,6}→{0,6,16}) ⇒ {0}→{0,6,16}
- [0,18,73]: ({0}→{0,6} ; {0,6}→{0,6,17}) ⇒ {0}→{0,6,17}
- [0,18,128]: ({0}→{0,6} ; {0,6}→{0,6,7,15}) ⇒ {0}→{0,6,7,15}
- [0,18,129]: ({0}→{0,6} ; {0,6}→{0,6,7,17}) ⇒ {0}→{0,6,7,17}
- [0,18,130]: ({0}→{0,6} ; {0,6}→{0,6,8,15}) ⇒ {0}→{0,6,8,15}
- [0,18,131]: ({0}→{0,6} ; {0,6}→{0,6,8,16}) ⇒ {0}→{0,6,8,16}
- [0,18,132]: ({0}→{0,6} ; {0,6}→{0,6,15,16}) ⇒ {0}→{0,6,15,16}
- [0,18,133]: ({0}→{0,6} ; {0,6}→{0,6,15,17}) ⇒ {0}→{0,6,15,17}
- [0,19,69]: ({0}→{0,7} ; {0,7}→{0,6,7}) ⇒ {0}→{0,6,7}
- …

**3-cells.** For each tetrahedron [i,j,k,l]:
  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);
     click the top edge above the two strands and choose [i,k,l]; press `S`.
  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.
  The globularity check passes because both pastings run from i→j→k→l to i→l.
- [0,18,69,128]
- [0,18,69,129]
- [0,18,70,130]
- [0,18,70,131]
- [0,18,71,128]
- [0,18,71,130]
- [0,18,71,132]
- [0,18,71,133]
- [0,18,72,131]
- [0,18,72,132]
- [0,18,73,129]
- [0,18,73,133]
- …

To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ.

"""Encode a finite simplicial complex as a homotopy.io signature via Street's orientals.

Oriental encoding of an ordered simplicial complex K (vertices carry a total order):
  0-cells  vertices                      (cover sets U_i, or poset elements)
  1-cells  i -> j for each edge i<j      (U_i meets U_j; or an inclusion)
  2-cells  (ij ; jk) => ik  for each triangle i<j<k
  3-cells  for each tetrahedron i<j<k<l, from the pasting [ijk] then [ikl] (odd faces d3,d1)
           to the pasting [jkl] then [ijl] (even faces d0,d2); both run from ij;jk;kl to il.
The output is a list of simplified ops replayed by vendor/homotopy-rs/.../nerve_hom (see export_homotopy.py),
and a human-readable click script for building the same signature by hand in https://beta.homotopy.io.
"""
import json


def _name_vertex(v, labels):
    return labels[v] if labels else f"U{v}"


def oriental_ops(vertices, edges, triangles, tetrahedra, labels=None, title=None, author=None, abstr=None,
                 max_tetrahedra=None):
    ops = []
    if title:
        ops.append(dict(op="meta", title=title, author=author, abstr=abstr))
    gens = {}
    next_id = [0]

    def new(simplex, dim):
        gens[tuple(simplex)] = [next_id[0], dim]
        next_id[0] += 1
        return gens[tuple(simplex)]

    for v in vertices:
        ops.append(dict(op="zero", name=_name_vertex(v, labels)))
        new((v,), 0)
    for (i, j) in edges:
        ops += [dict(op="select", gen=gens[(i,)]), dict(op="source"),
                dict(op="select", gen=gens[(j,)]), dict(op="target", name=f"{_name_vertex(i, labels)}→{_name_vertex(j, labels)}")]
        new((i, j), 1)
    for (i, j, k) in triangles:
        ops += [dict(op="select", gen=gens[(i, j)]),
                dict(op="attach", gen=gens[(j, k)], boundary=["Target", 0], embedding=[]),
                dict(op="source"),
                dict(op="select", gen=gens[(i, k)]),
                dict(op="target", name=f"[{i},{j},{k}]")]
        new((i, j, k), 2)
    tets = list(tetrahedra)[: max_tetrahedra] if max_tetrahedra else list(tetrahedra)
    for (i, j, k, l) in tets:
        ops += [dict(op="select", gen=gens[(i, j, k)]),
                dict(op="attach", gen=gens[(k, l)], boundary=["Target", 1], embedding=[]),
                dict(op="attach", gen=gens[(i, k, l)], boundary=["Target", 0], embedding=[0]),
                dict(op="source"),
                dict(op="select", gen=gens[(j, k, l)]),
                dict(op="attach", gen=gens[(i, j)], boundary=["Source", 1], embedding=[]),
                dict(op="attach", gen=gens[(i, j, l)], boundary=["Target", 0], embedding=[0]),
                dict(op="target", name=f"[{i},{j},{k},{l}]")]
        new((i, j, k, l), 3)
    return ops, gens


def complex_from_nerve(nerve, kind="base"):
    """kind='base': the witnessed cover complex on cover indices (<= 18 vertices).
       kind='poset': the order complex of the face poset of the base 2-skeleton (what the atlas draws),
       with a linear extension by (dimension, lexicographic order)."""
    if kind == "base":
        faces = set()
        for m in nerve["maximal_simplices"]:
            m = sorted(m)
            for size in range(1, min(4, len(m)) + 1):
                from itertools import combinations
                faces.update(combinations(m, size))
        vertices = sorted(f[0] for f in faces if len(f) == 1)
        edges = sorted(f for f in faces if len(f) == 2)
        triangles = sorted(f for f in faces if len(f) == 3)
        tetra = sorted(f for f in faces if len(f) == 4)
        labels = None
        return vertices, edges, triangles, tetra, labels
    # Order complex of the face poset of the base complex restricted to faces of dimension <= 3,
    # so that chains v < e < t < tet become 3-cells. Linear extension: (dimension, lexicographic).
    from itertools import combinations
    faces = set()
    for m in nerve["maximal_simplices"]:
        m = sorted(m)
        for size in range(1, min(4, len(m)) + 1):
            faces.update(combinations(m, size))
    faces = sorted(faces, key=lambda f: (len(f), f))
    sets = [set(f) for f in faces]
    vertices = list(range(len(faces)))
    edges = [(i, j) for i, a in enumerate(sets) for j, b in enumerate(sets) if a < b]
    succ = {}
    for i, j in edges:
        succ.setdefault(i, []).append(j)
    triangles = sorted((i, j, k) for i, j in edges for k in succ.get(j, []))
    tetra = sorted((a, b, c, d) for a, b, c in triangles for d in succ.get(c, []))
    labels = {i: "{" + ",".join(map(str, f)) + "}" for i, f in enumerate(faces)}
    return vertices, edges, triangles, tetra, labels


def click_script(vertices, edges, triangles, tetrahedra, labels=None, limit=12):
    """Markdown instructions reproducing the signature by hand in homotopy.io (first `limit` items per level)."""
    L = lambda v: _name_vertex(v, labels)
    out = ["### Click script (homotopy.io, https://beta.homotopy.io)", "",
           f"Signature size: {len(vertices)} 0-cells, {len(edges)} 1-cells, {len(triangles)} 2-cells, {len(tetrahedra)} 3-cells.", "",
           "**0-cells.** Press `A` (Add) once per vertex and rename: " + ", ".join(L(v) for v in vertices[:limit]) + (" …" if len(vertices) > limit else ""), "",
           "**1-cells.** For each edge i→j: click i, press `S` (Source); click j, press `T` (Target). Edges:"]
    out += [f"- {L(i)} → {L(j)}" for i, j in edges[:limit]] + (["- …"] if len(edges) > limit else [])
    out += ["", "**2-cells.** For each triangle [i,j,k]: click the 1-cell i→j; click just above its top end and choose j→k "
            "(the tool offers only cells whose source matches); press `S`; click the 1-cell i→k; press `T`."]
    out += [f"- [{i},{j},{k}]: ({L(i)}→{L(j)} ; {L(j)}→{L(k)}) ⇒ {L(i)}→{L(k)}" for i, j, k in triangles[:limit]] + (["- …"] if len(triangles) > limit else [])
    out += ["", "**3-cells.** For each tetrahedron [i,j,k,l]:",
            "  1. click the 2-cell [i,j,k]; click the right edge of the diagram and choose k→l (whiskering);",
            "     click the top edge above the two strands and choose [i,k,l]; press `S`.",
            "  2. click the 2-cell [j,k,l]; click the left edge and choose i→j; click the top edge and choose [i,j,l]; press `T`.",
            "  The globularity check passes because both pastings run from i→j→k→l to i→l."]
    out += [f"- [{i},{j},{k},{l}]" for i, j, k, l in tetrahedra[:limit]] + (["- …"] if len(tetrahedra) > limit else [])
    out += ["", "To see a 3-cell as a 3D geometry: select it in the signature, then use the view controls (top-right) "
            "to raise the view dimension to 3 and orbit the rendering; `Image Export` (left toolbar) saves 2D slices as SVG/TikZ."]
    return "\n".join(out)


def write_ops(path, ops):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(ops, f, ensure_ascii=False)

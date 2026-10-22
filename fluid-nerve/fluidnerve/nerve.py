"""Witnessed ball covers of a 2D chart, maximal simplices, face-poset nerves and GF(2) Betti numbers.

The construction mirrors alanine-nerve/build_validated_atlas.py: greedy farthest-point centers among
occupied grid cells, fixed radius in a declared chart metric, membership of every frame (witnesses),
maximal simplices kept without truncation, display restricted to the 2-skeleton's face poset.
"""
import itertools
import numpy as np
from .geometry import wrap_delta


def chart_limits(q_all, period=None, pad=0.01):
    if period:
        return np.array([[-180., -180.], [180., 180.]])
    lo = q_all.min(0)
    hi = q_all.max(0)
    span = hi - lo
    return np.array([lo - pad * span, hi + pad * span])


def histogram(q_all, limits, bins):
    lo, hi = limits
    ij = np.clip(np.floor((q_all - lo) / (hi - lo) * bins).astype(int), 0, bins - 1)
    return np.bincount(ij[:, 0] * bins + ij[:, 1], minlength=bins * bins).reshape(bins, bins), ij


def chart_distance(a, b, scale, period):
    delta = a - b
    if period:
        delta = wrap_delta(delta, period)
    return np.linalg.norm(delta / scale, axis=-1)


def greedy_centers(q_all, limits, bins=30, n_centers=18, period=None, min_count=None):
    """Farthest-point centers among occupied grid-cell centres (deterministic)."""
    hist, _ = histogram(q_all, limits, bins)
    if min_count is None:
        min_count = max(10, int(round(len(q_all) / 30000)))
    lo, hi = limits
    occ = np.argwhere(hist >= min_count)
    if len(occ) == 0:
        occ = np.argwhere(hist > 0)
    cand = lo + (occ + .5) / bins * (hi - lo)
    counts = hist[occ[:, 0], occ[:, 1]]
    scale = np.ones(2) if period else q_all.std(0)
    ids = [int(np.argmax(counts))]
    while len(ids) < min(n_centers, len(cand)):
        d = chart_distance(cand[:, None], cand[ids][None], scale, period)
        ids.append(int(d.min(1).argmax()))
    return cand[ids], scale, dict(min_count=int(min_count), candidates=int(len(cand)))


def membership(q, centers, radius, scale, period=None):
    return chart_distance(q[:, None], np.asarray(centers)[None], np.asarray(scale), period) <= radius


def masks_from_membership(M):
    bits = (M.astype(np.uint64) << np.arange(M.shape[1], dtype=np.uint64)).sum(1, dtype=np.uint64)
    masks, counts = np.unique(bits, return_counts=True)
    return masks.astype(np.int64), counts, bits.astype(np.int64)


def maximal_masks(masks):
    kept = []
    for m in sorted((int(x) for x in set(map(int, masks)) if int(x) != 0), key=lambda x: (-bin(x).count("1"), x)):
        if not any(m & k == m for k in kept):
            kept.append(m)
    return kept


def faces_from_maximal(maximal, max_size=4):
    out = set()
    for mask in maximal:
        v = [i for i in range(int(mask).bit_length()) if mask & (1 << i)]
        for k in range(1, min(len(v), max_size) + 1):
            out.update(itertools.combinations(v, k))
    return sorted(out, key=lambda s: (len(s), s))


def gf2_rank(columns):
    """Rank over GF(2) of a matrix given as a list of Python-int bitsets (columns)."""
    rank = 0
    pivots = {}
    for col in columns:
        while col:
            low = col.bit_length() - 1
            if low in pivots:
                col ^= pivots[low]
            else:
                pivots[low] = col
                rank += 1
                break
    return rank


def betti_numbers(faces, max_dim=2):
    """GF(2) Betti numbers beta_0..beta_max_dim of a complex given by its faces up to size max_dim+2."""
    by_dim = {}
    for f in faces:
        by_dim.setdefault(len(f) - 1, []).append(tuple(f))
    ranks = {}
    for k in range(1, max_dim + 2):
        if k not in by_dim or (k - 1) not in by_dim:
            ranks[k] = 0
            continue
        index = {s: i for i, s in enumerate(by_dim[k - 1])}
        cols = [sum(1 << index[f] for f in itertools.combinations(s, k)) for s in by_dim[k]]
        ranks[k] = gf2_rank(cols)
    betti = [int(len(by_dim.get(k, [])) - ranks.get(k, 0) - ranks.get(k + 1, 0)) for k in range(max_dim + 1)]
    return betti, {k: len(v) for k, v in by_dim.items()}


def complex_from_bits(bits, max_size=4):
    masks = np.unique(bits)
    maximal = maximal_masks(masks)
    faces = faces_from_maximal(maximal, max_size)
    return maximal, faces


def build_nerve(q_all, limits, period=None, bins=30, n_centers=18, radius=None, witness_stride=1):
    """Complete witnessed cover complex and the displayed face-poset nerve (objects, inclusions, triangles)."""
    centers, scale, cinfo = greedy_centers(q_all, limits, bins, n_centers, period)
    if radius is None:
        radius = 55. if period else .8
    qw = q_all[::witness_stride]
    M = membership(qw, centers, radius, scale, period)
    masks, counts, bits = masks_from_membership(M)
    maximal = maximal_masks(masks)
    faces = faces_from_maximal(maximal, max_size=4)
    max_dim = max(bin(int(m)).count("1") for m in maximal) - 1
    betti, simplex_counts = betti_numbers(faces, max_dim=2)
    display = [f for f in faces if len(f) <= 3]
    sets = [set(f) for f in display]
    nodes = []
    for f in display:
        fm = sum(1 << i for i in f)
        sel = (bits & fm) == fm
        w = qw[sel]
        if period:
            ang = np.deg2rad(w)
            pos = np.rad2deg(np.arctan2(np.sin(ang).mean(0), np.cos(ang).mean(0)))
        else:
            pos = w.mean(0)
        nodes.append(dict(id=len(nodes), simplex=list(map(int, f)), witnesses=int(sel.sum()), chart=pos.tolist()))
    edges = [(i, j) for i, a in enumerate(sets) for j, b in enumerate(sets) if a < b]
    succ = {i: [] for i in range(len(nodes))}
    for i, j in edges:
        succ[i].append(j)
    chains = [(i, j, k) for i, j in edges for k in succ[j]]
    chains3 = sum(len(succ[k]) for _, _, k in chains)
    tetra = [f for f in faces if len(f) == 4]
    result = dict(centers=centers.tolist(), metric_scale=np.asarray(scale).tolist(), radius=float(radius), period=period,
                  bins=bins, candidate_info=cinfo, witness_stride=witness_stride,
                  maximal_simplices=[[i for i in range(int(m).bit_length()) if int(m) & (1 << i)] for m in maximal],
                  max_dimension=int(max_dim),
                  simplex_counts={str(k): int(v) for k, v in simplex_counts.items()},
                  betti_0_1_2=betti, uncovered_frames=int((bits == 0).sum()), witnessed_frames=int(len(bits)),
                  nodes=nodes, edges=[list(e) for e in edges], chains=[list(c) for c in chains], chains3=int(chains3),
                  tetrahedra=[list(t) for t in tetra],
                  display=dict(objects=len(nodes), inclusions=len(edges), triangles=len(chains)),
                  scope="Full-data witnessed complex in a projected 2D chart; maximal simplices preserved; the drawing "
                        "is the nerve of the face poset of the 2-skeleton. No configuration-space homotopy claim.")
    return result, M, bits


def radius_sensitivity(q_all, centers, scale, period, radii):
    rows = []
    for r in radii:
        M = membership(q_all, np.asarray(centers), r, np.asarray(scale), period)
        masks, _, _ = masks_from_membership(M)
        maximal = maximal_masks(masks)
        faces = faces_from_maximal(maximal, 4)
        betti, counts = betti_numbers(faces, 2)
        rows.append(dict(radius=float(r), betti_0_1_2=betti, simplices={str(k): int(v) for k, v in counts.items()},
                         max_dimension=int(max(bin(int(m)).count("1") for m in maximal) - 1)))
    return rows

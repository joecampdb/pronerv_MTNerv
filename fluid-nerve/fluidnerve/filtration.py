"""Ambient-time ("fluid") filtration of a witnessed cover and occupancy flooding filtration.

Fluid filtration.  For a cover U = {U_i} and ambient time tau, let W_i^tau be the set of frames that
lie within tau frames (in the same run) of a visit to U_i.  {W_i^tau} is a cover of the frame set that
grows monotonically with tau; its witnessed nerve N_tau is therefore a filtration of simplicial complexes
starting at the ordinary overlap nerve N_0.  We record Betti curves and persistence pairs (birth tau,
death tau) over GF(2).  Persistence in tau is an ambient-time scale of the cover geometry under the
recorded dynamics, not a rate constant.

Flooding filtration.  Sublevel sets {F <= c} of the smoothed negative log occupancy F on the chart grid,
analysed as a 2D cubical complex (periodic on a torus chart).  This is the geometric analogue of the
history-dependent filling performed by metadynamics; it is computed from the recorded occupancy only.
"""
import itertools
import numpy as np
from scipy.ndimage import maximum_filter1d, label, gaussian_filter
from .nerve import masks_from_membership, maximal_masks, faces_from_maximal, betti_numbers


def thickened_membership(M_runs, tau):
    if tau == 0:
        return M_runs
    return [maximum_filter1d(M.astype(np.uint8), size=2 * tau + 1, axis=0, mode="constant", cval=0).astype(bool)
            for M in M_runs]


def persistence_pairs(birth, max_dim=2):
    """Standard GF(2) column reduction. birth: dict simplex(tuple)->filtration index."""
    simplices = sorted(birth, key=lambda s: (birth[s], len(s), s))
    index = {s: i for i, s in enumerate(simplices)}
    pivots = {}
    lows = set()
    pivot_cols = set()
    pairs = {k: [] for k in range(max_dim + 1)}
    for s in simplices:
        if len(s) == 1:
            continue
        col = 0
        for f in itertools.combinations(s, len(s) - 1):
            col ^= 1 << index[f]
        while col:
            low = col.bit_length() - 1
            if low in pivots:
                col ^= pivots[low]
            else:
                pivots[low] = col
                lows.add(low)
                pivot_cols.add(index[s])
                dim = len(s) - 2
                if dim <= max_dim:
                    pairs[dim].append((int(birth[simplices[low]]), int(birth[s])))
                break
    for s in simplices:
        i = index[s]
        dim = len(s) - 1
        if dim <= max_dim and i not in pivot_cols and i not in lows:
            pairs[dim].append((int(birth[s]), None))
    return pairs


def fluid_filtration(M_runs, taus, max_dim=2, max_simplices=20000):
    """Betti curves and persistence of the time-thickened cover nerve over the lag ladder (tau=0 first)."""
    ladder = [0] + [int(t) for t in taus]
    birth = {}
    rows = []
    for ti, tau in enumerate(ladder):
        Mt = thickened_membership(M_runs, tau)
        bits = np.concatenate([masks_from_membership(M)[2] for M in Mt])
        masks = np.unique(bits)
        maximal = maximal_masks(masks)
        faces = faces_from_maximal(maximal, max_dim + 2)
        for f in faces:
            birth.setdefault(f, ti)
        betti, counts = betti_numbers(faces, max_dim)
        rows.append(dict(index=ti, tau_frames=tau, betti=betti,
                         simplices={str(k): int(v) for k, v in counts.items()},
                         max_dimension=int(max(bin(int(m)).count("1") for m in maximal) - 1),
                         maximal=len(maximal), uncovered=int((bits == 0).sum())))
        if len(birth) > max_simplices:
            break
    pairs = persistence_pairs(birth, max_dim)
    def to_tau(i):
        return None if i is None else ladder[i]
    pairs_tau = {str(k): [[to_tau(b), to_tau(d)] for b, d in v if b != d] for k, v in pairs.items()}
    first_connected = next((r["tau_frames"] for r in rows if r["betti"][0] == 1), None)
    total_persistence = {}
    for k, v in pairs.items():
        finite = [(ladder[d] - ladder[b]) for b, d in v if d is not None and b != d]
        total_persistence[str(k)] = dict(finite_classes=len(finite), essential=sum(1 for _, d in v if d is None),
                                         total_lifetime_frames=int(sum(finite)))
    return dict(ladder_frames=ladder, rows=rows, pairs=pairs_tau, first_connected_tau=first_connected,
                persistence_summary=total_persistence,
                meaning="Nerve of the cover thickened by +-tau frames along each run. Monotone in tau. GF(2).")


def _components(mask, period):
    lab, n = label(mask)
    if n == 0:
        return 0
    if not period:
        return int(n)
    parent = list(range(n + 1))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    rows, cols = mask.shape
    for j in range(cols):
        if mask[0, j] and mask[-1, j]:
            union(lab[0, j], lab[-1, j])
    for i in range(rows):
        if mask[i, 0] and mask[i, -1]:
            union(lab[i, 0], lab[i, -1])
    return len({find(a) for a in range(1, n + 1)})


def _euler_cubical(mask, period):
    rows, cols = mask.shape
    cells = np.argwhere(mask)
    verts, edges = set(), set()
    def v(i, j):
        return (i % rows, j % cols) if period else (i, j)
    for i, j in cells:
        c = [v(i, j), v(i + 1, j), v(i, j + 1), v(i + 1, j + 1)]
        verts.update(c)
        edges.update({frozenset((c[0], c[1])), frozenset((c[0], c[2])), frozenset((c[1], c[3])), frozenset((c[2], c[3]))})
    return len(verts) - len(edges) + len(cells)


def occupancy_landscape(q_all, limits, bins, period, sigma=0.85):
    lo, hi = np.asarray(limits[0]), np.asarray(limits[1])
    ij = np.clip(np.floor((q_all - lo) / (hi - lo) * bins).astype(int), 0, bins - 1)
    hist = np.bincount(ij[:, 0] * bins + ij[:, 1], minlength=bins * bins).reshape(bins, bins).astype(float)
    smooth = gaussian_filter(hist, sigma, mode="wrap" if period else "reflect")
    F = -np.log(np.maximum(smooth, 1e-12) / smooth.max())
    F[hist == 0] = np.inf  # never visited: never flooded
    return hist, F


def flooding_filtration(F, period, n_levels=40):
    finite = F[np.isfinite(F)]
    levels = np.linspace(0, float(finite.max()), n_levels)
    rows = []
    for c in levels:
        mask = F <= c
        b0 = _components(mask, period)
        chi = _euler_cubical(mask, period)
        b2 = 1 if (period and mask.all()) else 0
        b1 = b0 - chi + b2
        rows.append(dict(level=float(c), filled_fraction=float(mask.mean()), betti=[int(b0), int(b1), int(b2)]))
    # exact 0-dimensional persistence (basin merging) by union-find in increasing F
    cells = np.argwhere(np.isfinite(F))
    order = np.argsort(F[cells[:, 0], cells[:, 1]], kind="stable")
    parent = {}
    birth = {}
    pairs = []
    rows_n, cols_n = F.shape
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for k in order:
        i, j = map(int, cells[k])
        parent[(i, j)] = (i, j)
        birth[(i, j)] = float(F[i, j])
        nbrs = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        if period:
            nbrs = [(a % rows_n, b % cols_n) for a, b in nbrs]
        for nb in nbrs:
            if nb in parent:
                ra, rb = find((i, j)), find(nb)
                if ra != rb:
                    elder, younger = (ra, rb) if birth[ra] <= birth[rb] else (rb, ra)
                    pairs.append([birth[younger], float(F[i, j])])
                    parent[younger] = elder
    roots = {find(c) for c in parent}
    basins = sorted([[birth[r], None] for r in roots] + pairs, key=lambda p: (p[1] is not None, -(p[1] or 0) + p[0]))
    return dict(levels=levels.tolist(), rows=rows, basin_pairs=basins,
                meaning="Sublevel sets of smoothed -log occupancy on the chart grid; cubical GF(2) Betti numbers; "
                        "0-dim pairs are exact basin merge levels (elder rule). Not a free energy.")

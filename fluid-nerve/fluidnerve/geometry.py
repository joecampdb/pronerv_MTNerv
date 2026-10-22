"""Rigid alignment, pair distances, charts (phi/psi or PCA) and shape descriptors. Units: nm, degrees."""
import numpy as np


def center(frames):
    return frames - frames.mean(1, keepdims=True)


def kabsch_rotations(P, Q):
    """Rotations R (N,3,3) minimising ||P_n R - Q_n|| for centered P (N,K,3) and Q (N,K,3) or (K,3)."""
    if Q.ndim == 2:
        H = np.einsum("nki,kj->nij", P, Q)
    else:
        H = np.einsum("nki,nkj->nij", P, Q)
    U, _, Vt = np.linalg.svd(H)
    d = np.sign(np.linalg.det(U @ Vt))
    d[d == 0] = 1.0
    U = U.copy()
    U[:, :, 2] *= d[:, None]
    return U @ Vt


def align_to_reference(frames, iterations=2, reference=None):
    """Center and iteratively align frames (N,K,3) to a running mean structure. Returns aligned, reference."""
    X = center(np.asarray(frames, dtype=np.float64))
    ref = X[0] if reference is None else np.asarray(reference, dtype=np.float64)
    for _ in range(iterations):
        R = kabsch_rotations(X, ref)
        X = np.einsum("nki,nij->nkj", X, R)
        if reference is None:
            ref = X.mean(0)
    return X, ref


def align_pairs(A, B):
    """Align each B_n onto A_n (both centered) and return the aligned B."""
    R = kabsch_rotations(B, A)
    return np.einsum("nki,nij->nkj", B, R)


def pair_indices(k, max_pairs=None, seed=0):
    a, b = np.triu_indices(k, 1)
    if max_pairs is not None and len(a) > max_pairs:
        rng = np.random.default_rng(seed)
        sel = np.sort(rng.choice(len(a), max_pairs, replace=False))
        a, b = a[sel], b[sel]
    return a, b


def pair_distances(frames, pairs, chunk=20000):
    """Pair distances (N,P) in float32, computed in frame chunks to bound memory."""
    a, b = pairs
    out = np.empty((len(frames), len(a)), np.float32)
    for s in range(0, len(frames), chunk):
        f = frames[s:s + chunk]
        out[s:s + chunk] = np.linalg.norm(f[:, a] - f[:, b], axis=2)
    return out


def dihedral(p0, p1, p2, p3):
    """Dihedral angles in degrees for arrays (N,3)."""
    b0 = p0 - p1
    b1 = p2 - p1
    b2 = p3 - p2
    b1n = b1 / np.linalg.norm(b1, axis=1, keepdims=True)
    v = b0 - (b0 * b1n).sum(1, keepdims=True) * b1n
    w = b2 - (b2 * b1n).sum(1, keepdims=True) * b1n
    x = (v * w).sum(1)
    y = (np.cross(b1n, v) * w).sum(1)
    return np.degrees(np.arctan2(y, x))


def pca_chart(aligned_runs, n_components=2):
    """Shared 2D PCA chart of aligned coordinates pooled over runs. Returns (list of q per run, info)."""
    X = np.concatenate([r.reshape(len(r), -1) for r in aligned_runs]).astype(np.float64)
    mean = X.mean(0)
    Xc = X - mean
    cov = Xc.T @ Xc / max(len(Xc) - 1, 1)
    w, V = np.linalg.eigh(cov)
    order = np.argsort(w)[::-1]
    w, V = w[order], V[:, order]
    comps = V[:, :n_components]
    for c in range(n_components):  # deterministic sign
        j = np.argmax(np.abs(comps[:, c]))
        if comps[j, c] < 0:
            comps[:, c] *= -1
    qs = [((r.reshape(len(r), -1) - mean) @ comps) for r in aligned_runs]
    info = dict(explained=(w[:n_components] / w.sum()).tolist(), total_variance=float(w.sum()),
                components=comps.T.astype(np.float32), mean=mean.astype(np.float32))
    return qs, info


def radius_of_gyration(frames):
    c = center(frames)
    return np.sqrt((c ** 2).sum(2).mean(1))


def end_to_end(frames):
    return np.linalg.norm(frames[:, 0] - frames[:, -1], axis=1)


def wrap_delta(d, period):
    return (d + period / 2) % period - period / 2

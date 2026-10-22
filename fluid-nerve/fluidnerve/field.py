"""Deformation fields on a 2D chart at a ladder of ambient lags.

For every frame t and lag tau (in frames, within one run) we record
  * mobility  h  = RMS change of the site pair distances (rigid-invariant, nm)  -- the atlas height estimand,
  * drift     dq = q(t+tau) - q(t) in the chart (periodic difference on a torus),
  * spread    E[dq dq^T] - v v^T  (conditional covariance of the chart displacement),
  * site displacement u_k = x_k(t+tau) - x_k(t) after rigid alignment of frame t+tau onto frame t (nm).
Everything is binned by the chart position at time t. Blocks never synthesise pairs across block or run
boundaries. Support needs >=100 pairs, >=5 blocks and (if available) >=2 runs; unsupported bins are null.
Intervals are block-resampling spread, not calibrated confidence intervals.
"""
import numpy as np
from .geometry import wrap_delta, align_pairs


def lag_ladder(run_lengths, n_values=12, cap_fraction=0.25):
    cap = max(1, int(min(run_lengths) * cap_fraction))
    lad = np.unique(np.round(np.geomspace(1, cap, n_values)).astype(int))
    return [int(x) for x in lad if x >= 1]


def default_block_length(run_lengths, min_block=50, max_block=20000):
    """About ten blocks per run, clipped; lags used for the field must satisfy 4*tau <= block_length."""
    n = min(run_lengths)
    return int(np.clip(n // 10, min_block, max_block))


def field_at_lag(runs_q, runs_d, runs_x, tau, limits, bins, period, block_length,
                 site_displacement=True, bootstrap=200, seed=42, min_pairs=100, min_blocks=5):
    lo, hi = np.asarray(limits[0]), np.asarray(limits[1])
    B = bins * bins
    K = runs_x[0].shape[1] if (site_displacement and runs_x is not None) else 0
    counts, hs, s1, s2, runids = [], [], [], [], []
    su = np.zeros((B, K, 3), np.float64) if K else None
    for rid, (q, d) in enumerate(zip(runs_q, runs_d)):
        n = len(q)
        if n <= tau:
            continue
        dq = q[tau:] - q[:-tau]
        if period:
            dq = wrap_delta(dq, period)
        h = np.sqrt(np.mean((d[tau:] - d[:-tau]) ** 2, axis=1))
        if K:
            x = runs_x[rid]
            u = align_pairs(x[:-tau], x[tau:]) - x[:-tau]
        ij = np.floor((q[:-tau] - lo) / (hi - lo) * bins).astype(int)
        valid = ((ij >= 0) & (ij < bins)).all(1)
        idx = np.clip(ij, 0, bins - 1)
        idx = idx[:, 0] * bins + idx[:, 1]
        for start in range(0, n, block_length):
            end = min(start + block_length - tau, n - tau)
            if end <= start:
                continue
            ok = valid[start:end]
            ii = idx[start:end][ok]
            if len(ii) == 0:
                continue
            counts.append(np.bincount(ii, minlength=B))
            hs.append(np.bincount(ii, weights=h[start:end][ok], minlength=B))
            dd = dq[start:end][ok]
            s1.append(np.stack([np.bincount(ii, weights=dd[:, k], minlength=B) for k in range(2)], 1))
            s2.append(np.stack([np.bincount(ii, weights=dd[:, 0] ** 2, minlength=B),
                                np.bincount(ii, weights=dd[:, 0] * dd[:, 1], minlength=B),
                                np.bincount(ii, weights=dd[:, 1] ** 2, minlength=B)], 1))
            runids.append(rid)
            if K:
                np.add.at(su, ii, u[start:end][ok])
    if not counts:
        return None
    counts = np.array(counts)
    hs = np.array(hs)
    s1 = np.array(s1)
    s2 = np.array(s2)
    runids = np.array(runids)
    total = counts.sum(0)
    blocks_touching = (counts > 0).sum(0)
    runs_touching = np.array([len(np.unique(runids[counts[:, b] > 0])) for b in range(B)])
    n_runs = len(runs_q)
    support = (total >= min_pairs) & (blocks_touching >= min_blocks) & (runs_touching >= min(2, n_runs))
    with np.errstate(invalid="ignore", divide="ignore"):
        h_mean = np.where(total > 0, hs.sum(0) / total, np.nan)
        v = np.where(total[:, None] > 0, s1.sum(0) / total[:, None], np.nan)
        m2 = np.where(total[:, None] > 0, s2.sum(0) / total[:, None], np.nan)
    cov = np.stack([m2[:, 0] - v[:, 0] ** 2, m2[:, 1] - v[:, 0] * v[:, 1], m2[:, 2] - v[:, 1] ** 2], 1)
    cov[:, [0, 2]] = np.maximum(cov[:, [0, 2]], 0)
    u_mean = None
    if K:
        with np.errstate(invalid="ignore", divide="ignore"):
            u_mean = (su / total[:, None, None]).astype(np.float32)
        u_mean[~support] = np.nan
    interval = np.full((2, B), np.nan)
    if bootstrap and len(counts) > 1:
        rng = np.random.default_rng(seed)
        draws = np.empty((bootstrap, B))
        nb = len(counts)
        for r in range(bootstrap):
            pick = rng.integers(0, nb, nb)
            c = counts[pick].sum(0)
            with np.errstate(invalid="ignore", divide="ignore"):
                draws[r] = np.where(c > 0, hs[pick].sum(0) / c, np.nan)
        with np.errstate(all="ignore"):
            interval = np.nanpercentile(draws, [2.5, 97.5], axis=0)
    interval[:, ~support] = np.nan
    h_sup = np.where(support, h_mean, np.nan)
    speed = np.linalg.norm(np.where(support[:, None], v, np.nan), axis=1)
    spread = np.sqrt(np.where(support, cov[:, 0] + cov[:, 2], np.nan))
    with np.errstate(invalid="ignore", divide="ignore"):
        drift_ratio = speed / spread
    weights = np.where(support, total, 0).astype(float)
    wsum = weights.sum()
    summary = dict(tau_frames=int(tau), supported_bins=int(support.sum()), pairs=int(total.sum()),
                   blocks=int(len(counts)),
                   median_h=float(np.nanmedian(h_sup)) if support.any() else None,
                   weighted_mean_h=float((np.nan_to_num(h_sup) * weights).sum() / wsum) if wsum else None,
                   median_interval_width=float(np.nanmedian(interval[1] - interval[0])) if support.any() else None,
                   median_speed=float(np.nanmedian(speed)) if support.any() else None,
                   median_spread=float(np.nanmedian(spread)) if support.any() else None,
                   median_drift_ratio=float(np.nanmedian(drift_ratio)) if support.any() else None,
                   median_site_displacement=float(np.nanmedian(np.linalg.norm(u_mean, axis=2))) if K and support.any() else None)
    return dict(tau=int(tau), bins=bins, limits=np.asarray(limits).tolist(), period=period, block_length=int(block_length),
                count=total.reshape(bins, bins), support=support.reshape(bins, bins),
                h=h_mean.reshape(bins, bins), h_interval=interval.reshape(2, bins, bins),
                v=v.reshape(bins, bins, 2), cov=cov.reshape(bins, bins, 3),
                u=None if u_mean is None else u_mean.reshape(bins, bins, K, 3),
                blocks_touching=blocks_touching.reshape(bins, bins), runs_touching=runs_touching.reshape(bins, bins),
                summary=summary)


def mobility_scaling(summaries, clock_ps=None):
    """Log-log slope of median mobility against lag over the ladder (ballistic ~1, diffusive ~0.5, plateau ~0)."""
    taus = np.array([s["tau_frames"] for s in summaries if s.get("median_h")], float)
    hs = np.array([s["median_h"] for s in summaries if s.get("median_h")], float)
    if len(taus) < 3:
        return None
    if clock_ps:
        taus = taus * clock_ps
    A = np.vstack([np.log(taus), np.ones_like(taus)]).T
    slope, intercept = np.linalg.lstsq(A, np.log(hs), rcond=None)[0]
    half = len(taus) // 2
    s_early = np.linalg.lstsq(A[:max(half, 2)], np.log(hs[:max(half, 2)]), rcond=None)[0][0]
    s_late = np.linalg.lstsq(A[half:], np.log(hs[half:]), rcond=None)[0][0] if len(taus) - half >= 2 else None
    return dict(slope=float(slope), early_slope=float(s_early), late_slope=None if s_late is None else float(s_late),
                units="ps" if clock_ps else "frames", n=int(len(taus)))

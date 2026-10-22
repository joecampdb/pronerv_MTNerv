"""Build the deformation field, witnessed nerve, fluid (ambient-time) filtration and flooding filtration
for one catalog system.  Outputs go to dist/systems/<id>/ :
  summary.json      everything small: provenance, chart, lag ladder, field summaries, nerve, filtrations
  field.npz         per-lag grids (h, interval, support, count, drift v, covariance) and site displacement at tau_ref
  membership.npz    cover membership bits per frame (int64) and run lengths, for cross-representation comparison
  chart.npz         subsampled chart coordinates and occupancy histogram for plotting
Usage: python build_system.py <system-id> [--quick]
"""
import argparse
import json
import sys
import time
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fluidnerve import loaders, geometry as G, nerve as N, field as F, filtration as FL  # noqa: E402

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist/systems"
BINS = 30


def load_spec(spec):
    fn = dict(ala2=loaders.load_ala2, dipeptide=loaders.load_dipeptide, sgdml=loaders.load_sgdml,
              mdcath=loaders.load_mdcath, cln025=loaders.load_cln025)[spec["loader"]]
    return fn(**spec.get("args", {}))


def clean(o):
    if isinstance(o, dict):
        return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, np.ndarray):
        return clean(o.tolist())
    if isinstance(o, (np.floating, float)):
        return None if not np.isfinite(o) else float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return o


def build(spec, quick=False, out_root=DIST):
    t0 = time.time()
    out = out_root / spec["id"]
    out.mkdir(parents=True, exist_ok=True)
    loaded = load_spec(spec)
    runs = loaded["runs"]
    if quick:
        runs = [r[: min(len(r), 20000)] for r in runs[:6]]
        chart_pre = None if loaded["chart"] is None else [c[: len(r)] for c, r in zip(loaded["chart"], runs)]
    else:
        chart_pre = loaded["chart"]
    lengths = [len(r) for r in runs]
    K = runs[0].shape[1]
    pooled = np.concatenate(runs)
    aligned, ref = G.align_to_reference(pooled)
    aligned = aligned.astype(np.float32)
    bounds = np.cumsum([0] + lengths)
    aligned_runs = [aligned[bounds[i]:bounds[i + 1]] for i in range(len(runs))]
    max_pairs = 4000 if K > 100 else None
    pairs = G.pair_indices(K, max_pairs=max_pairs)
    d_runs = [G.pair_distances(x, pairs).astype(np.float32) for x in aligned_runs]
    if chart_pre is not None:
        q_runs = [np.asarray(c, dtype=np.float64) for c in chart_pre]
        period = 360.0
        chart_info = dict(kind="phi/psi (degrees)", periodic=True)
    else:
        q_runs, pca = G.pca_chart(aligned_runs)
        period = None
        chart_info = dict(kind="PCA-2 of aligned site coordinates (nm)", periodic=False,
                          explained_variance=pca["explained"], total_variance_nm2=pca["total_variance"])
    q_all = np.concatenate(q_runs)
    limits = N.chart_limits(q_all, period)
    ladder = F.lag_ladder(lengths)                       # ambient-time ladder for the fluid filtration
    block = F.default_block_length(lengths)
    tau_max_field = max(1, block // 4)                    # pairs must fit inside resampling blocks
    tau_ref = min(int(spec.get("tau_ref", ladder[len(ladder) // 2])), tau_max_field)
    all_taus = sorted({t for t in ladder if t <= tau_max_field} | {tau_ref})
    site_disp = K <= 200
    # Field grid resolution follows the data volume (about 150 frames per bin at full resolution) so that the
    # support rule (>=100 pairs, >=5 blocks, >=2 runs) is attainable for small deposits; the nerve candidate grid
    # and the flooding grid stay at 30x30 as in the measured atlas.
    field_bins = int(np.clip(np.sqrt(sum(lengths) / 150.0), 10, BINS))
    fields = {}
    for tau in all_taus:
        fld = F.field_at_lag(q_runs, d_runs, aligned_runs if site_disp else None, tau, limits, field_bins, period, block,
                             site_displacement=site_disp and tau == tau_ref, bootstrap=100 if quick else 200)
        if fld is not None:
            fields[tau] = fld
    field_summaries = [fields[t]["summary"] for t in all_taus if t in fields]
    scaling = F.mobility_scaling(field_summaries, loaded["clock_ps"])
    nerve, M, bits = N.build_nerve(q_all, limits, period, BINS)
    sens = N.radius_sensitivity(q_all, nerve["centers"], nerve["metric_scale"], period,
                                [nerve["radius"] * f for f in (0.75, 1.0, 1.25, 1.5)])
    # attach height at tau_ref to nerve nodes
    hgrid = fields[tau_ref]["h"]
    sup = fields[tau_ref]["support"]
    lo, hi = limits
    for node in nerve["nodes"]:
        b = np.floor((np.array(node["chart"]) - lo) / (hi - lo) * field_bins).astype(int)
        inside = bool(((b >= 0) & (b < field_bins)).all())
        b = np.clip(b, 0, field_bins - 1)
        node["supported"] = bool(inside and sup[b[0], b[1]])
        node["height_nm"] = float(hgrid[b[0], b[1]]) if node["supported"] else None
    M_runs = [M[bounds[i]:bounds[i + 1]] for i in range(len(runs))]
    # Membership flip rates: fraction of within-run frame pairs (t, t+tau) whose cover-membership vector differs.
    # Small values at tau = 1 mean consecutive frames are first-order close relative to the cover (rigidity regime).
    def flip_rate(tau):
        num = sum(int((Mr[tau:] != Mr[:-tau]).any(1).sum()) for Mr in M_runs if len(Mr) > tau)
        den = sum(max(len(Mr) - tau, 0) for Mr in M_runs)
        return float(num / den) if den else None
    flips = {int(t): flip_rate(int(t)) for t in sorted({1, tau_ref} | set(ladder[:6]))}
    fluid = FL.fluid_filtration(M_runs, ladder)
    hist, Fgrid = FL.occupancy_landscape(q_all, limits, BINS, period)
    flood = FL.flooding_filtration(Fgrid, period)
    # Temperature ladder (mdCATH): nerve/field/filtration restricted to each temperature, same chart and cover.
    temp_ladder = None
    temps = sorted({m.get("temperature") for m in loaded["run_meta"] if m.get("temperature") is not None})
    if len(temps) > 1:
        temp_ladder = []
        for T in temps:
            ids = [i for i, m in enumerate(loaded["run_meta"]) if i < len(runs) and m.get("temperature") == T]
            if not ids:
                continue
            qs = [q_runs[i] for i in ids]
            bitsT = np.concatenate([masks_bits for masks_bits in [N.masks_from_membership(M_runs[i])[2] for i in ids]])
            maximal, faces = N.complex_from_bits(bitsT)
            betti, counts = N.betti_numbers(faces, 2)
            fT = F.field_at_lag(qs, [d_runs[i] for i in ids], None, tau_ref, limits, field_bins, period, block,
                                site_displacement=False, bootstrap=0)
            flT = FL.fluid_filtration([M_runs[i] for i in ids], ladder)
            temp_ladder.append(dict(temperature=T, runs=len(ids), frames=int(sum(lengths[i] for i in ids)),
                                    betti_0_1_2=betti, simplices={str(k): int(v) for k, v in counts.items()},
                                    max_dimension=int(max(bin(int(m)).count("1") for m in maximal) - 1),
                                    field=None if fT is None else fT["summary"],
                                    first_connected_tau=flT["first_connected_tau"],
                                    fluid_rows=[dict(tau_frames=r["tau_frames"], betti=r["betti"]) for r in flT["rows"]]))
    summary = dict(id=spec["id"], group=spec["group"], label=spec["label"], representation=spec["representation"],
                   family=spec.get("family"), paired_with=spec.get("paired_with"),
                   provenance=loaded["info"], run_meta=loaded["run_meta"], quick=quick,
                   frames=int(sum(lengths)), runs=len(runs), run_lengths=lengths, sites=len(loaded["sites"]),
                   site_labels=loaded["sites"] if len(loaded["sites"]) <= 400 else loaded["sites"][:400] + ["..."],
                   pairs_used=int(len(pairs[0])), pair_subsampled=bool(max_pairs is not None),
                   clock_ps_per_frame=loaded["clock_ps"], chart=chart_info, limits=limits.tolist(), bins=BINS, field_bins=field_bins,
                   lag_ladder_frames=ladder, field_lags_frames=all_taus, tau_ref_frames=tau_ref, block_length_frames=block,
                   field=dict(summaries=field_summaries, mobility_scaling=scaling,
                              meaning="h: RMS change of site pair distances over the lag (nm); v: mean chart displacement; "
                                      "cov: conditional covariance of chart displacement; u: mean rigid-aligned site displacement."),
                   nerve={k: v for k, v in nerve.items() if k not in ("nodes", "edges", "chains", "tetrahedra")},
                   nerve_display_counts=dict(objects=len(nerve["nodes"]), inclusions=len(nerve["edges"]),
                                             triangles=len(nerve["chains"]), length3_chains=nerve["chains3"],
                                             base_tetrahedra=len(nerve["tetrahedra"])),
                   radius_sensitivity=sens, membership_flip_rate=flips, fluid_filtration=fluid, flooding=flood,
                   temperature_ladder=temp_ladder,
                   seconds=round(time.time() - t0, 1))
    (out / "summary.json").write_text(json.dumps(clean(summary), indent=1))
    (out / "nerve.json").write_text(json.dumps(clean(dict(nodes=nerve["nodes"], edges=nerve["edges"], chains=nerve["chains"],
                                                            tetrahedra=nerve["tetrahedra"], maximal_simplices=nerve["maximal_simplices"],
                                                            centers=nerve["centers"], radius=nerve["radius"],
                                                            metric_scale=nerve["metric_scale"], period=period))))
    np.savez_compressed(out / "field.npz", taus=np.array(all_taus),
                        h=np.stack([fields[t]["h"] for t in all_taus]).astype(np.float32),
                        h_interval=np.stack([fields[t]["h_interval"] for t in all_taus]).astype(np.float32),
                        support=np.stack([fields[t]["support"] for t in all_taus]),
                        count=np.stack([fields[t]["count"] for t in all_taus]).astype(np.int32),
                        v=np.stack([fields[t]["v"] for t in all_taus]).astype(np.float32),
                        cov=np.stack([fields[t]["cov"] for t in all_taus]).astype(np.float32),
                        u_ref=np.zeros((0,)) if fields[tau_ref]["u"] is None else fields[tau_ref]["u"],
                        tau_ref=tau_ref, limits=limits, occupancy=hist, free=np.where(np.isfinite(Fgrid), Fgrid, np.nan),
                        reference_structure=ref.astype(np.float32))
    np.savez_compressed(out / "membership.npz", bits=bits.astype(np.int64), lengths=np.array(lengths),
                        centers=np.array(nerve["centers"]), radius=nerve["radius"])
    # Representative recorded conformations: nearest frame to each cover centre and to the occupancy peak.
    centers = np.array(nerve["centers"])
    scale = np.array(nerve["metric_scale"])
    rep_idx = []
    for c in centers:
        rep_idx.append(int(np.argmin(N.chart_distance(q_all, c, scale, period))))
    peak = np.unravel_index(np.argmax(hist), hist.shape)
    peak_pos = lo + (np.array(peak) + .5) / BINS * (hi - lo)
    rep_idx.append(int(np.argmin(N.chart_distance(q_all, peak_pos, scale, period))))
    rep_idx = np.array(rep_idx)
    rep_bins = np.clip(np.floor((q_all[rep_idx] - lo) / (hi - lo) * field_bins).astype(int), 0, field_bins - 1)
    np.savez_compressed(out / "representatives.npz", frame=rep_idx, coords=aligned[rep_idx].astype(np.float32),
                        chart=q_all[rep_idx].astype(np.float32), field_bin=rep_bins,
                        labels=np.array([f"U{i}" for i in range(len(centers))] + ["peak"]),
                        site_labels=np.array(loaded["sites"]))
    stride = max(1, len(q_all) // 60000)
    np.savez_compressed(out / "chart.npz", q=q_all[::stride].astype(np.float32), stride=stride,
                        run_id=np.repeat(np.arange(len(runs)), lengths)[::stride].astype(np.int16))
    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--catalog", default=str(ROOT / "catalog/systems.json"))
    args = ap.parse_args()
    catalog = json.loads(Path(args.catalog).read_text())["systems"]
    specs = [s for s in catalog if not args.ids or s["id"] in args.ids]
    for spec in specs:
        s = build(spec, quick=args.quick)
        print(spec["id"], "frames", s["frames"], "nerve", s["nerve_display_counts"], "betti", s["nerve"]["betti_0_1_2"],
              "first_connected_tau", s["fluid_filtration"]["first_connected_tau"], f"{s['seconds']}s", flush=True)


if __name__ == "__main__":
    main()

"""Comparative analysis within and between the atom-based and backbone-based groups.

Reads dist/systems/*/summary.json (+ membership.npz for paired representations) and writes dist/comparison/:
  invariants.csv / invariants.json      one row per system (nerve, field, fluid and flooding invariants)
  group_tests.json                      medians per group, Mann-Whitney U, Cliff's delta (descriptive; n is small
                                        and systems are not independent draws)
  distances.json                        standardized invariant distances, hierarchical clustering, MDS coordinates
  comparison_functor.json               atomistic -> C-alpha face-poset comparison on shared frames (mdCATH pairs)
  temperature_ladder.json               mdCATH nerve/field invariants against temperature
  figures: fig_embedding.png fig_invariants.png fig_betti_curves.png fig_scaling.png fig_functor.png fig_temperature.png
"""
import csv
import itertools
import json
import sys
from pathlib import Path
import numpy as np
from scipy.stats import mannwhitneyu, spearmanr
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fluidnerve.nerve import faces_from_maximal  # noqa: E402

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist/systems"
OUT = ROOT / "dist/comparison"
INK, INK2, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#fcfcfb"
GROUP = dict(atom="#2a78d6", backbone="#eb6834", paired="#1baf7a")
plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Segoe UI", "DejaVu Sans"], "font.size": 9,
                     "axes.edgecolor": "#c3c2b7", "axes.labelcolor": INK2, "xtick.color": MUTED, "ytick.color": MUTED,
                     "axes.titlecolor": INK, "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
                     "axes.spines.top": False, "axes.spines.right": False})

INVARIANTS = [  # (key, label, log-transform for distances)
    ("objects", "nerve objects", True), ("inclusions", "inclusions", True), ("triangles", "triangles", True),
    ("max_dimension", "max simplex dim", False), ("beta0", "β0 (cover)", False), ("beta1", "β1 (cover)", False),
    ("beta2", "β2 (cover)", False), ("uncovered_fraction", "uncovered fraction", False),
    ("median_h_ref", "median h at τ_ref (nm)", True), ("drift_ratio_ref", "drift/spread at τ_ref", False),
    ("h_slope", "mobility exponent", False), ("h_slope_early", "early mobility exponent", False),
    ("first_connected_frames", "τ_connect (frames)", True), ("beta1_total_lifetime_frames", "β1 total lifetime (frames)", True),
    ("beta1_classes", "β1 classes born (fluid)", False), ("flood_basins", "flooding basins (persistence ≥ 1)", False),
    ("flood_connect_level", "flooding connection level", False), ("entropy_bits", "occupancy entropy (bits)", False),
    ("connect_radius_factor", "cover-radius factor at which β0 = 1", False),
    ("flip_rate_1", "membership flip rate at τ = 1 frame", False),
]


def load_all():
    rows = []
    for p in sorted(DIST.iterdir()):
        f = p / "summary.json"
        if not f.exists():
            continue
        S = json.loads(f.read_text())
        if S.get("quick"):
            continue
        rows.append(S)
    return rows


def invariants(S):
    nd = S["nerve_display_counts"]
    nv = S["nerve"]
    tau_ref = S["tau_ref_frames"]
    fs = next((s for s in S["field"]["summaries"] if s["tau_frames"] == tau_ref), None)
    sc = S["field"].get("mobility_scaling") or {}
    fl = S["fluid_filtration"]
    fd = S["flooding"]
    basins = [p for p in fd["basin_pairs"] if p[1] is None or p[1] - p[0] >= 1.0]
    connect_level = next((r["level"] for r in fd["rows"] if r["betti"][0] == 1 and r["filled_fraction"] > 0), None)
    clock = S["clock_ps_per_frame"]
    fc = fl["first_connected_tau"]
    base_r = nv["radius"]
    crf = next((round(r["radius"] / base_r, 2) for r in S["radius_sensitivity"] if r["betti_0_1_2"][0] == 1), None)
    occ = None
    try:
        z = np.load(DIST / S["id"] / "field.npz")
        o = z["occupancy"].astype(float).ravel()
        pr = o[o > 0] / o.sum()
        occ = float(-(pr * np.log2(pr)).sum())
    except Exception:
        pass
    return dict(id=S["id"], group=S["group"], family=S.get("family"), label=S["label"], paired_with=S.get("paired_with"),
                frames=S["frames"], runs=S["runs"], sites=S["sites"], clock_ps=clock, tau_ref=tau_ref,
                objects=nd["objects"], inclusions=nd["inclusions"], triangles=nd["triangles"], base_tetrahedra=nd["base_tetrahedra"],
                max_dimension=nv["max_dimension"], beta0=nv["betti_0_1_2"][0], beta1=nv["betti_0_1_2"][1], beta2=nv["betti_0_1_2"][2],
                uncovered_fraction=nv["uncovered_frames"] / max(nv["witnessed_frames"], 1),
                median_h_ref=None if fs is None else fs["median_h"], drift_ratio_ref=None if fs is None else fs["median_drift_ratio"],
                speed_ref=None if fs is None else fs["median_speed"], supported_bins_ref=None if fs is None else fs["supported_bins"],
                h_slope=sc.get("slope"), h_slope_early=sc.get("early_slope"), h_slope_late=sc.get("late_slope"),
                first_connected_frames=fc, first_connected_ps=None if (fc is None or clock is None) else fc * clock,
                beta1_total_lifetime_frames=fl["persistence_summary"]["1"]["total_lifetime_frames"],
                beta1_classes=fl["persistence_summary"]["1"]["finite_classes"] + fl["persistence_summary"]["1"]["essential"],
                flood_basins=len(basins), flood_connect_level=connect_level, entropy_bits=occ, connect_radius_factor=crf,
                flip_rate_1=(S.get("membership_flip_rate") or {}).get("1"),
                flip_rate_ref=(S.get("membership_flip_rate") or {}).get(str(tau_ref)),
                chart_periodic=S["chart"]["periodic"], chart_explained=S["chart"].get("explained_variance"))


def cliffs_delta(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    gt = (a[:, None] > b[None]).sum(); lt = (a[:, None] < b[None]).sum()
    return float((gt - lt) / (len(a) * len(b)))


def group_tests(inv):
    res = {}
    for key, label, _ in INVARIANTS:
        a = [r[key] for r in inv if r["group"] == "atom" and r[key] is not None]
        b = [r[key] for r in inv if r["group"] == "backbone" and r[key] is not None]
        entry = dict(label=label, n_atom=len(a), n_backbone=len(b),
                     median_atom=float(np.median(a)) if a else None, median_backbone=float(np.median(b)) if b else None,
                     iqr_atom=[float(np.percentile(a, 25)), float(np.percentile(a, 75))] if a else None,
                     iqr_backbone=[float(np.percentile(b, 25)), float(np.percentile(b, 75))] if b else None)
        if len(a) >= 3 and len(b) >= 3:
            try:
                u = mannwhitneyu(a, b, alternative="two-sided")
                entry.update(mannwhitney_U=float(u.statistic), p_value=float(u.pvalue), cliffs_delta=cliffs_delta(a, b))
            except ValueError:
                pass
        res[key] = entry
    return res


def distance_analysis(inv):
    keys = [k for k, _, _ in INVARIANTS]
    logs = {k: lg for k, _, lg in INVARIANTS}
    rows = [r for r in inv if r["group"] in ("atom", "backbone")]
    X = np.array([[np.nan if r[k] is None else (np.log10(r[k] + 1e-9) if logs[k] else r[k]) for k in keys] for r in rows], float)
    mu = np.nanmean(X, 0); sd = np.nanstd(X, 0); sd[sd == 0] = 1
    Z = (X - mu) / sd
    Z = np.where(np.isnan(Z), 0, Z)
    D = np.sqrt(((Z[:, None] - Z[None]) ** 2).sum(2))
    # MDS (classical) in 2D
    n = len(rows)
    J = np.eye(n) - 1 / n
    B = -0.5 * J @ (D ** 2) @ J
    w, V = np.linalg.eigh(B)
    order = np.argsort(w)[::-1]
    coords = V[:, order[:2]] * np.sqrt(np.maximum(w[order[:2]], 0))
    link = linkage(Z, "average")
    clusters = fcluster(link, 2, "maxclust")
    ids = [r["id"] for r in rows]
    within = {g: float(np.mean([D[i, j] for i, j in itertools.combinations([k for k, r in enumerate(rows) if r["group"] == g], 2)]))
              for g in ("atom", "backbone") if sum(r["group"] == g for r in rows) > 1}
    between = float(np.mean([D[i, j] for i, r in enumerate(rows) for j, s in enumerate(rows) if r["group"] == "atom" and s["group"] == "backbone"])) if within else None
    # permutation test for between/within separation
    labels = np.array([r["group"] for r in rows])
    def stat(lab):
        wa = D[np.ix_(lab == "atom", lab == "atom")]; wb = D[np.ix_(lab == "backbone", lab == "backbone")]
        bt = D[np.ix_(lab == "atom", lab == "backbone")]
        w = (wa.sum() + wb.sum()) / max((lab == "atom").sum() * ((lab == "atom").sum() - 1) + (lab == "backbone").sum() * ((lab == "backbone").sum() - 1), 1)
        return bt.mean() / w if w > 0 else 0
    rng = np.random.default_rng(0)
    obs = stat(labels)
    perms = [stat(rng.permutation(labels)) for _ in range(2000)]
    p_perm = float((np.sum(np.array(perms) >= obs) + 1) / (len(perms) + 1))
    return dict(ids=ids, groups=labels.tolist(), families=[r["family"] for r in rows], keys=keys, mds=coords.tolist(),
                clusters=clusters.tolist(), mean_within=within, mean_between=between, separation_ratio=float(obs),
                permutation_p=p_perm, dendrogram=dendrogram(link, no_plot=True, labels=ids)["ivl"],
                note="Euclidean distance on z-scored (log where marked) invariants; classical MDS; average linkage. Descriptive only.")


def comparison_functor(inv):
    pairs = [(r["id"], r["paired_with"]) for r in inv if r["group"] == "paired" and r.get("paired_with")]
    results = []
    for heavy_id, ca_id in pairs:
        if not (DIST / ca_id / "membership.npz").exists():
            continue
        A = np.load(DIST / heavy_id / "membership.npz"); B = np.load(DIST / ca_id / "membership.npz")
        ba, bb = A["bits"], B["bits"]
        if len(ba) != len(bb):
            continue
        na = json.loads((DIST / heavy_id / "nerve.json").read_text()); nb = json.loads((DIST / ca_id / "nerve.json").read_text())
        fa = faces_from_maximal([sum(1 << i for i in m) for m in na["maximal_simplices"]], 4)
        fb = faces_from_maximal([sum(1 << i for i in m) for m in nb["maximal_simplices"]], 4)
        def witness_matrix(bits, faces):
            W = np.zeros((len(faces), len(bits)), bool)
            for k, f in enumerate(faces):
                fm = sum(1 << i for i in f)
                W[k] = (bits & fm) == fm
            return W
        Wa = witness_matrix(ba, fa); Wb = witness_matrix(bb, fb)
        inter = Wa.astype(np.int32) @ Wb.astype(np.int32).T
        union = Wa.sum(1)[:, None] + Wb.sum(1)[None] - inter
        with np.errstate(invalid="ignore", divide="ignore"):
            J = np.where(union > 0, inter / union, 0)
        def rates(J, faces_src, faces_dst):
            f = J.argmax(1); best = J.max(1)
            sets_src = [set(x) for x in faces_src]; sets_dst = [set(x) for x in faces_dst]
            incl = [(i, j) for i, a in enumerate(sets_src) for j, b in enumerate(sets_src) if a < b]
            kept = [sets_dst[f[i]] <= sets_dst[f[j]] for i, j in incl]
            strict = [sets_dst[f[i]] < sets_dst[f[j]] for i, j in incl]
            succ = {}
            for i, j in incl:
                succ.setdefault(i, []).append(j)
            comp = [(i, j, k) for i, j in incl for k in succ.get(j, [])]
            comp_kept = [sets_dst[f[i]] <= sets_dst[f[j]] <= sets_dst[f[k]] for i, j, k in comp]
            return dict(faces=len(faces_src), median_best_jaccard=float(np.median(best)), fraction_jaccard_over_half=float(np.mean(best > .5)),
                        inclusions=len(incl), inclusion_preserved_lax=float(np.mean(kept)) if kept else None,
                        inclusion_preserved_strict=float(np.mean(strict)) if strict else None,
                        composable_pairs=len(comp), composition_preserved_lax=float(np.mean(comp_kept)) if comp_kept else None,
                        image_faces=int(len(set(f.tolist()))))
        vertJ = J[:len(na["centers"]), :len(nb["centers"])] if False else None
        results.append(dict(heavy=heavy_id, ca=ca_id, frames=int(len(ba)),
                            heavy_to_ca=rates(J, fa, fb), ca_to_heavy=rates(J.T, fb, fa),
                            note="f(σ) = C-alpha face with maximal witness-set Jaccard. Lax preservation allows equal images (identities). "
                                 "This is an empirical comparison of two face posets on identical frames, not a proved functor."))
    summary = {}
    for direction in ("heavy_to_ca", "ca_to_heavy"):
        for key in ("inclusion_preserved_lax", "inclusion_preserved_strict", "composition_preserved_lax", "median_best_jaccard"):
            vals = [r[direction][key] for r in results if r[direction][key] is not None]
            summary[f"{direction}.{key}"] = dict(median=float(np.median(vals)) if vals else None, min=float(np.min(vals)) if vals else None,
                                                 max=float(np.max(vals)) if vals else None, n=len(vals))
    return dict(pairs=results, summary=summary)


def temperature_ladder(rows):
    out = []
    for S in rows:
        tl = S.get("temperature_ladder")
        if not tl or S["group"] != "backbone":
            continue
        out.append(dict(id=S["id"], ladder=[dict(T=t["temperature"], beta=t["betti_0_1_2"], max_dimension=t["max_dimension"],
                                                 simplices=t["simplices"], median_h=(t["field"] or {}).get("median_h"),
                                                 drift_ratio=(t["field"] or {}).get("median_drift_ratio"),
                                                 first_connected_tau=t["first_connected_tau"]) for t in tl]))
    return out


def fig_embedding(dist):
    fig, ax = plt.subplots(figsize=(6.4, 5.2))
    xy = np.array(dist["mds"])
    for g in ("atom", "backbone"):
        sel = np.array(dist["groups"]) == g
        ax.scatter(xy[sel, 0], xy[sel, 1], s=42, facecolor=GROUP[g], edgecolor=SURFACE, linewidth=1.2, label=f"{g}-based", zorder=3)
    fam_seen = set()
    for (x, y), fam, sid in zip(xy, dist["families"], dist["ids"]):
        tag = fam if fam not in ("dipeptide", "mdcath") else sid.split("-")[1][:7]
        ax.annotate(tag, (x, y), textcoords="offset points", xytext=(4, 3), fontsize=6, color=INK2)
    ax.axhline(0, color=GRID, lw=0.6); ax.axvline(0, color=GRID, lw=0.6)
    ax.set_xlabel("MDS 1 (z-scored invariants)"); ax.set_ylabel("MDS 2")
    ax.set_title(f"Systems embedded by nerve + field invariants\nbetween/within distance ratio {dist['separation_ratio']:.2f}, permutation p = {dist['permutation_p']:.3f}", loc="left")
    ax.legend(frameon=False, loc="best")
    fig.tight_layout(); fig.savefig(OUT / "fig_embedding.png", dpi=170); plt.close(fig)


def fig_invariants(inv, tests):
    keys = ["objects", "beta1", "median_h_ref", "h_slope", "first_connected_frames", "flood_basins"]
    fig, axes = plt.subplots(2, 3, figsize=(9.6, 5.6))
    rng = np.random.default_rng(1)
    for ax, key in zip(axes.ravel(), keys):
        label = dict(INVARIANTS_LABEL)[key]
        for gi, g in enumerate(("atom", "backbone")):
            vals = [r[key] for r in inv if r["group"] == g and r[key] is not None]
            x = gi + rng.uniform(-.16, .16, len(vals))
            ax.scatter(x, vals, s=22, facecolor=GROUP[g], edgecolor=SURFACE, linewidth=0.8, zorder=3)
            if vals:
                ax.hlines(np.median(vals), gi - .28, gi + .28, color=INK, lw=1.6, zorder=4)
        t = tests[key]
        p = t.get("p_value")
        ax.set_title(label + ("" if p is None else f"\nMann–Whitney p = {p:.3f}, Cliff's δ = {t['cliffs_delta']:+.2f}"), loc="left", fontsize=8.5)
        ax.set_xticks([0, 1]); ax.set_xticklabels(["atom-based", "backbone-based"])
        if key in ("objects", "median_h_ref"):
            ax.set_yscale("log")
        elif key == "first_connected_frames":
            ax.set_yscale("symlog", linthresh=1.0)
        ax.grid(True, axis="y", color=GRID, lw=0.5)
    fig.suptitle("Invariant distributions by group (bars: medians; descriptive, systems are not independent samples)", x=0.02, ha="left", fontsize=9.5, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.95)); fig.savefig(OUT / "fig_invariants.png", dpi=170); plt.close(fig)


def fig_betti_curves(rows):
    """Absolute Betti curves of the fluid filtration against ambient time (frames), one line per system."""
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 6.6))
    for row, g in zip(axes, ("atom", "backbone")):
        for S in rows:
            if S["group"] != g:
                continue
            fl = S["fluid_filtration"]["rows"]
            t = np.maximum(np.array([r["tau_frames"] for r in fl], float), 0.5)
            for ax, k in zip(row, (0, 1)):
                ax.step(t, [r["betti"][k] for r in fl], where="post", color=GROUP[g], lw=1.0, alpha=0.55)
        for ax, k in zip(row, (0, 1)):
            ax.set_xscale("log")
            ax.set_xlabel("ambient time τ (frames; τ = 0 drawn at 0.5)")
            ax.set_ylabel(f"β{'₀' if k == 0 else '₁'}(N_τ)")
            ax.set_title(f"{g}-based: {'components' if k == 0 else 'loops'} of the τ-thickened cover nerve", loc="left", fontsize=9)
            ax.grid(True, color=GRID, lw=0.5)
    fig.tight_layout(); fig.savefig(OUT / "fig_betti_curves.png", dpi=170); plt.close(fig)


def fig_scaling(rows):
    fig, ax = plt.subplots(figsize=(6.4, 4.6))
    for S in rows:
        if S["group"] not in ("atom", "backbone") or not S["clock_ps_per_frame"]:
            continue
        xs = [s["tau_frames"] * S["clock_ps_per_frame"] for s in S["field"]["summaries"] if s.get("median_h")]
        ys = [s["median_h"] for s in S["field"]["summaries"] if s.get("median_h")]
        ax.plot(xs, ys, color=GROUP[S["group"]], lw=1.1, alpha=0.65)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel("ambient lag τ (ps)"); ax.set_ylabel("median mobility h(τ) over supported bins (nm)")
    ax.set_title("Mobility against ambient lag (blue: atom-based, orange: backbone-based)\nslopes near 1 = ballistic, 0.5 = diffusive, 0 = saturated", loc="left")
    ax.grid(True, color=GRID, lw=0.5)
    fig.tight_layout(); fig.savefig(OUT / "fig_scaling.png", dpi=170); plt.close(fig)


def fig_functor(cf):
    pairs = cf["pairs"]
    if not pairs:
        return
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.6))
    rng = np.random.default_rng(3)
    panels = [("inclusion_preserved_lax", "inclusions preserved (lax)"), ("composition_preserved_lax", "composable pairs preserved (lax)"),
              ("median_best_jaccard", "median witness-set Jaccard")]
    for ax, (key, label) in zip(axes, panels):
        for gi, (direction, col) in enumerate((("heavy_to_ca", GROUP["paired"]), ("ca_to_heavy", GROUP["backbone"]))):
            vals = [p[direction][key] for p in pairs if p[direction][key] is not None]
            x = gi + rng.uniform(-.16, .16, len(vals))
            ax.scatter(x, vals, s=20, facecolor=col, edgecolor=SURFACE, linewidth=0.8, zorder=3)
            if vals:
                ax.hlines(np.median(vals), gi - .28, gi + .28, color=INK, lw=1.6, zorder=4)
        ax.set_xticks([0, 1]); ax.set_xticklabels(["heavy → Cα", "Cα → heavy"])
        ax.set_ylim(0, 1.02); ax.set_title(label, loc="left", fontsize=9)
        ax.grid(True, axis="y", color=GRID, lw=0.5)
    fig.suptitle(f"Face-poset comparison on shared frames, {len(pairs)} mdCATH domains (bars: medians)", x=0.02, ha="left", fontsize=9.5, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.93)); fig.savefig(OUT / "fig_functor.png", dpi=170); plt.close(fig)


def fig_temperature(tl):
    if not tl:
        return
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.6))
    for d in tl:
        T = [r["T"] for r in d["ladder"]]
        axes[0].plot(T, [r["beta"][0] for r in d["ladder"]], color=GROUP["backbone"], lw=1, alpha=0.5, marker="o", ms=3)
        axes[1].plot(T, [r["median_h"] or np.nan for r in d["ladder"]], color=GROUP["backbone"], lw=1, alpha=0.5, marker="o", ms=3)
        axes[2].plot(T, [r["simplices"].get("2", 0) for r in d["ladder"]], color=GROUP["backbone"], lw=1, alpha=0.5, marker="o", ms=3)
    axes[0].set_ylabel("β₀ of the per-temperature witnessed cover"); axes[1].set_ylabel("median h at τ_ref (nm)"); axes[2].set_ylabel("triangles witnessed")
    for ax in axes:
        ax.set_xlabel("temperature (K)"); ax.grid(True, color=GRID, lw=0.5)
    fig.suptitle("mdCATH temperature ladder (same chart and cover per domain; one line per domain)", x=0.02, ha="left", fontsize=9.5, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.93)); fig.savefig(OUT / "fig_temperature.png", dpi=170); plt.close(fig)


INVARIANTS_LABEL = [(k, l) for k, l, _ in INVARIANTS]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = load_all()
    inv = [invariants(S) for S in rows]
    with open(OUT / "invariants.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(inv[0].keys()))
        w.writeheader(); w.writerows(inv)
    (OUT / "invariants.json").write_text(json.dumps(inv, indent=1))
    tests = group_tests(inv)
    (OUT / "group_tests.json").write_text(json.dumps(tests, indent=1))
    dist = distance_analysis(inv)
    (OUT / "distances.json").write_text(json.dumps(dist, indent=1))
    cf = comparison_functor(inv)
    (OUT / "comparison_functor.json").write_text(json.dumps(cf, indent=1))
    tl = temperature_ladder(rows)
    (OUT / "temperature_ladder.json").write_text(json.dumps(tl, indent=1))
    # correlations across all primary systems
    prim = [r for r in inv if r["group"] in ("atom", "backbone")]
    corr = {}
    for a, b in [("median_h_ref", "first_connected_frames"), ("drift_ratio_ref", "first_connected_frames"), ("objects", "entropy_bits"),
                 ("h_slope", "first_connected_ps"), ("beta1", "flood_basins"), ("sites", "objects"),
                 ("h_slope_early", "flip_rate_1"), ("h_slope", "flip_rate_1")]:
        pairs = [(r[a], r[b]) for r in prim if r[a] is not None and r[b] is not None]
        if len(pairs) >= 4:
            rho = spearmanr(*zip(*pairs))
            corr[f"{a}~{b}"] = dict(n=len(pairs), spearman_rho=float(rho.statistic), p=float(rho.pvalue))
    (OUT / "correlations.json").write_text(json.dumps(corr, indent=1))
    fig_embedding(dist); fig_invariants(inv, tests); fig_betti_curves(rows); fig_scaling(rows); fig_functor(cf); fig_temperature(tl)
    counts = {g: sum(r["group"] == g for r in inv) for g in ("atom", "backbone", "paired")}
    (OUT / "overview.json").write_text(json.dumps(dict(systems=len(inv), groups=counts, separation=dict(ratio=dist["separation_ratio"], permutation_p=dist["permutation_p"]),
                                                      functor_summary=cf["summary"], correlations=corr), indent=1))
    print(json.dumps(dict(systems=len(inv), groups=counts, separation_ratio=round(dist["separation_ratio"], 3), permutation_p=dist["permutation_p"]), indent=1))


if __name__ == "__main__":
    main()

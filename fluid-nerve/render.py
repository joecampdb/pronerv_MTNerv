"""Per-system figure: occupancy landscape with the face-poset nerve, the mobility/drift field at the reference lag,
the ambient-time (fluid) Betti curves and the flooding Betti curves. Writes dist/systems/<id>/figure.png.
Palette: single-hue sequential ramps, three fixed categorical slots (atom=blue, backbone=orange, paired=aqua)."""
import json
import sys
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from matplotlib.patches import Ellipse

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist/systems"
INK, INK2, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#fcfcfb"
GROUP = dict(atom="#2a78d6", backbone="#eb6834", paired="#1baf7a")
BLUES = ListedColormap(["#f4f8fd", "#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5",
                        "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b"], name="blues13")
ORANGES = LinearSegmentedColormap.from_list("orange1", ["#fdf1ea", "#f7c4ab", "#f29a72", "#eb6834", "#b94417", "#7a2a0e"])
plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Segoe UI", "DejaVu Sans"], "font.size": 9,
                     "axes.edgecolor": "#c3c2b7", "axes.labelcolor": INK2, "xtick.color": MUTED, "ytick.color": MUTED,
                     "axes.titlecolor": INK, "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
                     "axes.spines.top": False, "axes.spines.right": False, "axes.grid": False})


def fmt(x, spec=".3g", none="n/a"):
    return none if x is None else format(x, spec)


def time_label(frames, clock_ps):
    if clock_ps is None:
        return f"{frames} frames"
    ps = frames * clock_ps
    if ps < 1:
        return f"{ps * 1000:.3g} fs"
    if ps < 1000:
        return f"{ps:.3g} ps"
    if ps < 1e6:
        return f"{ps / 1000:.3g} ns"
    return f"{ps / 1e6:.3g} µs"


def render(sid, show_u=False):
    out = DIST / sid
    S = json.loads((out / "summary.json").read_text())
    nerve = json.loads((out / "nerve.json").read_text())
    fld = np.load(out / "field.npz", allow_pickle=True)
    lo, hi = np.array(S["limits"])
    bins = S["bins"]
    period = S["chart"]["periodic"]
    clock = S["clock_ps_per_frame"]
    tau_ref = int(fld["tau_ref"])
    taus = list(fld["taus"])
    k = taus.index(tau_ref)
    extent = [lo[0], hi[0], lo[1], hi[1]]
    color = GROUP.get(S["group"], INK)
    fig, axes = plt.subplots(2, 2, figsize=(10.5, 8.6))
    fig.subplots_adjust(hspace=0.45, wspace=0.30, top=0.82, bottom=0.07, left=0.07, right=0.95)

    # (a) occupancy + nerve
    ax = axes[0, 0]
    occ = fld["occupancy"].astype(float)
    dens = occ / occ.max()
    ax.imshow(dens.T, origin="lower", extent=extent, cmap=BLUES, vmin=0, vmax=1, aspect="auto", interpolation="nearest")
    pos = np.array([n["chart"] for n in nerve["nodes"]])
    for i, j in nerve["edges"]:
        a, b = pos[i], pos[j]
        if period and np.abs(a - b).max() > 180:
            continue
        ax.plot([a[0], b[0]], [a[1], b[1]], color=INK2, lw=0.35, alpha=0.55, solid_capstyle="round")
    dims = np.array([len(n["simplex"]) for n in nerve["nodes"]])
    for d, ms in ((1, 14), (2, 8), (3, 4)):
        sel = dims == d
        if sel.any():
            ax.scatter(pos[sel, 0], pos[sel, 1], s=ms, facecolor=SURFACE, edgecolor=INK, linewidth=0.6, zorder=5)
    scale = np.array(nerve["metric_scale"])
    for c in nerve["centers"]:
        ax.add_patch(Ellipse(c, 2 * nerve["radius"] * scale[0], 2 * nerve["radius"] * scale[1], fill=False,
                             edgecolor=color, lw=0.5, alpha=0.6))
    ax.set_xlim(lo[0], hi[0]); ax.set_ylim(lo[1], hi[1])
    nd = S["nerve_display_counts"]
    ax.set_title(f"(a) occupancy, {len(nerve['centers'])} cover balls, face-poset nerve\n"
                 f"{nd['objects']} objects · {nd['inclusions']} inclusions · {nd['triangles']} triangles · "
                 f"β = {S['nerve']['betti_0_1_2']}", loc="left", fontsize=9)
    ax.set_xlabel("chart axis 1" + (" (φ, °)" if period else " (PC1, nm)"))
    ax.set_ylabel("chart axis 2" + (" (ψ, °)" if period else " (PC2, nm)"))

    # (b) mobility + drift
    ax = axes[0, 1]
    h = fld["h"][k].astype(float)
    sup = fld["support"][k]
    h = np.where(sup, h, np.nan)
    im = ax.imshow(h.T, origin="lower", extent=extent, cmap=ORANGES, aspect="auto", interpolation="nearest")
    v = fld["v"][k]
    fb = h.shape[0]
    xs = lo[0] + (np.arange(fb) + .5) / fb * (hi[0] - lo[0])
    ys = lo[1] + (np.arange(fb) + .5) / fb * (hi[1] - lo[1])
    X, Y = np.meshgrid(xs, ys, indexing="ij")
    step = 2
    m = sup[::step, ::step]
    ax.quiver(X[::step, ::step][m], Y[::step, ::step][m], v[::step, ::step, 0][m], v[::step, ::step, 1][m],
              color=INK, width=0.0025, headwidth=4, alpha=0.85, scale_units="xy", angles="xy", scale=1.0 / 0.9 if not period else 1 / 0.9)
    cb = fig.colorbar(im, ax=ax, fraction=0.045, pad=0.02, format="%.3g")
    cb.set_label("mobility h (nm): RMS pair-distance change", color=INK2)
    cb.outline.set_visible(False)
    fs = next(s for s in S["field"]["summaries"] if s["tau_frames"] == tau_ref)
    ax.set_title(f"(b) deformation field at τ = {time_label(tau_ref, clock)}\n"
                 f"{fs['supported_bins']} supported bins · median h {fmt(fs['median_h'])} nm · "
                 f"median drift/spread {fmt(fs['median_drift_ratio'], '.2f')}", loc="left", fontsize=9)
    ax.set_xlim(lo[0], hi[0]); ax.set_ylim(lo[1], hi[1])
    ax.set_xlabel("chart axis 1"); ax.set_ylabel("chart axis 2")

    # (c) fluid filtration
    ax = axes[1, 0]
    rows = S["fluid_filtration"]["rows"]
    t = np.array([r["tau_frames"] for r in rows], float)
    tplot = np.maximum(t, 0.5)
    b0 = [r["betti"][0] for r in rows]
    b1 = [r["betti"][1] for r in rows]
    ax.step(tplot, b0, where="post", color=GROUP["atom"], lw=2)
    ax.step(tplot, b1, where="post", color=GROUP["backbone"], lw=2)
    ax.text(tplot[-1], b0[-1], "  β₀", color=GROUP["atom"], va="center", fontsize=9)
    ax.text(tplot[-1], b1[-1], "  β₁", color=GROUP["backbone"], va="center", fontsize=9)
    ax.set_xscale("log")
    ax.set_xlabel("ambient time τ (frames; τ = 0 drawn at 0.5)" + (f"; 1 frame = {time_label(1, clock)}" if clock else ""))
    ax.set_ylabel("Betti number of the τ-thickened cover nerve")
    fc = S["fluid_filtration"]["first_connected_tau"]
    ax.set_title(f"(c) fluid filtration: nerve of W_i^τ\nfirst connected at τ = "
                 f"{'never' if fc is None else time_label(fc, clock)}", loc="left", fontsize=9)
    ax.grid(True, axis="y", color=GRID, lw=0.5)
    ax.set_xlim(0.4, tplot[-1] * 3)

    # (d) flooding filtration
    ax = axes[1, 1]
    rows = S["flooding"]["rows"]
    lv = [r["level"] for r in rows]
    ax.step(lv, [r["betti"][0] for r in rows], where="post", color=GROUP["atom"], lw=2)
    ax.step(lv, [r["betti"][1] for r in rows], where="post", color=GROUP["backbone"], lw=2)
    ax.text(lv[-1], rows[-1]["betti"][0], "  β₀", color=GROUP["atom"], va="center", fontsize=9)
    ax.text(lv[-1], rows[-1]["betti"][1], "  β₁", color=GROUP["backbone"], va="center", fontsize=9)
    ax.set_xlabel("flooding level c of −log(p / p_max)")
    ax.set_ylabel("Betti number of the sublevel set {F ≤ c}")
    basins = [p for p in S["flooding"]["basin_pairs"] if p[1] is None or p[1] - p[0] >= 1.0]
    ax.set_title(f"(d) flooding filtration of the occupancy landscape\n{len(basins)} basins with persistence ≥ 1 (log-occupancy units)",
                 loc="left", fontsize=9)
    ax.grid(True, axis="y", color=GRID, lw=0.5)
    ax.set_xlim(lv[0], lv[-1] * 1.12)

    fig.text(0.07, 0.955, S["label"], fontsize=13, color=INK, weight="bold")
    fig.text(0.07, 0.925, f"{S['group']} group · {S['representation']} ({S['sites']} sites) · {S['frames']:,} frames in {S['runs']} runs · "
             f"chart: {S['chart']['kind']}" + (f" · clock {time_label(1, clock)}/frame" if clock else " · physical clock unresolved"),
             fontsize=8.5, color=INK2)
    fig.text(0.07, 0.902, "Descriptive constructions: no equilibrium free energy, rate or configuration-space nerve theorem is claimed.",
             fontsize=7.5, color=MUTED)
    fig.savefig(out / "figure.png", dpi=150)
    plt.close(fig)
    return out / "figure.png"


if __name__ == "__main__":
    ids = sys.argv[1:] or sorted(p.name for p in DIST.iterdir() if (p / "summary.json").exists())
    for sid in ids:
        try:
            print(render(sid), flush=True)
        except Exception as e:  # keep going; report at the end
            print("FAILED", sid, repr(e), flush=True)

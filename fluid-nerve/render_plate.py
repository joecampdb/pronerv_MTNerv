"""Atlas plate for one system: biophysical object + categorical nerve + deformation field + filtrations.

  (A) recorded conformation nearest the occupancy peak, with the deformation field drawn on the molecule
      (mean rigid-aligned site displacement over the reference lag, in the chart bin of that conformation)
  (B) chart occupancy with the face-poset nerve; one morphism and one 2-cell are annotated
  (C) mobility h and drift v on the chart at the reference lag
  (D) fluid filtration Betti curves      (E) flooding filtration Betti curves
  (F) categorical reading of the plate (objects, morphisms, 2-cells, 3-cells, fluid extension)
Writes dist/systems/<id>/plate.png.  Usage: python render_plate.py [ids...]
"""
import json
import sys
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fluidnerve.textsym import sym  # noqa: E402

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist/systems"
INK, INK2, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#fcfcfb"
GROUP = dict(atom="#2a78d6", backbone="#eb6834", paired="#1baf7a")
ELEMENT = dict(C="#52514e", N="#2a78d6", O="#e34948", S="#eda100", P="#eb6834", H="#c3c2b7")
BLUES = ListedColormap(["#f4f8fd", "#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5",
                        "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b"], name="blues13")
ORANGES = LinearSegmentedColormap.from_list("orange1", ["#fdf1ea", "#f7c4ab", "#f29a72", "#eb6834", "#b94417", "#7a2a0e"])
SEQ = LinearSegmentedColormap.from_list("seq", ["#86b6ef", "#2a78d6", "#0d366b"])
plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Segoe UI", "DejaVu Sans"], "font.size": 8.5,
                     "axes.edgecolor": "#c3c2b7", "axes.labelcolor": INK2, "xtick.color": MUTED, "ytick.color": MUTED,
                     "axes.titlecolor": INK, "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
                     "axes.spines.top": False, "axes.spines.right": False})


def fmt(x, spec=".3g"):
    return "n/a" if x is None else format(x, spec)


def time_label(frames, clock):
    if frames is None:
        return "never"
    if clock is None:
        return f"{frames} frames"
    ps = frames * clock
    return f"{ps*1000:.3g} fs" if ps < 1 else (f"{ps:.3g} ps" if ps < 1000 else f"{ps/1000:.3g} ns")


def element_of(label):
    atom = label.split("_")[-1] if "_" in label else label
    return atom[:1].upper()


def draw_molecule(ax, coords, site_labels, representation, u=None, group="atom"):
    X = coords - coords.mean(0)
    K = len(X)
    ca = "C-alpha" in representation or representation == "ca"
    if ca:
        cols = SEQ(np.linspace(0, 1, K))
        ax.plot(X[:, 0], X[:, 1], X[:, 2], color=INK2, lw=2.2, alpha=0.9, solid_capstyle="round")
        ax.scatter(X[:, 0], X[:, 1], X[:, 2], s=22 if K < 120 else 10, c=cols, depthshade=False, edgecolor=SURFACE, linewidth=0.4)
    else:
        D = np.linalg.norm(X[:, None] - X[None], axis=2)
        i, j = np.where(np.triu(D < 0.19, 1))
        for a, b in zip(i, j):
            ax.plot(X[[a, b], 0], X[[a, b], 1], X[[a, b], 2], color=INK2, lw=1.6, alpha=0.85)
        cols = [ELEMENT.get(element_of(l), INK2) for l in site_labels]
        ax.scatter(X[:, 0], X[:, 1], X[:, 2], s=70 if K < 40 else 28, c=cols, depthshade=False, edgecolor=SURFACE, linewidth=0.5)
    extent = np.abs(X).max() * 1.15 + 1e-6
    if u is not None and np.isfinite(u).all():
        lengths = np.linalg.norm(u, axis=1)
        med = np.median(lengths) if lengths.max() > 0 else 0
        factor = (0.18 * extent / med) if med > 0 else 1.0
        factor = float(min(max(factor, 1.0), 400.0))
        ax.quiver(X[:, 0], X[:, 1], X[:, 2], u[:, 0] * factor, u[:, 1] * factor, u[:, 2] * factor,
                  color=GROUP["backbone"], lw=1.2, arrow_length_ratio=0.25, alpha=0.95)
        note = f"arrows: mean rigid-aligned site displacement over τ_ref (×{factor:.0f})"
    else:
        note = "deformation field unsupported in this bin"
    ax.set_xlim(-extent, extent); ax.set_ylim(-extent, extent); ax.set_zlim(-extent, extent)
    ax.set_box_aspect((1, 1, 1))
    ax.set_axis_off()
    ax.view_init(elev=18, azim=-55)
    return note


def plate(sid):
    out = DIST / sid
    S = json.loads((out / "summary.json").read_text())
    nerve = json.loads((out / "nerve.json").read_text())
    fld = np.load(out / "field.npz", allow_pickle=True)
    rep = np.load(out / "representatives.npz")
    lo, hi = np.array(S["limits"])
    period = S["chart"]["periodic"]
    clock = S["clock_ps_per_frame"]
    tau_ref = int(fld["tau_ref"])
    taus = list(fld["taus"]); k = taus.index(tau_ref)
    extent = [lo[0], hi[0], lo[1], hi[1]]
    gcol = GROUP.get(S["group"], INK)
    nd = S["nerve_display_counts"]
    fig = plt.figure(figsize=(12.5, 9.2))
    gs = fig.add_gridspec(2, 3, left=0.05, right=0.985, top=0.83, bottom=0.07, hspace=0.45, wspace=0.28, width_ratios=[1.15, 1.25, 0.95])

    # (A) biophysical object
    ax = fig.add_subplot(gs[0, 0], projection="3d")
    coords = rep["coords"][-1]
    u = None
    if fld["u_ref"].size:
        b = rep["field_bin"][-1]
        try:
            u = fld["u_ref"][b[0], b[1]]
        except Exception:
            u = None
    note = draw_molecule(ax, coords, [str(x) for x in rep["site_labels"]], S["representation"], u, S["group"])
    ax.set_box_aspect((1, 1, 1), zoom=1.45)
    ax.set_title(sym(f"(A) biophysical object: recorded frame {int(rep['frame'][-1])}\n(nearest the occupancy peak); {S['representation']}, {S['sites']} sites\n{note}"),
                 loc="left", fontsize=8.0)

    # (B) chart + nerve with categorical annotation
    ax = fig.add_subplot(gs[0, 1])
    occ = fld["occupancy"].astype(float)
    ax.imshow((occ / occ.max()).T, origin="lower", extent=extent, cmap=BLUES, vmin=0, vmax=1, aspect="auto", interpolation="nearest")
    pos = np.array([n["chart"] for n in nerve["nodes"]])
    dims = np.array([len(n["simplex"]) for n in nerve["nodes"]])
    ok_edge = lambda a, b: not (period and np.abs(pos[a] - pos[b]).max() > 180)
    for i, j in nerve["edges"]:
        if ok_edge(i, j):
            ax.plot([pos[i, 0], pos[j, 0]], [pos[i, 1], pos[j, 1]], color=INK2, lw=0.35, alpha=0.5)
    for d, ms in ((1, 16), (2, 9), (3, 4.5)):
        sel = dims == d
        if sel.any():
            ax.scatter(pos[sel, 0], pos[sel, 1], s=ms, facecolor=SURFACE, edgecolor=INK, linewidth=0.6, zorder=5)
    scale = np.array(nerve["metric_scale"])
    for c in nerve["centers"]:
        ax.add_patch(Ellipse(c, 2 * nerve["radius"] * scale[0], 2 * nerve["radius"] * scale[1], fill=False, edgecolor=gcol, lw=0.5, alpha=0.55))
    # annotate one composable pair (2-cell) and its morphisms
    best = None
    for (i, j, kk) in nerve["chains"]:
        if ok_edge(i, j) and ok_edge(j, kk) and ok_edge(i, kk):
            spread = min(np.linalg.norm(pos[i] - pos[j]), np.linalg.norm(pos[j] - pos[kk]), np.linalg.norm(pos[i] - pos[kk]))
            if best is None or spread > best[0]:
                best = (spread, i, j, kk)
    if best:
        _, i, j, kk = best
        ax.add_patch(Polygon(pos[[i, j, kk]], closed=True, facecolor=GROUP["backbone"], alpha=0.22, edgecolor="none", zorder=4))
        for a, b, lab in ((i, j, "σ ↪ τ"), (j, kk, "τ ↪ ρ"), (i, kk, "σ ↪ ρ")):
            ax.add_patch(FancyArrowPatch(pos[a], pos[b], arrowstyle="-|>", mutation_scale=9, color=INK, lw=0.9, zorder=6, shrinkA=3, shrinkB=3))
        cen = pos[[i, j, kk]].mean(0)
        ax.annotate(sym("2-cell: (σ↪τ);(τ↪ρ) ⇒ σ↪ρ"), cen, textcoords="offset points", xytext=(8, 10), fontsize=7, color=INK,
                    bbox=dict(boxstyle="round,pad=0.2", facecolor=SURFACE, edgecolor=GRID, alpha=0.9), zorder=7)
        for a, name in ((i, "σ=" + "{" + ",".join(map(str, nerve["nodes"][i]["simplex"])) + "}"),
                        (j, "τ=" + "{" + ",".join(map(str, nerve["nodes"][j]["simplex"])) + "}"),
                        (kk, "ρ=" + "{" + ",".join(map(str, nerve["nodes"][kk]["simplex"])) + "}")):
            ax.annotate(name, pos[a], textcoords="offset points", xytext=(4, -9), fontsize=6.5, color=INK2, zorder=7)
    ax.set_xlim(lo[0], hi[0]); ax.set_ylim(lo[1], hi[1])
    ax.set_title(f"(B) chart occupancy, {len(nerve['centers'])} cover balls, face-poset nerve\n"
                 f"{nd['objects']} objects · {nd['inclusions']} morphisms · {nd['triangles']} 2-cells · {nd['base_tetrahedra']} base tetrahedra · β = {S['nerve']['betti_0_1_2']}",
                 loc="left", fontsize=8.5)
    ax.set_xlabel("chart axis 1" + (" (φ, °)" if period else " (PC1, nm)")); ax.set_ylabel("chart axis 2" + (" (ψ, °)" if period else " (PC2, nm)"))

    # (F) categorical reading
    ax = fig.add_subplot(gs[0, 2]); ax.set_axis_off()
    fl = S["fluid_filtration"]; fc = fl["first_connected_tau"]
    fs = next((s for s in S["field"]["summaries"] if s["tau_frames"] == tau_ref), {})
    sc = S["field"].get("mobility_scaling") or {}
    flips = S.get("membership_flip_rate") or {}
    crf = next((round(r["radius"] / S["nerve"]["radius"], 2) for r in S["radius_sensitivity"] if r["betti_0_1_2"][0] == 1), None)
    text = [
        "(F) categorical reading",
        "",
        f"Cover 𝒰: {len(nerve['centers'])} balls, radius {S['nerve']['radius']:.3g} ({'degrees' if period else 'chart s.d.'}).",
        f"Witnessed complex K(𝒰;S): max dim {S['nerve']['max_dimension']},",
        f"  {len(nerve['maximal_simplices'])} maximal simplices; β₀,β₁,β₂ = {S['nerve']['betti_0_1_2']};",
        f"  β₀ = 1 first at radius ×{fmt(crf, '.2f')}.",
        "",
        "Category N(𝒰) (face poset of the 2-skeleton):",
        f"  objects = faces σ (U_σ = ∩ U_i)             {nd['objects']}",
        f"  morphisms = inclusions σ ↪ τ                 {nd['inclusions']}",
        f"  2-cells = composable pairs (orientals)        {nd['triangles']}",
        f"  3-cells (base tetrahedra / length-3 chains)   {nd['base_tetrahedra']}",
        "",
        "Fluid extension:",
        f"  N_τ = nerve of the ±τ-thickened cover; τ ↦ N_τ",
        f"  is a functor (ℝ≥0, ≤) → SimpCx. β₀ = 1 from τ = {time_label(fc, clock)}.",
        f"  β₁ classes born: {fl['persistence_summary']['1']['finite_classes'] + fl['persistence_summary']['1']['essential']},"
        f" total β₁ lifetime {fl['persistence_summary']['1']['total_lifetime_frames']} frames.",
        f"  membership flip rate at 1 frame: {fmt(flips.get('1'), '.3f')}",
        "",
        "Deformation field (presheaf of conditional laws over",
        "  N(𝒰), derived from the cosheaf μ_τ of pair measures):",
        f"  τ_ref = {time_label(tau_ref, clock)}; median h = {fmt(fs.get('median_h'))} nm;",
        f"  drift/spread = {fmt(fs.get('median_drift_ratio'), '.2f')}; mobility exponent α = {fmt(sc.get('slope'), '.2f')}",
        f"  (early α = {fmt(sc.get('early_slope'), '.2f')}).",
        "",
        "Flooding filtration (metadynamics analogue):",
        f"  {sum(1 for p in S['flooding']['basin_pairs'] if p[1] is None or p[1]-p[0] >= 1)} basins with persistence ≥ 1 log-occupancy unit.",
    ]
    ax.text(0.0, 1.0, "\n".join(sym(t) for t in text), va="top", ha="left", fontsize=7.4, color=INK, family="DejaVu Sans", linespacing=1.35,
            transform=ax.transAxes)

    # (C) field
    ax = fig.add_subplot(gs[1, 0])
    h = fld["h"][k].astype(float); sup = fld["support"][k]; h = np.where(sup, h, np.nan)
    im = ax.imshow(h.T, origin="lower", extent=extent, cmap=ORANGES, aspect="auto", interpolation="nearest")
    v = fld["v"][k]; fb = h.shape[0]
    xs = lo[0] + (np.arange(fb) + .5) / fb * (hi[0] - lo[0]); ys = lo[1] + (np.arange(fb) + .5) / fb * (hi[1] - lo[1])
    X, Y = np.meshgrid(xs, ys, indexing="ij")
    step = 2 if fb > 15 else 1
    m = sup[::step, ::step]
    if m.any():
        ax.quiver(X[::step, ::step][m], Y[::step, ::step][m], v[::step, ::step, 0][m], v[::step, ::step, 1][m], color=INK, width=0.003,
                  headwidth=4, alpha=0.85, scale_units="xy", angles="xy", scale=1 / 0.9)
    cb = fig.colorbar(im, ax=ax, fraction=0.045, pad=0.02, format="%.3g"); cb.outline.set_visible(False)
    cb.set_label("mobility h (nm)", color=INK2)
    ax.set_title(sym(f"(C) deformation field at τ_ref = {time_label(tau_ref, clock)}: h (colour) and drift v (arrows)\n"
                 f"{fs.get('supported_bins', 0)} supported bins on a {fb}×{fb} grid"), loc="left", fontsize=8.5)
    ax.set_xlim(lo[0], hi[0]); ax.set_ylim(lo[1], hi[1]); ax.set_xlabel("chart axis 1"); ax.set_ylabel("chart axis 2")

    # (D) fluid
    ax = fig.add_subplot(gs[1, 1])
    rows = fl["rows"]; t = np.maximum(np.array([r["tau_frames"] for r in rows], float), 0.5)
    b0 = [r["betti"][0] for r in rows]; b1 = [r["betti"][1] for r in rows]
    ax.step(t, b0, where="post", color=GROUP["atom"], lw=2); ax.step(t, b1, where="post", color=GROUP["backbone"], lw=2)
    ax.text(t[-1], b0[-1], "  β₀", color=GROUP["atom"], va="center"); ax.text(t[-1], b1[-1], "  β₁", color=GROUP["backbone"], va="center")
    ax.set_xscale("log"); ax.set_xlim(0.4, t[-1] * 3); ax.grid(True, axis="y", color=GRID, lw=0.5)
    ax.set_xlabel("ambient time τ (frames; τ = 0 at 0.5)" + (f"; 1 frame = {time_label(1, clock)}" if clock else ""))
    ax.set_ylabel(sym("Betti numbers of N_τ"))
    ax.set_title(sym(f"(D) fluid filtration τ ↦ N_τ\nfirst connected at τ = {time_label(fc, clock)}"), loc="left", fontsize=8.5)

    # (E) flooding
    ax = fig.add_subplot(gs[1, 2])
    rows = S["flooding"]["rows"]; lv = [r["level"] for r in rows]
    ax.step(lv, [r["betti"][0] for r in rows], where="post", color=GROUP["atom"], lw=2)
    ax.step(lv, [r["betti"][1] for r in rows], where="post", color=GROUP["backbone"], lw=2)
    ax.text(lv[-1], rows[-1]["betti"][0], "  β₀", color=GROUP["atom"], va="center"); ax.text(lv[-1], rows[-1]["betti"][1], "  β₁", color=GROUP["backbone"], va="center")
    ax.set_xlim(lv[0], lv[-1] * 1.12); ax.grid(True, axis="y", color=GRID, lw=0.5)
    ax.set_xlabel("flooding level c of −log(p / p_max)"); ax.set_ylabel("Betti numbers of {F ≤ c}")
    ax.set_title("(E) flooding filtration of the occupancy landscape", loc="left", fontsize=8.5)

    fig.text(0.05, 0.955, S["label"], fontsize=13, color=INK, weight="bold")
    fig.text(0.05, 0.925, f"{S['group']} group · {S['representation']} ({S['sites']} sites) · {S['frames']:,} frames in {S['runs']} runs · "
             f"chart: {S['chart']['kind']}" + (f" · clock {time_label(1, clock)}/frame" if clock else " · physical clock unresolved") + f" · id {sid}",
             fontsize=8.5, color=INK2)
    fig.text(0.05, 0.902, "Descriptive constructions: no equilibrium free energy, rate or configuration-space nerve theorem is claimed.", fontsize=7.5, color=MUTED)
    fig.savefig(out / "plate.png", dpi=140)
    plt.close(fig)
    return out / "plate.png"


if __name__ == "__main__":
    ids = sys.argv[1:] or sorted(p.name for p in DIST.iterdir() if (p / "representatives.npz").exists())
    for sid in ids:
        try:
            print(plate(sid), flush=True)
        except Exception as e:
            print("FAILED", sid, repr(e), flush=True)

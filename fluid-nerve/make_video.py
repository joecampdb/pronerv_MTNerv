"""Pedagogical video: how the nerve plate rises out of a biophysical object (alanine dipeptide).

Scenes (20 fps, ~55 s):
  1 title  2 the molecule  3 recorded frames become chart points  4 occupancy and the cover
  5 the deformation field lifts the chart: the plate rises  6 the nerve rises onto the plate (objects, morphisms, 2-cells)
  7 ambient time: the fluid extension  8 legend card
Writes dist/video/nerve-plate-alanine.mp4 (H.264) and a short GIF preview.  Needs ffmpeg on PATH.
"""
import json
import shutil
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
from matplotlib.patches import Ellipse, Polygon
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fluidnerve.textsym import sym  # noqa: E402

ROOT = Path(__file__).resolve().parent
SYS = ROOT / "dist/systems/ala2"
OUT = ROOT / "dist/video"
ATLAS = ROOT.parent / "alanine-nerve"
INK, INK2, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#fcfcfb"
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
ELEMENT = dict(C="#52514e", N="#2a78d6", O="#e34948")
BLUES = ListedColormap(["#f4f8fd", "#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5", "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b"])
ORANGES = LinearSegmentedColormap.from_list("orange1", ["#fdf1ea", "#f7c4ab", "#f29a72", "#eb6834", "#b94417", "#7a2a0e"])
plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Segoe UI", "DejaVu Sans"], "font.size": 11,
                     "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "axes.edgecolor": "#c3c2b7", "axes.labelcolor": INK2,
                     "xtick.color": MUTED, "ytick.color": MUTED, "axes.spines.top": False, "axes.spines.right": False})
FPS = 20
W, H = 12.8, 7.2
ZSCALE = 130.0  # degrees of chart per nm of mobility, for the 3D plate


def load():
    S = json.loads((SYS / "summary.json").read_text())
    nerve = json.loads((SYS / "nerve.json").read_text())
    fld = np.load(SYS / "field.npz", allow_pickle=True)
    coords = np.load(ATLAS / "data/alanine-dipeptide-3x250ns-heavy-atom-positions.npz")
    angles = np.load(ATLAS / "data/alanine-dipeptide-3x250ns-backbone-dihedrals.npz")
    k0 = list(coords.keys())[0]
    xyz = coords[k0].reshape(-1, 10, 3)[:4000]
    phipsi = np.rad2deg(angles[list(angles.keys())[0]][:4000])
    from fluidnerve.geometry import align_to_reference
    aligned, _ = align_to_reference(xyz)
    return S, nerve, fld, aligned.astype(np.float32), phipsi


def molecule(ax, X, labels, alpha=1.0, arrows=None, factor=1.0):
    X = X - X.mean(0)
    D = np.linalg.norm(X[:, None] - X[None], axis=2)
    i, j = np.where(np.triu(D < 0.19, 1))
    for a, b in zip(i, j):
        ax.plot(X[[a, b], 0], X[[a, b], 1], X[[a, b], 2], color=INK2, lw=2.2, alpha=alpha)
    cols = [ELEMENT.get(l.split("_")[-1][0], INK2) for l in labels]
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], s=160, c=cols, depthshade=False, edgecolor=SURFACE, linewidth=0.8, alpha=alpha)
    if arrows is not None:
        ax.quiver(X[:, 0], X[:, 1], X[:, 2], arrows[:, 0] * factor, arrows[:, 1] * factor, arrows[:, 2] * factor,
                  color=ORANGE, lw=1.8, arrow_length_ratio=0.25)
    ax.set_xlim(-.45, .45); ax.set_ylim(-.45, .45); ax.set_zlim(-.45, .45); ax.set_box_aspect((1, 1, 1), zoom=1.55); ax.set_axis_off()



def plate_tiles(ax, xs, ys, hplot, sup, hmax, scale=1.0, alpha=1.0):
    """Draw the mobility plate as flat square tiles at height scale*h over supported bins only (no walls)."""
    fb = len(xs)
    dx = (xs[1] - xs[0]) / 2 if fb > 1 else 1
    dy = (ys[1] - ys[0]) / 2 if fb > 1 else 1
    polys, cols = [], []
    for i in range(fb):
        for j in range(fb):
            if not sup[i, j]:
                continue
            z = hplot[i, j] * ZSCALE * scale
            x, y = xs[i], ys[j]
            polys.append([(x - dx, y - dy, z), (x + dx, y - dy, z), (x + dx, y + dy, z), (x - dx, y + dy, z)])
            c = ORANGES(np.clip(hplot[i, j] / hmax, 0, 1))
            cols.append((c[0], c[1], c[2], alpha))
    if polys:
        pc = Poly3DCollection(polys, facecolors=cols, edgecolors=(0.3, 0.2, 0.1, 0.25 * alpha), linewidths=0.3)
        ax.add_collection3d(pc)

def caption(fig, title, body="", y=0.94):
    fig.text(0.04, y, sym(title), fontsize=17, color=INK, weight="bold")
    if body:
        fig.text(0.04, y - 0.05, sym(body), fontsize=11.5, color=INK2)


def card(fig, lines, y0=0.78, size=13):
    for k, line in enumerate(lines):
        fig.text(0.08, y0 - 0.075 * k, sym(line), fontsize=size, color=INK if not line.startswith("  ") else INK2)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    S, nerve, fld, X, pp = load()
    labels = ["ACE_CH3", "ACE_C", "ACE_O", "ALA_N", "ALA_CA", "ALA_CB", "ALA_C", "ALA_O", "NME_N", "NME_CH3"]
    lo, hi = np.array(S["limits"])
    taus = list(fld["taus"]); k = taus.index(int(fld["tau_ref"]))
    h = fld["h"][k].astype(float); sup = fld["support"][k]
    hplot = np.where(sup, h, 0.0); hmax = np.nanmax(np.where(sup, h, np.nan))
    occ = fld["occupancy"].astype(float); dens = occ / occ.max()
    fb = h.shape[0]
    xs = lo[0] + (np.arange(fb) + .5) / fb * (hi[0] - lo[0]); ys = lo[1] + (np.arange(fb) + .5) / fb * (hi[1] - lo[1])
    Xg, Yg = np.meshgrid(xs, ys, indexing="ij")
    nodes = nerve["nodes"]; pos = np.array([n["chart"] for n in nodes]); dims = np.array([len(n["simplex"]) for n in nodes])
    heights = np.array([n.get("height_nm") or 0.0 for n in nodes]) * ZSCALE
    edges = [(i, j) for i, j in nerve["edges"] if np.abs(pos[i] - pos[j]).max() <= 180]
    chains = [(i, j, kk) for i, j, kk in nerve["chains"] if all(np.abs(pos[a] - pos[b]).max() <= 180 for a, b in ((i, j), (j, kk), (i, kk)))]
    centers = np.array(nerve["centers"]); radius = nerve["radius"]
    u_ref = fld["u_ref"]
    rep = np.load(SYS / "representatives.npz")
    peak_bin = rep["field_bin"][-1]
    u_peak = u_ref[peak_bin[0], peak_bin[1]] if u_ref.size else None
    fluid_rows = S["fluid_filtration"]["rows"]
    # components of the base complex at tau = 0 (union-find on witnessed pairs)
    parent = list(range(len(centers)))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a
    for m in nerve["maximal_simplices"]:
        for a in m[1:]:
            ra, rb = find(m[0]), find(a)
            if ra != rb:
                parent[ra] = rb
    comp = np.array([find(i) for i in range(len(centers))])
    comp_ids = {c: n for n, c in enumerate(sorted(set(comp)))}
    comp_col = [BLUE, ORANGE, AQUA, "#eda100", "#6250d6"]

    writer = FFMpegWriter(fps=FPS, codec="libx264", bitrate=4000, extra_args=["-pix_fmt", "yuv420p"])
    fig = plt.figure(figsize=(W, H), dpi=100)
    path = OUT / "nerve-plate-alanine.mp4"
    frame_count = 0
    with writer.saving(fig, str(path), dpi=100):
        def emit():
            nonlocal frame_count
            writer.grab_frame(); frame_count += 1; fig.clf()

        # 1 title (3 s)
        for t in range(3 * FPS):
            fig.text(0.5, 0.6, "How a nerve plate rises out of a molecule", ha="center", fontsize=26, color=INK, weight="bold")
            fig.text(0.5, 0.5, "alanine dipeptide · 3 × 250 ns recorded MD at 300 K (mdshare) · heavy atoms", ha="center", fontsize=14, color=INK2)
            fig.text(0.5, 0.42, sym("biophysical object → chart → cover → deformation field (the plate) → nerve (the category) → ambient time (the fluid extension)"),
                     ha="center", fontsize=11, color=MUTED)
            fig.text(0.5, 0.2, "pronerv fluid-nerve atlas · descriptive constructions, no free energy or rate claims", ha="center", fontsize=10, color=MUTED)
            emit()
        # 2 molecule rotating (5 s)
        for t in range(5 * FPS):
            ax = fig.add_subplot(111, projection="3d")
            molecule(ax, X[0], labels)
            ax.view_init(elev=18, azim=-60 + 360 * t / (5 * FPS))
            caption(fig, "1. The biophysical object", "Ace–Ala–NMe, ten heavy atoms (C grey, N blue, O red). Each recorded frame is one configuration of these sites.")
            emit()
        # 3 frames become chart points (8 s)
        n3 = 8 * FPS
        for t in range(n3):
            fi = int(t * 2000 / n3)
            ax = fig.add_subplot(121, projection="3d")
            molecule(ax, X[fi], labels)
            ax.view_init(elev=18, azim=-60)
            ax.set_title(f"frame {fi} (t = {fi} ps)", color=INK2, fontsize=10)
            ax2 = fig.add_subplot(122)
            ax2.scatter(pp[:fi:2, 0], pp[:fi:2, 1], s=5, color=BLUE, alpha=0.35)
            ax2.scatter([pp[fi, 0]], [pp[fi, 1]], s=90, facecolor=ORANGE, edgecolor=INK, zorder=5)
            ax2.set_xlim(-180, 180); ax2.set_ylim(-180, 180); ax2.set_xlabel("φ (°)"); ax2.set_ylabel("ψ (°)")
            ax2.set_aspect("equal"); ax2.grid(True, color=GRID, lw=0.5)
            caption(fig, "2. The chart", "Backbone dihedrals (φ, ψ) map every frame to a point on a torus. The trajectory writes the chart.")
            emit()
        # 4 occupancy and cover (6 s)
        n4 = 6 * FPS
        for t in range(n4):
            ax = fig.add_subplot(111)
            a = min(1.0, t / (0.3 * n4))
            ax.imshow(dens.T, origin="lower", extent=[-180, 180, -180, 180], cmap=BLUES, vmin=0, vmax=1, alpha=a, aspect="equal", interpolation="nearest")
            nb = int(np.clip((t - 0.35 * n4) / (0.6 * n4) * len(centers), 0, len(centers)))
            for c in centers[:nb]:
                ax.add_patch(Ellipse(c, 2 * radius, 2 * radius, fill=False, edgecolor=ORANGE, lw=1.4))
                ax.scatter([c[0]], [c[1]], s=14, color=ORANGE)
            ax.set_xlim(-180, 180); ax.set_ylim(-180, 180); ax.set_xlabel("φ (°)"); ax.set_ylabel("ψ (°)")
            caption(fig, "3. Occupancy and cover", f"750,000 frames give the occupancy. {len(centers)} balls of radius {radius:.0f}° (farthest-point centres) cover the occupied chart; "
                    "overlaps are witnessed by frames." if nb else "750,000 frames give the occupancy on a 30 × 30 grid.")
            emit()
        # 5 the plate rises (7 s)
        n5 = 7 * FPS
        for t in range(n5):
            s = min(1.0, t / (0.7 * n5))
            ax = fig.add_subplot(111, projection="3d")
            ax.contourf(Xg, Yg, dens[:fb, :fb], zdir="z", offset=-0.3, cmap=BLUES, alpha=0.9, levels=12)
            plate_tiles(ax, xs, ys, hplot, sup, hmax, scale=s, alpha=1.0)
            ax.set_xlim(-180, 180); ax.set_ylim(-180, 180); ax.set_zlim(-0.3, ZSCALE * hmax * 1.15)
            ax.set_xlabel("φ (°)"); ax.set_ylabel("ψ (°)"); ax.set_zlabel("mobility h (scaled)")
            ax.view_init(elev=28, azim=-50 + 20 * t / n5)
            caption(fig, "4. The deformation field lifts the chart: the plate rises",
                    f"h(φ,ψ) = RMS change of the 45 pair distances over τ = 100 ps, conditional on the bin (median {np.nanmedian(np.where(sup, h, np.nan)):.3f} nm). Unsupported bins stay flat.")
            emit()
        # 6 the nerve rises (9 s)
        n6 = 9 * FPS
        order = np.argsort(dims, kind="stable")
        for t in range(n6):
            prog = t / n6
            ax = fig.add_subplot(111, projection="3d")
            ax.contourf(Xg, Yg, dens[:fb, :fb], zdir="z", offset=-0.3, cmap=BLUES, alpha=0.7, levels=12)
            plate_tiles(ax, xs, ys, hplot, sup, hmax, scale=1.0, alpha=0.55)
            nshow = int(min(len(order), prog / 0.45 * len(order)))
            zoff = 0.25
            for i in order[:nshow]:
                ax.scatter([pos[i, 0]], [pos[i, 1]], [heights[i] + zoff], s=(60, 28, 12)[dims[i] - 1], facecolor=SURFACE, edgecolor=INK, linewidth=0.8, depthshade=False)
            if prog > 0.45:
                ne = int(min(len(edges), (prog - 0.45) / 0.3 * len(edges)))
                for i, j in edges[:ne]:
                    ax.plot([pos[i, 0], pos[j, 0]], [pos[i, 1], pos[j, 1]], [heights[i] + zoff, heights[j] + zoff], color=INK2, lw=0.6, alpha=0.7)
            if prog > 0.75:
                nc = int(min(len(chains), (prog - 0.75) / 0.25 * len(chains)))
                tris = [[(pos[a, 0], pos[a, 1], heights[a] + zoff) for a in (i, j, kk)] for i, j, kk in chains[:nc]]
                if tris:
                    ax.add_collection3d(Poly3DCollection(tris, facecolor=ORANGE, alpha=0.25, edgecolor="none"))
            ax.set_xlim(-180, 180); ax.set_ylim(-180, 180); ax.set_zlim(-0.3, ZSCALE * hmax * 1.3)
            ax.set_xlabel("φ (°)"); ax.set_ylabel("ψ (°)"); ax.set_zlabel("mobility h (scaled)")
            ax.view_init(elev=30, azim=-30 + 25 * prog)
            if prog <= 0.45:
                body = "Objects: faces σ of the witnessed complex, drawn at the witness centroid and lifted to the plate height h(σ)."
            elif prog <= 0.75:
                body = "Morphisms: strict inclusions σ ↪ τ (one edge per inclusion). Composition is transitivity; identities are implicit."
            else:
                body = "2-cells: composable pairs (σ↪τ);(τ↪ρ) ⇒ σ↪ρ, the triangles. With 3-cells they give the homotopy.io presentation."
            caption(fig, "5. The nerve rises onto the plate: the category N(𝒰)", body)
            emit()
        # 7 ambient time (7 s)
        n7 = 7 * FPS
        t_rows = [r["tau_frames"] for r in fluid_rows]; b0_rows = [r["betti"][0] for r in fluid_rows]
        for t in range(n7):
            prog = t / n7
            ax = fig.add_subplot(121, projection="3d")
            ax.contourf(Xg, Yg, dens[:fb, :fb], zdir="z", offset=-0.3, cmap=BLUES, alpha=0.6, levels=12)
            plate_tiles(ax, xs, ys, hplot, sup, hmax, scale=1.0, alpha=0.4)
            merged = prog > 0.5
            vert_height = {tuple(nodes[i]["simplex"])[0]: heights[i] for i in range(len(nodes)) if dims[i] == 1}
            for i in range(len(centers)):
                col = comp_col[comp_ids[comp[i]] % len(comp_col)] if not merged else BLUE
                zi = vert_height.get(i, 0.0) + 0.25
                ax.scatter([centers[i, 0]], [centers[i, 1]], [zi], s=70, facecolor=col, edgecolor=INK, depthshade=False)
            if merged:
                for a in range(len(centers)):
                    for b in range(a + 1, len(centers)):
                        if comp[a] != comp[b]:
                            d = np.abs(centers[a] - centers[b]).max()
                            if d <= 180 and np.linalg.norm(centers[a] - centers[b]) < 140:
                                ax.plot([centers[a, 0], centers[b, 0]], [centers[a, 1], centers[b, 1]], [vert_height.get(a, 0.0) + 0.25, vert_height.get(b, 0.0) + 0.25], color=AQUA, lw=1.0, ls="--")
            ax.set_xlim(-180, 180); ax.set_ylim(-180, 180); ax.set_zlim(-0.3, ZSCALE * hmax * 1.3); ax.set_axis_off()
            ax.view_init(elev=35, azim=-40)
            ax2 = fig.add_subplot(122)
            tp = np.maximum(np.array(t_rows, float), 0.5)
            ax2.step(tp, b0_rows, where="post", color=BLUE, lw=2.5)
            cur = 0 if not merged else max(1, int((prog - 0.5) / 0.5 * (len(tp) - 1)))
            ax2.scatter([tp[cur]], [b0_rows[cur]], s=120, facecolor=ORANGE, edgecolor=INK, zorder=5)
            ax2.set_xscale("log"); ax2.set_xlabel("ambient time τ (ps; τ = 0 drawn at 0.5)"); ax2.set_ylabel(sym("β₀ of N_τ (components)"))
            ax2.set_ylim(0, max(b0_rows) + 0.5); ax2.grid(True, color=GRID, lw=0.5)
            caption(fig, "6. Ambient time: the fluid extension",
                    "Thicken every ball by ±τ frames along the runs: W_i^τ. Its nerve N_τ grows with τ; τ ↦ N_τ is a functor (ℝ≥0, ≤) → SimpCx."
                    if not merged else f"At τ = 1 ps the three components of N₀ (coloured) are already tied by actual visits (dashed): β₀ = 1. Persistence in ambient time, not a rate.")
            emit()
        # 8 legend card (6 s)
        for t in range(6 * FPS):
            caption(fig, "Legend", "")
            card(fig, ["objects  = faces σ of the witnessed complex   (U_σ = ∩ U_i, witnessed by recorded frames)",
                       "morphisms = inclusions σ ↪ τ   (composition = transitivity; identities implicit)",
                       "2-cells  = composable pairs (σ↪τ);(τ↪ρ) ⇒ σ↪ρ;   3-cells = length-3 chains / quadruple overlaps (orientals → homotopy.io)",
                       "deformation field = cosheaf μ_τ of lag-τ pair measures over N(𝒰); h, v, Σ, u are its presheaf of conditional laws",
                       "fluid extension = functor τ ↦ N_τ from ambient time to simplicial complexes (persistence); rigid at infinitesimal τ for open covers",
                       "  descriptive constructions: no equilibrium free energy, rate or configuration-space nerve theorem is claimed",
                       "  pronerv_MTNerv / fluid-nerve · see fluid-nerve-theory.pdf and fluid-nerve-atlas.pdf"], y0=0.8, size=12)
            emit()
    print("frames", frame_count, "->", path)
    # GIF preview (every 4th frame, scaled) via ffmpeg
    gif = OUT / "nerve-plate-alanine-preview.gif"
    ff = shutil.which("ffmpeg") or matplotlib.rcParams.get("animation.ffmpeg_path", "ffmpeg")
    import subprocess
    subprocess.run([ff, "-y", "-loglevel", "error", "-i", str(path), "-vf", "fps=5,scale=640:-1", str(gif)], check=False)
    print("gif", gif.exists())


if __name__ == "__main__":
    main()

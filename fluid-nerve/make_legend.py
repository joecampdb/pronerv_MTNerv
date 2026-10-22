"""Categorical legend figure for the atlas: cover -> witnessed nerve -> face-poset category -> fluid extension.
Writes dist/comparison/fig_legend.png."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, FancyArrowPatch
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fluidnerve.textsym import sym  # noqa: E402

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dist/comparison"
INK, INK2, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#fcfcfb"
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Segoe UI", "DejaVu Sans"], "font.size": 8.5,
                     "figure.facecolor": SURFACE, "axes.facecolor": SURFACE})


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 4, figsize=(13.5, 3.9))
    for ax in axes:
        ax.set_axis_off(); ax.set_aspect("equal")

    # 1. cover and witnesses
    ax = axes[0]
    rng = np.random.default_rng(0)
    pts = np.concatenate([rng.normal([0.35, 0.55], 0.13, (60, 2)), rng.normal([0.65, 0.55], 0.13, (60, 2)), rng.normal([0.5, 0.3], 0.1, (40, 2))])
    ax.scatter(pts[:, 0], pts[:, 1], s=4, color=INK2, alpha=0.6)
    centers = [(0.35, 0.58), (0.65, 0.58), (0.5, 0.3)]
    for (x, y), name in zip(centers, ("U₀", "U₁", "U₂")):
        ax.add_patch(Circle((x, y), 0.2, fill=False, edgecolor=BLUE, lw=1.2))
        ax.text(x, y + 0.23, name, ha="center", color=BLUE, fontsize=9)
    ax.text(0.5, 0.58, sym("U₀∩U₁\nwitnessed"), ha="center", va="center", fontsize=6.5, color=INK)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_title(sym("1. cover 𝒰 of the chart and recorded frames (witnesses)"), loc="left", fontsize=8.5)

    # 2. witnessed complex and face poset (category)
    ax = axes[1]
    V = {"0": (0.15, 0.15), "1": (0.85, 0.15), "2": (0.5, 0.2), "01": (0.5, 0.45), "02": (0.3, 0.45), "12": (0.7, 0.45), "012": (0.5, 0.78)}
    for a, b in [("0", "01"), ("1", "01"), ("0", "02"), ("2", "02"), ("1", "12"), ("2", "12"), ("01", "012"), ("02", "012"), ("12", "012")]:
        ax.add_patch(FancyArrowPatch(V[a], V[b], arrowstyle="-|>", mutation_scale=8, color=INK2, lw=0.8, shrinkA=9, shrinkB=9))
    ax.add_patch(Polygon([V["0"], V["01"], V["012"]], closed=True, facecolor=ORANGE, alpha=0.18, edgecolor="none"))
    ax.add_patch(FancyArrowPatch(V["0"], V["012"], arrowstyle="-|>", mutation_scale=8, color=ORANGE, lw=1.1, shrinkA=9, shrinkB=9, connectionstyle="arc3,rad=-0.25"))
    for k, (x, y) in V.items():
        ax.text(x, y, sym("{") + ",".join(k) + "}", ha="center", va="center", fontsize=7.5, color=INK,
                bbox=dict(boxstyle="round,pad=0.25", facecolor=SURFACE, edgecolor=INK, lw=0.6))
    ax.text(0.5, 0.0, sym("objects = faces σ;  morphisms = inclusions σ ↪ τ;\n2-cell (orange) = composable pair ({0}↪{0,1});({0,1}↪{0,1,2}) ⇒ {0}↪{0,1,2}"),
            ha="center", va="bottom", fontsize=6.5, color=INK)
    ax.set_xlim(0, 1); ax.set_ylim(-0.05, 1)
    ax.set_title(sym("2. category N(𝒰): face poset of the witnessed complex"), loc="left", fontsize=8.5)

    # 3. fluid extension: thickened cover and the functor tau -> N_tau
    ax = axes[2]
    for (x, y) in [(0.3, 0.55), (0.7, 0.55)]:
        ax.add_patch(Circle((x, y), 0.17, fill=False, edgecolor=BLUE, lw=1.2))
        ax.add_patch(Circle((x, y), 0.26, fill=False, edgecolor=ORANGE, lw=1.0, ls="--"))
    t = np.linspace(0, 1, 60)
    path = np.column_stack([0.3 + 0.4 * t, 0.55 + 0.12 * np.sin(6 * t)])
    ax.plot(path[:, 0], path[:, 1], color=INK2, lw=1)
    ax.scatter(path[::6, 0], path[::6, 1], s=8, color=INK)
    ax.text(0.3, 0.84, sym("U_i"), ha="center", color=BLUE); ax.text(0.7, 0.84, sym("U_j"), ha="center", color=BLUE)
    ax.text(0.5, 0.18, sym("W_i^τ = frames within ±τ of a visit to U_i\n"
            "N_τ = nerve of {W_i^τ};  τ ≤ τ′ ⇒ N_τ ⊆ N_τ′\n"
            "τ ↦ N_τ : (ℝ≥0, ≤) → SimpCx  (persistence in ambient time)"), ha="center", va="center", fontsize=6.5, color=INK)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_title(sym("3. fluid extension: ambient-time thickening (dashed)"), loc="left", fontsize=8.5)

    # 4. deformation field as cosheaf / presheaf over the nerve + molecule glyph
    ax = axes[3]
    mol = np.array([[0.2, 0.6], [0.35, 0.5], [0.5, 0.6], [0.65, 0.5], [0.8, 0.6], [0.35, 0.32], [0.65, 0.32]])
    bonds = [(0, 1), (1, 2), (2, 3), (3, 4), (1, 5), (3, 6)]
    for a, b in bonds:
        ax.plot(mol[[a, b], 0], mol[[a, b], 1], color=INK2, lw=1.6)
    ax.scatter(mol[:, 0], mol[:, 1], s=60, c=[INK2, BLUE, INK2, "#e34948", INK2, INK2, INK2], edgecolor=SURFACE, zorder=3)
    disp = np.array([[0.04, 0.08], [-0.02, 0.06], [0.0, 0.1], [0.03, 0.05], [0.06, 0.07], [-0.05, -0.04], [0.05, -0.05]])
    ax.quiver(mol[:, 0], mol[:, 1], disp[:, 0], disp[:, 1], color=ORANGE, angles="xy", scale_units="xy", scale=1, width=0.008, zorder=4)
    ax.text(0.5, 0.12, sym("μ_τ|_{U_σ}: cosheaf of lag-τ pair measures over N(𝒰)\n"
            "h, v, Σ, u: presheaf of conditional laws (restrict, do not glue)\n"
            "u = mean rigid-aligned site displacement (arrows)"), ha="center", va="center", fontsize=6.5, color=INK)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.set_title(sym("4. deformation field on the molecule and over the nerve"), loc="left", fontsize=8.5)

    fig.suptitle("Legend: from a biophysical object to its fluid nerve", x=0.02, ha="left", fontsize=11, color=INK, weight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(OUT / "fig_legend.png", dpi=170)
    plt.close(fig)
    print(OUT / "fig_legend.png")


if __name__ == "__main__":
    main()

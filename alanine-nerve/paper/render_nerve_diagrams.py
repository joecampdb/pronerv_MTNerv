"""Render standalone, data-backed categorical nerve diagrams for both systems."""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / "output" / "nerve-diagrams"
OUT.mkdir(parents=True, exist_ok=True)
BG, FG, MUTED = "#0b1522", "#eef5f5", "#a9bec8"
MINT, GOLD = "#8de7c1", "#f3c784"
plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans"})


def triangle(ax, labels, morphisms, color):
    points = [(0.15, 0.22), (0.5, 0.79), (0.85, 0.22)]
    ax.add_patch(Polygon(points, facecolor=color, alpha=.075, edgecolor="none"))
    for i, j, txt, offset in [
        (0, 1, morphisms[0], (-.075, .015)),
        (1, 2, morphisms[1], (.075, .015)),
        (0, 2, morphisms[2], (0, -.105)),
    ]:
        a, b = points[i], points[j]
        ax.add_patch(FancyArrowPatch(
            a, b, arrowstyle="-|>", mutation_scale=22, linewidth=2.6,
            color=GOLD if (i,j)==(0,2) else color,
            shrinkA=38, shrinkB=38,
        ))
        ax.text((a[0]+b[0])/2+offset[0], (a[1]+b[1])/2+offset[1],
                txt, color=GOLD if (i,j)==(0,2) else color,
                fontsize=23, ha="center", va="center")
    for p, label in zip(points, labels):
        ax.add_patch(Circle(p, .069, facecolor="#142535", edgecolor=color, lw=2))
        ax.text(*p, label, color=FG, fontsize=14 if label.count(",") == 2 else 19,
                ha="center", va="center")
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis("off")


for slug, title, rel, subtitle in [
    ("alanine", "Alanine dipeptide", "data.json",
     r"Dihedral chart $(\phi,\psi)$  |  750,000 MD frames"),
    ("chignolin", "Chignolin · CLN025", "chignolin/data.json",
     r"Geometric chart $(R_g,d_{\mathrm{end}})$  |  63,999 MD frames"),
]:
    data = json.loads((ROOT / "dist" / rel).read_text())
    dyn = (json.loads((ROOT / "dist" / "dynamics.json").read_text())
           if slug == "alanine" else data)
    chain = data["chains"][0]
    sets = [data["nodes"][i]["simplex"] for i in chain]
    # Check this really is a 2-simplex of the face-poset nerve.
    assert set(sets[0]) < set(sets[1]) < set(sets[2])
    labels = ["$\\{" + ",".join(map(str, s)) + "\\}$" for s in sets]
    routes = dyn["edges"] if slug == "alanine" else dyn["routes"]
    f = next(r for r in routes if (r["source"], r["target"]) == (0, 1))
    g = next(r for r in routes if (r["source"], r["target"]) == (1, 2))
    fig = plt.figure(figsize=(15, 10), facecolor=BG)
    fig.text(.055, .935, "MOLECULAR ATLAS  /  CATEGORICAL NERVES",
             color=MINT, size=13, weight="bold")
    fig.text(.055, .865, title, color=FG, size=34, weight="bold")
    fig.text(.055, .82, subtitle, color=MUTED, size=15)
    fig.text(.055, .75, "01  OVERLAP / FACE POSET", color=MINT, size=15, weight="bold")
    fig.text(.535, .75, "02  DYNAMICS / PATH CATEGORY", color=MINT, size=15, weight="bold")
    left = fig.add_axes([.035, .29, .46, .43])
    right = fig.add_axes([.515, .29, .46, .43])
    triangle(left, labels, [r"$i$", r"$j$", r"$j\circ i$"], MINT)
    triangle(right, ["A", "B", "C"], [r"$f$", r"$g$", r"$g\circ f$"], MINT)
    fig.text(.055, .285, r"$(i,j)\in N_2(\mathrm{Face}(K))$", color=FG, size=21)
    fig.text(.535, .285, r"$(f,g)\in N_2(\mathcal{P})$", color=FG, size=21)
    fig.text(.055, .235,
             "Vertices are witnessed overlap index sets.\n"
             "Arrows are inclusions; the long edge is their composite.",
             color=MUTED, size=13, linespacing=1.65)
    fig.text(.535, .235,
             f"Observed route generators: A → B ({f['count']:,} events)\n"
             f"and B → C ({g['count']:,} events). Counts are not rates.",
             color=MUTED, size=13, linespacing=1.65)
    fig.text(.055, .145,
             r"$N_n(\mathcal{C})=\mathrm{Fun}([n],\mathcal{C})$"
             r"      •      $d_0(f,g)=g,\quad d_1(f,g)=g\circ f,\quad d_2(f,g)=f$",
             color=GOLD, size=18)
    fig.text(.055, .095,
             "Selected 2-simplices, not the full nerve. Composition is formal; it does not establish a continuous MD trajectory.\n"
             "Overlap incidence alone does not establish homotopy recovery. CLN025 is the chignolin variant used in this atlas.",
             color=MUTED, size=11, linespacing=1.6)
    fig.text(.055, .035, "Joseph Campagna, PSM", color=FG, size=14, weight="bold")
    fig.text(.945, .035, "STRUCTURAL BIOINFORMATICS", color=MUTED, size=10, ha="right")
    target = OUT / f"{slug}-categorical-nerve.png"
    fig.savefig(target, dpi=200, facecolor=BG)
    fig.savefig(ROOT / "paper" / "figures" / target.name, dpi=200, facecolor=BG)
    plt.close(fig)
    print(target)

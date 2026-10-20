"""Monochrome geometric views of the complete exported nerve 2-skeleta."""
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / "output" / "nerve-diagrams"
OUT.mkdir(parents=True, exist_ok=True)

for slug, title, file in [
    ("alanine", "Alanine dipeptide", "data.json"),
    ("chignolin", "Chignolin CLN025", "chignolin/data.json"),
]:
    data = json.loads((ROOT / "dist" / file).read_text())
    # The viewer uses y for height; matplotlib uses z.
    xyz = np.array([n["pos"] for n in data["nodes"]])[:, [0, 2, 1]]
    edges = np.array(data["edges"], dtype=int)
    triangles = np.array(data["chains"], dtype=int)
    assert edges.max() < len(xyz) and triangles.max() < len(xyz)
    fig = plt.figure(figsize=(12, 10), facecolor="white")
    ax = fig.add_axes([0, .09, 1, .84], projection="3d")
    ax.add_collection3d(Poly3DCollection(
        xyz[triangles], facecolors=(.5, .5, .5, .12),
        edgecolors="none", zsort="average"))
    ax.add_collection3d(Line3DCollection(
        xyz[edges], colors=(0, 0, 0, .8), linewidths=.65))
    ax.scatter(*xyz.T, s=9, color="black", depthshade=False, linewidths=0)
    lo, hi = xyz.min(axis=0), xyz.max(axis=0)
    center = (lo + hi) / 2
    span = hi - lo
    for setter, c, s in zip([ax.set_xlim, ax.set_ylim, ax.set_zlim], center, span):
        setter(c - s*.54, c + s*.54)
    ax.set_box_aspect(span)
    ax.view_init(elev=29, azim=-58)
    ax.set_proj_type("ortho")
    ax.set_axis_off()
    fig.text(.5, .94, title, ha="center", size=23, fontfamily="DejaVu Sans")
    fig.text(.5, .075,
             f"{len(xyz)} vertices  ·  {len(edges)} edges  ·  {len(triangles)} triangular faces",
             ha="center", size=11, color="black")
    fig.text(.5, .048, "Full exported overlap nerve (2-skeleton), embedded in landscape coordinates",
             ha="center", size=10, color="black")
    fig.text(.5, .022, "Joseph Campagna, PSM", ha="center", size=10, color="black")
    for directory in [OUT, ROOT / "paper" / "figures"]:
        fig.savefig(directory / f"{slug}-full-nerve.png", dpi=250, facecolor="white")
    fig.savefig(OUT / f"{slug}-full-nerve.svg", facecolor="white")
    plt.close(fig)
    print(OUT / f"{slug}-full-nerve.png")

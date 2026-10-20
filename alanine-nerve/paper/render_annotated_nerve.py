"""Two annotated viewpoints of each complete exported overlap nerve."""
import json
from pathlib import Path
import zipfile
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / "output" / "nerve-diagrams" / "annotated"
OUT.mkdir(parents=True, exist_ok=True)

for slug, title, source in [
    ("alanine", "Alanine dipeptide", "data.json"),
    ("chignolin", "Chignolin CLN025", "chignolin/data.json"),
]:
    d = json.loads((ROOT / "dist" / source).read_text())
    xyz = np.array([n["pos"] for n in d["nodes"]])[:, [0, 2, 1]]
    edges, faces = np.array(d["edges"]), np.array(d["chains"])
    ranks = np.array([len(n["simplex"]) for n in d["nodes"]])
    chain = faces[0]
    labels = [f"v{i} = " + "{" + ",".join(map(str, d["nodes"][i]["simplex"])) + "}" for i in chain]
    for layout in ["both", "oblique", "overhead"]:
        fig = plt.figure(figsize=(16, 10), facecolor="white")
        views = [("Oblique view", 30, -58), ("Overhead view", 90, -90)]
        if layout != "both":
            views = [views[0 if layout == "oblique" else 1]]
        fig.text(.05, .94, title + "  |  Landscape nerve", size=25)
        fig.text(.05, .903,
                 f"{len(xyz)} vertices · {len(edges)} inclusion edges · {len(faces)} triangular faces"
                 "   |   Complete exported 2-skeleton", size=12)
        axes = []
        for k, (name, elev, azim) in enumerate(views):
            rect = [.025 + k*.49, .36, .49, .50] if len(views) == 2 else [.08, .36, .84, .50]
            ax = fig.add_axes(rect, projection="3d")
            ax.add_collection3d(Poly3DCollection(xyz[faces], facecolors=(.4,.4,.4,.10), edgecolors="none"))
            ax.add_collection3d(Line3DCollection(xyz[edges], colors=(0,0,0,.55), linewidths=.7))
            for rank, marker in [(1,"o"), (2,"s"), (3,"^")]:
                p = xyz[ranks == rank]
                ax.scatter(*p.T, marker=marker, s=19, c="black", depthshade=False, linewidths=0)
            selected = np.array([[chain[0],chain[1]], [chain[1],chain[2]], [chain[0],chain[2]]])
            ax.add_collection3d(Line3DCollection(xyz[selected], colors="black", linewidths=2.1))
            ax.add_collection3d(Poly3DCollection([xyz[chain]], facecolors=(.15,.15,.15,.24), edgecolors="none"))
            lo, hi = xyz.min(0), xyz.max(0)
            center, span = (lo+hi)/2, hi-lo
            for setter,c,s in zip([ax.set_xlim,ax.set_ylim,ax.set_zlim],center,span):
                setter(c-s*.58,c+s*.58)
            ax.set_box_aspect(span)
            ax.view_init(elev=elev, azim=azim)
            ax.set_proj_type("ortho")
            ax.set_axis_off()
            ax.set_title(name, size=14, pad=-10)
            axes.append(ax)
        fig.canvas.draw()
        for ax in axes:
            for idx, offset in zip(chain, [(-75,45), (-90,65), (45,-45)]):
                x,y,_ = proj3d.proj_transform(*xyz[idx], ax.get_proj())
                ax.annotate(f"v{idx}", (x,y), xytext=offset, textcoords="offset points",
                            fontsize=11, weight="bold",
                            bbox=dict(boxstyle="round,pad=.2",fc="white",ec="none",alpha=.93),
                            arrowprops=dict(arrowstyle="-",color="black",lw=.7))
        handles = [
            Line2D([],[],color="black",marker="o",linestyle="",label="Vertex {i}: one cover region"),
            Line2D([],[],color="black",marker="s",linestyle="",label="Vertex {i,j}: witnessed pair overlap"),
            Line2D([],[],color="black",marker="^",linestyle="",label="Vertex {i,j,k}: witnessed triple overlap"),
            Line2D([],[],color="black",lw=.8,label="Edge: inclusion of overlap index sets"),
            Patch(facecolor=".85",edgecolor="black",lw=.5,label="Face: a composable chain of two inclusions"),
        ]
        fig.legend(handles=handles,loc="upper left",bbox_to_anchor=(.045,.335),
                   frameon=False,fontsize=11,labelspacing=.65)
        fig.text(.54,.31,"ANNOTATED SIMPLEX",size=12,weight="bold")
        fig.text(.54,.275,"  →  ".join(labels),size=11)
        fig.text(.54,.25,
                 "Bold edges outline this inclusion chain and its composite.\n"
                 "Every plotted point is a vertex of the face-poset nerve;\n"
                 "marker shapes distinguish the size of its index set.\n"
                 "Edges express overlap inclusion, not MD transitions.",
                 size=11,linespacing=1.5,va="top")
        coordinates = ("Horizontal plane: dihedral chart (φ, ψ). Height: viewer-scaled free energy."
                       if slug == "alanine" else
                       "Horizontal plane: radius of gyration and end-to-end distance. Height: pooled-occupancy score.")
        fig.text(.05,.105,coordinates,size=11)
        fig.text(.05,.076,
                 "Same coordinates and connectivity in both views; projected crossings do not create vertices."
                 + (" CLN025 heights are not equilibrium free energies." if slug=="chignolin" else ""),
                 size=10)
        fig.text(.05,.035,"Joseph Campagna, PSM",size=12,weight="bold")
        name = f"{slug}-nerve-annotated-{layout}"
        fig.savefig(OUT / (name+".png"),dpi=200,facecolor="white")
        fig.savefig(OUT / (name+".svg"),facecolor="white")
        if layout == "both":
            fig.savefig(ROOT / "paper" / "figures" / (name+".png"),
                        dpi=200, facecolor="white")
        plt.close(fig)
with zipfile.ZipFile(OUT / "annotated-nerve-views.zip","w",zipfile.ZIP_DEFLATED) as z:
    for file in sorted(OUT.glob("*.png")):
        z.write(file,file.name)
    for file in sorted(OUT.glob("*.svg")):
        z.write(file,file.name)
print(OUT)

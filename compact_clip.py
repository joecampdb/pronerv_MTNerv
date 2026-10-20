"""Closer view of a fixed 25–35 ns interval from GROMACS-prepared backbones."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter,PillowWriter
from mpl_toolkits.mplot3d.art3d import Line3DCollection
out=Path(__file__).resolve().parent/"reports/compact_comparison"
d=np.load(out/"backbones.npz")
t=d["times_ns"]; sel=np.flatnonzero((t>=25)&(t<=35))
x=[d["rep01"],d["rep02"]]
limit=max(np.abs(a[sel]).max() for a in x)+.1
fig=plt.figure(figsize=(10,5))
lines=[];titles=[]
for i in range(2):
    ax=fig.add_subplot(1,2,i+1,projection="3d")
    line=Line3DCollection([],cmap="viridis",linewidths=3)
    line.set_array(np.arange(49));line.set_clim(0,49);ax.add_collection(line)
    ax.set(xlim=(-limit,limit),ylim=(-limit,limit),zlim=(-limit,limit))
    ax.set_box_aspect([1,1,1],zoom=1.4);ax.set_proj_type("ortho");ax.view_init(25,-65);ax.set_axis_off()
    titles.append(ax.set_title(""));lines.append(line)
fig.suptitle("Closer view: fixed 25–35 ns interval, unfiltered chronological frames\nSame scale and common GROMACS reference fit; backbone only")
fig.subplots_adjust(top=.75,bottom=.02,left=.02,right=.98,wspace=.02)
def update(k):
    for i in range(2):
        s=x[i][k]
        lines[i].set_segments(np.stack([s[:-1],s[1:]],axis=1))
        titles[i].set_text(f"Replica {i+1} | {t[k]:.1f} ns\nRg {np.sqrt((s*s).sum(1).mean()):.2f} nm")
movie=FFMpegWriter(fps=10,codec="libx264",extra_args=["-pix_fmt","yuv420p"])
with movie.saving(fig,str(out/"compact_closeup.mp4"),dpi=120):
    for k in sel: update(k);movie.grab_frame()
gif=PillowWriter(fps=10)
with gif.saving(fig,str(out/"compact_closeup.gif"),dpi=90):
    for k in sel: update(k);gif.grab_frame()
plt.close(fig)

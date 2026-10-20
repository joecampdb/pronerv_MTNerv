"""Packing comparison around the PE25 rep01 expansion; no simulation changes."""
import json
from pathlib import Path
import numpy as np
from scipy.spatial.distance import cdist
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from analyze import unwrap_chain, metrics

root=Path(__file__).resolve().parent
out=root/"reports/PE25_rep01"
data=np.load(out/"contact_frames.npz")
t=data["times_ns"]; xyz=data["shapes"]
ij=np.triu_indices(50,4)
dist=np.array([cdist(s,s)[ij] for s in xyz])
c=dist<.5
windows={"Before":(72,75),"After":(80,83),"Later":(90,93)}
def mask(bounds): return (t>=bounds[0]) & (t<bounds[1])
def rmsd(a,b):
    a=a-a.mean(0); b=b-b.mean(0)
    u,_,vh=np.linalg.svd(a.T@b)
    d=np.linalg.det(u@vh)
    rot=u@np.diag([1,1,d])@vh
    return float(np.sqrt(np.mean(np.sum((a@rot-b)**2,axis=1))))
def jac(a,b):
    union=np.maximum(a,b).sum()
    return float(np.minimum(a,b).sum()/union) if union else 1.
def comparison(a,b):
    return {"occupancy_RMS_difference":float(np.sqrt(np.mean((a-b)**2))),
            "weighted_Jaccard":jac(a,b)}
means={name:c[mask(w)].mean(0) for name,w in windows.items()}
# Typical snapshot: minimizes squared distance to its window's mean contact vector.
reps={}
for name,w in windows.items():
    ids=np.flatnonzero(mask(w))
    index=ids[np.argmin(((c[ids]-means[name])**2).sum(1))]
    reps[name]=(float(t[index]),xyz[index])
import MDAnalysis as mda
folder=root/"runs/PE25/rep01"
u=mda.Universe(str(folder/"prod.gro"),str(folder/"prod.xtc"))
ts=u.trajectory[76520]
assert abs(ts.time-76520)<.1
peak=unwrap_chain(u.atoms[:50].positions/10,ts.dimensions[:3]/10)
peak-=peak.mean(0)
reps["Expanded"]=(ts.time/1000,peak)
report={"method":"Contact medoids of prespecified 72–75, 80–83, 90–93 ns windows; peak Rg frame 76.52 ns. Fixed atom identities. No reflection in RMSD alignment.",
        "windows_ns":windows,"snapshots":{},"window_comparisons":{},"sensitivity":[]}
for name,(time,s) in reps.items():
    contacts=cdist(s,s)[ij]<.5
    ref=cdist(reps["Before"][1],reps["Before"][1])[ij]<.5
    report["snapshots"][name]={"time_ns":float(time),"rg_nm":float(np.sqrt((s*s).sum(1).mean())),
        "contacts":int(contacts.sum()),"contacts_shared_with_before":int((contacts&ref).sum()),
        "contact_Jaccard_with_before":jac(contacts,ref),"aligned_RMSD_to_before_nm":rmsd(s,reps["Before"][1])}
    np.savetxt(out/f"backbone_{name.lower()}.xyz",s*10,header=f"50\nPE25 carbons at {time:.2f} ns, coordinates in angstrom",comments="",fmt="C %.6f %.6f %.6f")
for name in ["After","Later"]:
    report["window_comparisons"][name]=comparison(means["Before"],means[name])
# Equal-duration, disjoint reference windows inside the earlier compact period.
controls=[(a,a+3) for a in range(20,63,3)]
for cutoff in [.45,.5,.55]:
    for separation in [4,8]:
        valid=ij[1]-ij[0]>=separation
        cc=(dist[:,valid]<cutoff)
        base=np.array([cc[mask(w)].mean(0) for w in controls])
        diffs=[float(np.sqrt(np.mean((a-b)**2))) for i,a in enumerate(base) for b in base[i+1:]]
        entry={"cutoff_nm":cutoff,"sequence_separation":separation,
               "reference_pairs":len(diffs),"reference_RMS_quantiles":np.quantile(diffs,[.05,.5,.95]).tolist()}
        for name in ["After","Later"]:
            a=cc[mask(windows["Before"])].mean(0); b=cc[mask(windows[name])].mean(0)
            delta=float(np.sqrt(np.mean((a-b)**2)))
            entry[name]={"RMS":delta,"reference_percentile":100*float(np.mean(np.array(diffs)<=delta))}
        report["sensitivity"].append(entry)
# Contact survival from the before window, relative to other compact reference windows.
report["baseline_window_weighted_Jaccard"]=[
    jac(c[mask(a)].mean(0),c[mask(b)].mean(0))
    for i,a in enumerate(controls) for b in controls[i+1:]]
report["reference_note"]="Overlapping information and time correlation: percentiles are descriptive, not p-values. Reference windows are 20–65 ns in 3 ns blocks."
(out/"expansion_comparison.json").write_text(json.dumps(report,indent=2))

fig=plt.figure(figsize=(14,4.5))
order=["Before","Expanded","After","Later"]
display={}
for name,(_,s) in reps.items():
    _,_,vh=np.linalg.svd(s,full_matrices=False)
    if np.linalg.det(vh)<0: vh[-1]*=-1
    display[name]=s@vh.T
limit=max(np.abs(s).max() for s in display.values())+.1
for k,name in enumerate(order):
    ax=fig.add_subplot(1,4,k+1,projection="3d")
    time,s=reps[name]
    s=display[name]
    segments=np.stack([s[:-1],s[1:]],axis=1)
    lc=Line3DCollection(segments,cmap="viridis",linewidths=2.5)
    lc.set_array(np.arange(49)); lc.set_clim(0,49); ax.add_collection(lc)
    ax.scatter(*s.T,c=np.arange(50),cmap="viridis",vmin=0,vmax=49,s=12,depthshade=False)
    ax.text(*s[0],"C1",fontsize=8); ax.text(*s[-1],"C50",fontsize=8)
    ax.set(xlim=(-limit,limit),ylim=(-limit,limit),zlim=(-limit,limit))
    ax.set_box_aspect([1,1,1],zoom=1.5); ax.view_init(15,-80)
    ax.set_proj_type("ortho")
    ax.set_axis_off()
    r=report["snapshots"][name]
    ax.set_title(f"{name}: {time:.2f} ns\nRg {r['rg_nm']:.2f} nm; {r['contacts']} contacts",fontsize=11)
fig.suptitle("Actual PE25 backbones • identical scale • independently rotated for visibility • color C1 → C50\nCompact snapshots represent 3 ns windows; expanded snapshot is the Rg maximum. Water/H omitted.",fontsize=12)
fig.subplots_adjust(left=.01,right=.99,bottom=.02,top=.74,wspace=.02)
fig.savefig(out/"expansion_structures.png",dpi=180); plt.close(fig)

def matrix(v):
    a=np.full((50,50),np.nan); a[ij]=v; a[(ij[1],ij[0])]=v
    return a
fig,axes=plt.subplots(1,4,figsize=(14,4),layout="constrained")
for ax,name in zip(axes[:3],["Before","After","Later"]):
    im=ax.imshow(matrix(means[name]),origin="lower",vmin=0,vmax=1,cmap="viridis",extent=(.5,50.5,.5,50.5))
    ax.set_title(f"{name}: {windows[name][0]}–{windows[name][1]} ns")
    ax.set_xlabel("Carbon index"); ax.set_ylabel("Carbon index")
fig.colorbar(im,ax=list(axes[:3]),shrink=.7,label="Contact occupancy")
im=axes[3].imshow(matrix(means["After"]-means["Before"]),origin="lower",vmin=-1,vmax=1,cmap="RdBu_r",extent=(.5,50.5,.5,50.5))
axes[3].set_title("After − before"); axes[3].set_xlabel("Carbon index")
fig.colorbar(im,ax=axes[3],shrink=.7,label="Occupancy change")
fig.suptitle("Contact identities: C–C distance <0.50 nm, sequence separation ≥4 bonds")
fig.savefig(out/"expansion_contacts.png",dpi=170); plt.close(fig)
print(json.dumps(report,indent=2))

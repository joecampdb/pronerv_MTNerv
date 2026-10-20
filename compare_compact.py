"""Completed PE25 replicas: GROMACS preparation, compact-ensemble diagnostics and movie."""
import json, subprocess, hashlib
from pathlib import Path
import numpy as np
from scipy.spatial.distance import cdist
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter, PillowWriter
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import MDAnalysis as mda

ROOT=Path(__file__).resolve().parent
OUT=ROOT/"reports/compact_comparison"; OUT.mkdir(exist_ok=True,parents=True)
GMX=str(ROOT/"vendor/gromacs-install/bin/gmx")
frozen=hashlib.sha256((ROOT/"transition_definition.json").read_bytes()).hexdigest()
assert frozen==json.loads((ROOT/"reports/transition_events/report.json").read_text())["definition_sha256"]
index=OUT/"backbone.ndx"
index.write_text("[ Backbone ]\n"+" ".join(map(str,range(1,51)))+"\n")
def call(args,stdin,name):
    with (OUT/name).open("w") as log:
        subprocess.run([GMX]+args,input=stdin,text=True,stdout=log,stderr=log,check=True)

xyz=[]; scalars=[]; cores=[]; paths=[]
for rep in ["rep01","rep02"]:
    folder=ROOT/"runs/PE25"/rep
    assert (folder/"prod.done.json").exists()
    whole=OUT/f"{rep}_whole.xtc"; gro=OUT/f"{rep}_reference.gro"
    if not whole.exists():
        call(["trjconv","-s",str(folder/"prod.tpr"),"-f",str(folder/"prod.xtc"),
              "-n",str(index),"-o",str(whole),"-pbc","whole","-dt","100","-b","20000","-e","100000"],
              "0\n",f"{rep}_whole.log")
    if not gro.exists():
        call(["trjconv","-s",str(folder/"prod.tpr"),"-f",str(folder/"prod.xtc"),
              "-n",str(index),"-o",str(gro),"-pbc","whole","-dump","20000"],
              "0\n",f"{rep}_reference.log")
    fitted=OUT/f"{rep}_fitted.xtc"
    if not fitted.exists():
        call(["trjconv","-s",str(OUT/"rep01_reference.gro"),"-f",str(whole),"-n",str(index),
              "-o",str(fitted),"-fit","rot+trans"],"0\n0\n",f"{rep}_fit.log")
    u=mda.Universe(str(gro),str(fitted))
    times=[]; shapes=[]
    for ts in u.trajectory:
        s=u.atoms.positions.copy()/10; shapes.append(s-s.mean(0)); times.append(ts.time/1000)
    shapes=np.array(shapes); times=np.array(times)
    assert len(times)==801 and np.allclose(times,np.arange(20,100.01,.1))
    assert np.max(np.linalg.norm(np.diff(shapes,axis=1),axis=2))<.20
    obs=json.loads((ROOT/f"reports/transition_events/{rep}_observables.json").read_text())
    obs=[obs[int(round(t*1000/10))] for t in times]
    assert np.max(np.abs(np.sqrt((shapes**2).sum(2).mean(1))-np.array([r["rg_nm"] for r in obs])))<.003
    labels=np.genfromtxt(ROOT/f"reports/transition_events/{rep}_states.csv",delimiter=",",names=True)
    core=labels["core_label_minus1_undecided_0_C_1_E"][np.rint(times*100).astype(int)]==0
    xyz.append(shapes); scalars.append(obs); cores.append(core)
    paths.append(str(fitted))
    print(rep,"GROMACS preparation verified",flush=True)

ij=np.triu_indices(50,4)
dist=[np.array([cdist(s,s)[ij] for s in traj]) for traj in xyz]
contacts=[d<.5 for d in dist]
report=dict(definition_sha256=frozen,interval_ns=[20,100],sampling_ps=100,
            conditioning="Frozen compact-core labels on trailing-median observables; same definition in both replicas.",
            warning="Single trajectories per preparation. Descriptive comparisons, not independent-sample significance tests or proof of equilibrium.",
            replicas={},sensitivity=[])
features=["rg_nm","anisotropy","contacts_per_carbon","nematic_order","trans_fraction","hydration_waters"]
for i,rep in enumerate(["rep01","rep02"]):
    report["replicas"][rep]={"compact_sample_fraction":float(cores[i].mean()),"features":{}}
    for f in features:
        v=np.array([r[f] for r in scalars[i]])[cores[i]]
        report["replicas"][rep]["features"][f]=dict(mean=float(v.mean()),std=float(v.std()),
            quantiles_05_50_95=np.quantile(v,[.05,.5,.95]).tolist())

for cutoff in [.45,.5,.55]:
    for sep in [4,8]:
        valid=ij[1]-ij[0]>=sep
        cc=[d[:,valid]<cutoff for d in dist]
        means=[c[mask].mean(0) for c,mask in zip(cc,cores)]
        blocks=[]
        for i in range(2):
            bs=[]
            for start in range(20,100,5):
                keep=cores[i] & (times>=start)&(times<start+5)
                if keep.sum()>=20: bs.append(cc[i][keep].mean(0))
            blocks.append(np.array(bs))
        within=[cdist(b,b)/np.sqrt(valid.sum()) for b in blocks]
        within=[a[np.triu_indices(len(a),1)] for a in within]
        between=(cdist(*blocks)/np.sqrt(valid.sum())).ravel()
        entry=dict(cutoff_nm=cutoff,separation=sep,
                   whole_window_mean_contact_RMS_difference=float(np.sqrt(np.mean((means[0]-means[1])**2))),
                   block_within_median=[float(np.median(a)) for a in within],
                   block_between_median=float(np.median(between)),
                   block_within_05_95=[np.quantile(a,[.05,.95]).tolist() for a in within],
                   block_between_05_95=np.quantile(between,[.05,.95]).tolist())
        report["sensitivity"].append(entry)

# Contact-pattern memory, conditioned on compact endpoints. No trajectory time compression.
memory=[]
for c,core in zip(contacts,cores):
    p=c[core].mean(0); centered=c.astype(float)-p
    rows=[]
    for lag in [1,2,5,10,20,50,100]:
        keep=core[:-lag]&core[lag:]
        a=centered[:-lag][keep]; b=centered[lag:][keep]
        corr=float(np.sum(a*b)/np.sqrt(np.sum(a*a)*np.sum(b*b)))
        rows.append(dict(lag_ns=lag*.1,normalized_contact_memory=corr,endpoint_pairs=int(keep.sum())))
    memory.append(rows)
report["contact_memory"]=memory

def rmsd(a,b):
    u,_,vh=np.linalg.svd(a.T@b)
    rot=u@np.diag([1,1,np.linalg.det(u@vh)])@vh
    return float(np.sqrt(np.mean(np.sum((a@rot-b)**2,axis=1))))
rng=np.random.default_rng(174209); rms={}
for label,i,j in [("within_rep01",0,0),("within_rep02",1,1),("between",0,1)]:
    values=[]
    ai=np.flatnonzero(cores[i]); bj=np.flatnonzero(cores[j])
    for _ in range(3000):
        a=int(rng.choice(ai)); b=int(rng.choice(bj))
        if i==j and abs(a-b)<50: continue
        values.append(rmsd(xyz[i][a],xyz[j][b]))
    rms[label]=dict(median_nm=float(np.median(values)),quantiles_05_95_nm=np.quantile(values,[.05,.95]).tolist(),pairs=len(values))
report["aligned_backbone_RMSD"]=rms
(OUT/"comparison.json").write_text(json.dumps(report,indent=2))
np.savez_compressed(OUT/"backbones.npz",times_ns=times,rep01=xyz[0],rep02=xyz[1],compact01=cores[0],compact02=cores[1])

fig,axs=plt.subplots(2,3,figsize=(12,7),layout="constrained")
for ax,f in zip(axs.ravel()[:4],["rg_nm","contacts_per_carbon","nematic_order","hydration_waters"]):
    for i,color in enumerate(["#376a92","#c47a35"]):
        v=np.array([r[f] for r in scalars[i]])[cores[i]]
        ax.hist(v,bins=30,density=True,histtype="step",lw=1.5,label=f"Replica {i+1}",color=color)
    ax.set_xlabel(f); ax.set_ylabel("Density")
axs[0,0].legend()
for i in range(2):
    axs[1,1].plot([v["lag_ns"] for v in memory[i]],[v["normalized_contact_memory"] for v in memory[i]],"o-",label=f"Replica {i+1}")
axs[1,1].set(xlabel="Lag (ns), compact endpoints",ylabel="Contact memory"); axs[1,1].legend()
entry=report["sensitivity"][2]
axs[1,2].bar(["Within 1","Within 2","Between"],entry["block_within_median"]+[entry["block_between_median"]])
axs[1,2].set(ylabel="Median 5 ns contact-block RMS difference")
fig.suptitle("PE25 compact-core ensembles, 20–100 ns • definition unchanged")
fig.savefig(OUT/"ensemble_comparison.png",dpi=160);plt.close(fig)

means=[c[core].mean(0) for c,core in zip(contacts,cores)]
fig,axs=plt.subplots(1,3,figsize=(12,4),layout="constrained")
for ax,v,title in zip(axs,[means[0],means[1],means[1]-means[0]],["Replica 1 compact","Replica 2 compact","Replica 2 − replica 1"]):
    mat=np.full((50,50),np.nan);mat[ij]=v;mat[(ij[1],ij[0])]=v
    diff=title.startswith("Replica 2 −")
    im=ax.imshow(mat,origin="lower",vmin=-.3 if diff else 0,vmax=.3 if diff else 1,cmap="RdBu_r" if diff else "viridis",extent=(.5,50.5,.5,50.5))
    ax.set(title=title,xlabel="Carbon index",ylabel="Carbon index")
    fig.colorbar(im,ax=ax,shrink=.7)
fig.savefig(OUT/"compact_contacts.png",dpi=160);plt.close(fig)

# Both movies retain chronological time, including noncompact excursions.
# GROMACS removes PBC and aligns both to a common reference; no invented/interpolated frames.
fig=plt.figure(figsize=(10,5),facecolor="white")
axes=[]; lines=[]; texts=[]
movie_limit=max(float(np.abs(s).max()) for s in xyz)+.15
for i in range(2):
    ax=fig.add_subplot(1,2,i+1,projection="3d")
    lc=Line3DCollection([],cmap="viridis",linewidths=3);lc.set_array(np.arange(49));lc.set_clim(0,49);ax.add_collection(lc)
    ax.set(xlim=(-movie_limit,movie_limit),ylim=(-movie_limit,movie_limit),zlim=(-movie_limit,movie_limit))
    ax.set_box_aspect([1,1,1],zoom=1.35);ax.set_proj_type("ortho");ax.view_init(25,-65);ax.set_axis_off()
    text=ax.set_title("");axes.append(ax);lines.append(lc);texts.append(text)
fig.suptitle("PE25: matched GROMACS trajectories, same scale and reference fit\nBackbone C1 → C50 colored purple → yellow; water/H omitted",fontsize=12)
fig.subplots_adjust(top=.75,bottom=.05,left=.02,right=.98,wspace=.02)
def update(k):
    for i in range(2):
        s=xyz[i][k];lines[i].set_segments(np.stack([s[:-1],s[1:]],axis=1))
        texts[i].set_text(f"Replica {i+1} | {times[k]:.1f} ns\nRg {scalars[i][k]['rg_nm']:.2f} nm | "+("compact core" if cores[i][k] else "outside compact core"))
writer=FFMpegWriter(fps=20,codec="libx264",extra_args=["-pix_fmt","yuv420p","-crf","20"])
with writer.saving(fig,str(OUT/"pe25_comparison.mp4"),dpi=110):
    for k in range(len(times)): update(k);writer.grab_frame()
print("Full paired movie rendered",flush=True)
preview=PillowWriter(fps=5)
with preview.saving(fig,str(OUT/"pe25_comparison_preview.gif"),dpi=85):
    for k in range(0,len(times),10):
        update(k);preview.grab_frame()
plt.close(fig)
assert hashlib.sha256((ROOT/"transition_definition.json").read_bytes()).hexdigest()==frozen
print(json.dumps(report,indent=2))

"""Read-only trajectory review for completed PE25/rep01; writes analysis artifacts."""
import json
from pathlib import Path
import numpy as np
from scipy.cluster.vq import kmeans2
from scipy.spatial.distance import cdist
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from analyze import extract, energy_checks, committed_labels, unwrap_chain

ROOT = Path(__file__).resolve().parent
folder = ROOT / "runs/PE25/rep01"
out = ROOT / "reports/PE25_rep01"
out.mkdir(parents=True, exist_ok=True)
assert (folder / "prod.done.json").exists()
cache = out / "observables.json"
if cache.exists():
    rows = json.loads(cache.read_text())
else:
    rows = extract(folder, 10)
    cache.write_text(json.dumps(rows))
print("Structural observables extracted", flush=True)
t = np.array([r["time_ps"] for r in rows]) / 1000
assert t[-1] >= 100
features = ["rg_nm", "anisotropy", "contacts_per_carbon", "nematic_order", "trans_fraction"]
x = np.array([[r[f] for f in features] for r in rows])
report = dict(replica="PE25/rep01", preparation="compact", end_ns=float(t[-1]),
              sampling_ps=10, blocks=[], sensitivity=[])
for lo in range(0, 100, 10):
    block = x[(t >= lo) & (t < lo+10)]
    report["blocks"].append(dict(start_ns=lo, means=dict(zip(features, block.mean(0).tolist())),
                                std=dict(zip(features, block.std(0).tolist()))))
for discard in [0, 10, 20, 40]:
    keep = t >= discard
    z = (x[keep]-x[keep].mean(0))/np.maximum(x[keep].std(0), 1e-8)
    centers, _ = kmeans2(z, 2, minit="++", seed=174209)
    d = cdist(z, centers)
    labels = d.argmin(1)
    labels[np.abs(d[:,0]-d[:,1])/np.maximum(d.sum(1),1e-12) < .15] = -1
    counts = {}
    for dwell in [50,100,200,500,1000,2000]:
        events = committed_labels(labels, t[keep]*1000, dwell)
        counts[str(dwell)] = dict(forward=sum(a[1]==0 and b[1]==1 for a,b in zip(events,events[1:])),
                                 reverse=sum(a[1]==1 and b[1]==0 for a,b in zip(events,events[1:])),
                                 entries_ns=[[a/1000,b] for a,b in events])
    report["sensitivity"].append(dict(discard_ns=discard, ambiguous_fraction=float(np.mean(labels<0)),
        centers=(centers*x[keep].std(0)+x[keep].mean(0)).tolist(), counts=counts))
    if discard == 20:
        main_labels=labels
thermo, warnings = energy_checks(folder, str(ROOT/"vendor/gromacs-install/bin/gmx"))
report.update(thermodynamics=thermo, warnings=warnings,
              min_image_clearance_nm=min(r["image_distance_or_lower_bound_nm"] for r in rows),
              max_cc_bond_nm=max(r["max_cc_bond_nm"] for r in rows))

# Independent contact-identity inspection at 100 ps, avoiding a full-system distance matrix.
import MDAnalysis as mda
u=mda.Universe(str(folder/"prod.gro"), str(folder/"prod.xtc"))
ij=np.triu_indices(50,4)
contacts=[]; ct=[]; shapes=[]
for ts in u.trajectory[::100]:
    chain=unwrap_chain(u.atoms[:50].positions/10, ts.dimensions[:3]/10)
    contacts.append((cdist(chain,chain)[ij]<.5).astype(float))
    ct.append(ts.time/1000)
    shapes.append(chain-chain.mean(0))
c=np.array(contacts); ct=np.array(ct)
np.savez_compressed(out/"contact_frames.npz",times_ns=ct,contacts=c,shapes=shapes)
block_c=np.array([c[(ct>=a)&(ct<a+10)].mean(0) for a in range(0,100,10)])
report["contact_block_rms_difference"] = (cdist(block_c,block_c)/np.sqrt(c.shape[1])).tolist()
fig,ax=plt.subplots(5,1,figsize=(12,10),sharex=True)
for a,f,title in zip(ax[:4],["rg_nm","contacts_per_carbon","nematic_order","hydration_waters"],
                     ["Backbone Rg (nm)","Contacts / carbon","Alignment","Hydration waters"]):
    v=np.array([r[f] for r in rows])
    a.plot(t,v,color="#507e99",alpha=.45,lw=.45)
    n=(len(t)//100)*100
    a.plot(t[:n].reshape(-1,100).mean(1),v[:n].reshape(-1,100).mean(1),color="#132f45",lw=1.4)
    a.set_ylabel(title); a.axvline(20,color="gray",ls="--")
ax[4].scatter(t[t>=20],main_labels,s=1,color="#895425")
ax[4].set_yticks([-1,0,1],["Ambiguous","A","B"])
ax[4].set_ylabel("Exploratory\ncluster"); ax[4].set_xlabel("Production time (ns)")
fig.suptitle("PE25 replica 1: compact start, 100 ns\nThin: 10 ps samples; bold: 1 ns means. Clusters are not validated states.")
fig.tight_layout(); fig.savefig(out/"trajectory_review.png",dpi=150); plt.close(fig)
fig,ax=plt.subplots(1,3,figsize=(13,4))
for a,i,j in [(ax[0],0,2),(ax[1],0,3)]:
    a.hexbin(x[t>=20,i],x[t>=20,j],gridsize=40,mincnt=1,cmap="viridis")
    a.set_xlabel(features[i]); a.set_ylabel(features[j])
im=ax[2].imshow(cdist(block_c,block_c)/np.sqrt(c.shape[1]),origin="lower",cmap="magma")
ax[2].set_xlabel("10 ns block"); ax[2].set_ylabel("10 ns block")
ax[2].set_title("Contact-occupancy RMS difference")
fig.colorbar(im,ax=ax[2]); fig.tight_layout(); fig.savefig(out/"packing_review.png",dpi=150)
(out/"review.json").write_text(json.dumps(report,indent=2))
print(json.dumps({k:v for k,v in report.items() if k not in ["sensitivity","contact_block_rms_difference"]},indent=2))
print("Crossings:",[(s["discard_ns"], {d:[v["forward"],v["reverse"]] for d,v in s["counts"].items()}) for s in report["sensitivity"]])

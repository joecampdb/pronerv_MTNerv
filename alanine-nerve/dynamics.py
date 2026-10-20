"""Empirical core-to-core passages; independent runs are never concatenated."""
from pathlib import Path
import json
import numpy as np
from scipy.ndimage import gaussian_filter, maximum_filter, map_coordinates

ROOT = Path(__file__).parent
raw = np.load(ROOT/"data/alanine-dipeptide-3x250ns-backbone-dihedrals.npz")
atomic = np.load(ROOT/"data/alanine-dipeptide-3x250ns-heavy-atom-positions.npz")
runs = [np.rad2deg(raw[k]).astype(float) for k in raw]
all_angles = np.concatenate(runs)
hist = np.histogram2d(*all_angles.T, bins=60, range=[[-180,180]]*2)[0]
density = gaussian_filter(hist,1.4,mode="wrap")
peaks = np.argwhere((density == maximum_filter(density,size=9,mode="wrap")) & (density > density.max()*.005))
peaks = sorted(peaks,key=lambda p:-density[tuple(p)])
centers = np.array(peaks)*6-177
assert len(centers)==4, "Review basin construction if the input dataset changes"
def delta(a,b):
    return (a-b+180)%360-180
free = np.array(json.loads((ROOT/"dist/data.json").read_text())["freeEnergy"])
def pos(a):
    single=np.asarray(a).ndim==1
    a=np.atleast_2d(a)
    e=map_coordinates(free, np.stack([(a[...,0]+180)/12-.5,(a[...,1]+180)/12-.5]),order=1,mode="grid-wrap")
    result=np.stack([a[...,0]/12,e*1.3+2.8,a[...,1]/12],axis=-1)
    return result[0] if single else result

events = {}
labels = []
pop = np.zeros(4,int)
initial_unassigned = []
for run,angles in enumerate(runs):
    distances=np.linalg.norm(delta(angles[:,None,:],centers[None,:,:]),axis=2)
    nearest=distances.argmin(1)
    # Disjoint 25-degree cores; retain the last visited core in intervening regions.
    cores=np.where(distances.min(1)<=25,nearest,-1)
    assigned=np.full(len(angles),-1,int)
    current=-1; last_core=-1
    for t,c in enumerate(cores):
        if c>=0:
            if current>=0 and c!=current:
                events.setdefault((current,int(c)),[]).append((run,last_core,t))
            current=int(c); last_core=t
        assigned[t]=current
    labels.append(assigned)
    initial_unassigned.append(int((assigned<0).sum()))
    pop+=np.bincount(assigned[assigned>=0],minlength=4)

lag_models={}
for lag in (10,50,100):
    per_run=[]
    for assigned in labels:
        left,right=assigned[:-lag],assigned[lag:]
        valid=(left>=0)&(right>=0)
        count=np.zeros((4,4),int)
        np.add.at(count,(left[valid],right[valid]),1)
        assert count.sum()==valid.sum()
        per_run.append(count)
    counts=sum(per_run)
    probabilities=counts/counts.sum(1)[:,None]
    assert np.allclose(probabilities.sum(1),1)
    lag_models[str(lag)]=dict(counts=counts.tolist(),probabilities=probabilities.tolist(),
                             perRunCounts=[c.tolist() for c in per_run])

basins=[dict(id=i,name=chr(65+i),angles=c.tolist(),pos=pos(c).tolist(),
             occupancy=float(pop[i]/pop.sum()),exposureNs=float(pop[i]/1000)) for i,c in enumerate(centers)]
edges=[]
for (i,j),ev in sorted(events.items()):
    durations=np.array([end-start for _,start,end in ev])
    # Select a real event closest to the median duration; no invented route.
    sample=ev[int(np.argmin(abs(durations-np.median(durations))))]
    run,start,end=sample
    path=runs[run][start:end+1]
    atoms=atomic[f"arr_{run}"][start:end+1].reshape(-1,10,3).astype(float)
    atoms-=atoms.mean(axis=1,keepdims=True)
    # Unwrap before temporal resampling, then cut the chart again for display.
    unwrapped=np.rad2deg(np.unwrap(np.deg2rad(path),axis=0))
    times=np.linspace(0,len(path)-1,min(160,max(2,len(path))))
    route=np.stack([np.interp(times,np.arange(len(path)),unwrapped[:,k]) for k in range(2)],axis=1)
    route=(route+180)%360-180
    per_run=[sum(r==k for r,_,_ in ev) for k in range(3)]
    edges.append(dict(id=len(edges),source=i,target=j,count=len(ev),perRunCounts=per_run,
                      grossEventsPerNs=len(ev)/750,conditionalEventsPerNs=len(ev)/(pop[i]/1000),
                      medianDurationPs=float(np.median(durations)),
                      representative=dict(run=run+1,startPs=start,endPs=end,angles=route.round(5).tolist(),
                                          molecularFrames=atoms.round(7).tolist(),
                                          frameAngles=path.round(7).tolist(),
                                          positions=pos(route).round(5).tolist())))
chains=[[a["id"],b["id"]] for a in edges for b in edges if a["target"]==b["source"]]
for x,y in chains:
    assert edges[x]["target"]==edges[y]["source"]
assert all(e["count"]==sum(e["perRunCounts"]) for e in edges)
out=dict(basins=basins,edges=edges,chains=chains,lagModels=lag_models,coreRadiusDeg=25,
         initialUnassignedFrames=initial_unassigned,
         method="Periodic density modes; disjoint angular cores; last-core assignment; empirical independent-run counts.",
         durationNs=750,frameSpacingPs=1)
(ROOT/"dist/dynamics.json").write_text(json.dumps(out,separators=(",",":")))
print(json.dumps(dict(basins=basins,edges=[{k:e[k] for k in ("source","target","count","perRunCounts","medianDurationPs")} for e in edges],chains=len(chains)),indent=2))

"""Rebuild a full-deposit witnessed cover and supported mobility visualization.

Maximal simplices are preserved without dimension truncation. The face-poset
display is explicitly the nerve of the 2-skeleton's face poset. No physical
time, equilibrium energy, or good-cover equivalence is asserted.
"""
import itertools,json
import numpy as np
from robustness import ROOT, OUT, height, metric_features, lineage_groups, initial_cohort_groups, complex_stats
from close_limitations import write

def periodic_delta(a,b,period=None):
 d=np.asarray(a)-np.asarray(b)
 return (d+period/2)%period-period/2 if period is not None else d

def maximal_masks(masks):
 kept=[]
 for m in sorted(set(map(int,masks))-{0},key=lambda x:(-x.bit_count(),x)):
  if not any(m&k==m for k in kept):kept.append(m)
 return kept

def masks_to_faces(masks,max_size=None):
 out=set()
 for mask in masks:
  v=[i for i in range(int(mask).bit_length()) if int(mask)&(1<<i)]
  for k in range(1,min(len(v),max_size or len(v))+1):out.update(itertools.combinations(v,k))
 return sorted(out,key=lambda x:(len(x),x))

def build_cover(q,h,period=None):
 # Fixed occupied-grid candidates; descriptive cover fit uses full data.
 lo,hi=np.array(h['limits']);bins=30
 ij=np.floor((q-lo)/(hi-lo)*bins).astype(int);ij=np.clip(ij,0,bins-1)
 hist=np.bincount(ij[:,0]*bins+ij[:,1],minlength=bins*bins).reshape(bins,bins)
 cand=np.array([lo+(np.array([i,j])+.5)/bins*(hi-lo) for i,j in zip(*np.where(hist>=25))])
 scale=np.ones(2) if period else q.std(0)
 ids=[int(np.argmax([hist[tuple(np.clip(((p-lo)/(hi-lo)*bins).astype(int),0,bins-1))] for p in cand]))]
 for _ in range(17):
  dis=np.linalg.norm(periodic_delta(cand[:,None],cand[ids],period)/scale,axis=2)
  ids.append(int(dis.min(1).argmax()))
 centers=cand[ids];radius=55. if period else .8
 delta=periodic_delta(q[:,None],centers,period)/scale
 dis=np.linalg.norm(delta,axis=2)
 membership=dis<=radius
 bit=(membership.astype(np.uint32)*(1<<np.arange(18,dtype=np.uint32))).sum(1,dtype=np.uint32)
 masks,counts=np.unique(bit,return_counts=True);maximal=maximal_masks(masks)
 faces=masks_to_faces(maximal,3);nodes=[];m=np.array(h['supported']);v=np.array(h['height_nm'],float);ci=np.array(h['conditional_resampling_interval_nm'],float)
 # Full witnesses, not density-filled intersections. Circular means on torus.
 for f in faces:
  fm=sum(1<<i for i in f);select=(bit&fm)==fm;w=q[select]
  pos=np.rad2deg(np.arctan2(np.sin(np.deg2rad(w)).mean(0),np.cos(np.deg2rad(w)).mean(0))) if period else w.mean(0)
  b=np.floor((pos-lo)/(hi-lo)*h['bins']).astype(int);inside=bool(((b>=0)&(b<h['bins'])).all());b=np.clip(b,0,h['bins']-1);supported=inside and bool(m[tuple(b)])
  nodes.append(dict(id=len(nodes),simplex=list(f),witnesses=int(select.sum()),chart=pos.tolist(),supported=supported,height_nm=float(v[tuple(b)]) if supported else None,interval_nm=ci[:,b[0],b[1]].tolist() if supported else None))
 sets=[set(f) for f in faces];edges=[(i,j) for i,a in enumerate(sets) for j,b in enumerate(sets) if a<b]
 successors={i:[] for i in range(len(nodes))}
 for i,j in edges:successors[i].append(j)
 chains=[(i,j,k) for i,j in edges for k in successors[j]]
 # Check all facets through dimension 3 to compute H_2, retain maxima for all higher faces.
 rows=[]
 for r in ([45,55,65,73] if period else [.6,.8,1.,1.2]):
  for stride in [1,10]:
   mm=dis[::stride]<=r;rows.append(dict(radius=r,witness_stride=stride,**complex_stats(mm)))
 return dict(centers=centers.tolist(),metric_scale=scale.tolist(),radius=radius,period=period,maximal_simplices=[[i for i in range(18) if x&(1<<i)] for x in maximal],max_dimension=max(int(x).bit_count()-1 for x in maximal),uncovered_frames=int((bit==0).sum()),total_frames=len(q),nodes=nodes,edges=edges,chains=chains,sensitivity=rows,scope='Full-data witnessed complex in a projected chart. Maximal simplices preserve all faces. Display: 2-skeleton of the face-poset nerve of the base complex 2-skeleton; higher base simplices remain in metadata. No configuration-space homotopy claim.',node_height='Mobility field evaluated in the bin containing the witness centroid; null if unsupported. Not conditional intersection-specific mobility.')

def main():
 full=json.loads((OUT/'full-audit.json').read_text())
 raw=np.load(ROOT/'data/alanine-dipeptide-3x250ns-backbone-dihedrals.npz');aq=[np.rad2deg(raw[k]).astype(float) for k in raw]
 atom=np.load(ROOT/'data/alanine-dipeptide-3x250ns-heavy-atom-positions.npz');ad=[metric_features(atom[k].reshape(-1,10,3)) for k in atom]
 z=np.load(OUT/'chignolin-full-features.npz');lens=z['lengths'];ends=np.cumsum(lens)[:-1];cq=list(np.split(z['q'],ends));cd=list(np.split(z['distances'],ends));roots,_,_=lineage_groups(json.loads(str(z['audit']))['timing'])
 manifest=json.loads((ROOT/'data/chignolin-full/manifest.json').read_text())
 cohorts,_,cohort_info=initial_cohort_groups(json.loads(str(z['audit']))['timing'],manifest['files'])
 write('initial-cohorts.json',cohort_info)
 sensitivity=[]
 for name,qs,ds,clusters,period in [('alanine',aq,ad,None,360),('chignolin',cq,cd,roots,None)]:
  old=full['systems'][name]['mobility']
  estimator='root-balanced' if clusters is not None else 'pooled'
  groups=cohorts if clusters is not None else None
  pooled=height(qs,ds,old['lag_frames'],old['bins'],old['limits'],old['block_length'],cluster_ids=clusters,bootstrap_groups=groups)
  write(name+'-pooled-height.json',pooled)
  h=height(qs,ds,old['lag_frames'],old['bins'],old['limits'],old['block_length'],cluster_ids=clusters,estimator=estimator,bootstrap_groups=groups)
  cover=build_cover(np.concatenate(qs),h,period)
  result=dict(system=name,frames=sum(map(len,qs)),runs=len(qs),height=h,cover=cover,clock='1 ps/frame' if period else 'UNRESOLVED; frames only',energy_claim=False)
  write(name+'-atlas.json',result)
  base=np.array(h['height_nm'],float);support=np.array(h['supported'])
  for lag in ([50,100,250] if period else [5,10,20]):
   for block in ([2500,5000,10000] if period else [100,250,500]):
    hh=height(qs,ds,lag,16,h['limits'],block,cluster_ids=clusters,estimator=estimator,bootstrap_groups=groups);a=np.array(hh['height_nm'],float);valid=support&np.array(hh['supported']);width=np.array(hh['conditional_resampling_interval_nm'],float)
    sensitivity.append(dict(system=name,lag_frames=lag,block_length=block,bins=16,supported_bins=int(np.sum(hh['supported'])),common_bins=int(valid.sum()),median_height_nm=float(np.median(a[valid])) if valid.any() else None,median_change_from_baseline_nm=float(np.median(abs(a[valid]-base[valid]))) if valid.any() else None,median_interval_width_nm=float(np.nanmedian((width[1]-width[0])[valid])) if valid.any() else None))
  for bins in [8,12,24]:
   hh=height(qs,ds,h['lag_frames'],bins,h['limits'],h['block_length'],cluster_ids=clusters,estimator=estimator,bootstrap_groups=groups);write(name+f'-height-{bins}.json',hh)
   sensitivity.append(dict(system=name,lag_frames=h['lag_frames'],block_length=h['block_length'],bins=bins,supported_bins=int(np.sum(hh['supported']))))
  print('Rebuilt',name,len(cover['nodes']),len(cover['chains']),flush=True)
 write('06-topology-height-sensitivity.json',dict(interpretation='Conditional resampling spread only; not calibrated confidence. Block-length, lag, bin and cover-scale sensitivities retained. Missing support is not filled.',results=sensitivity))

if __name__=='__main__':main()

"""Train-only state fitting and nested, lineage-grouped prediction diagnostics.
No fitted model is promoted to validated kinetics or an equilibrium estimator.
"""
import json, os, sys
os.environ.setdefault('OMP_NUM_THREADS','4')
os.environ.setdefault('OPENBLAS_NUM_THREADS','4')
from pathlib import Path
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from threadpoolctl import threadpool_limits
from robustness import ROOT, OUT, counts, normalize, lineage_groups, initial_cohort_groups, clean
from close_limitations import write

def ridge(x,y,train,test,alpha):
 mu=x[train].mean(0);sd=x[train].std(0);sd[sd<1e-8]=1
 ym=y[train].mean(0);a=(x[train]-mu)/sd;b=(x[test]-mu)/sd
 w=np.linalg.solve(a.T@a/len(a)+alpha*np.eye(a.shape[1]),a.T@(y[train]-ym)/len(a))
 return b@w+ym

def main():
 z=np.load(OUT/'chignolin-full-features.npz');chem=np.load(OUT/'chemical-features.npz')
 lens=z['lengths'];timing=json.loads(str(z['audit']))['timing'];roots,folds,meta=lineage_groups(timing)
 suffix=''
 if '--initial-cohorts' in sys.argv:
  manifest=json.loads((ROOT/'data/chignolin-full/manifest.json').read_text())
  roots,folds,meta=initial_cohort_groups(timing,manifest['files']);suffix='-initial-cohorts'
 d=z['distances'];q=z['q'];angles=np.concatenate([z['torsions'],chem['omega']],axis=1)
 periodic=np.concatenate([np.sin(angles),np.cos(angles)],axis=1)
 rootnames=sorted(set(roots));rootids=np.array([rootnames.index(r) for r in roots])
 targets={'distances':d,'omega_periodic':np.concatenate([np.sin(chem['omega']),np.cos(chem['omega'])],1),'NMR_distance_deviation_nm':chem['reference_distance_rms_nm'][:,None]}
 rows=[]
 for lag in ([] if '--kinetics-only' in sys.argv else [10,50]):
  origins=[];fg=[];rg=[];off=0
  for n,f,r in zip(lens,folds,rootids):
   ix=np.arange(off+20,off+n-lag,20);origins.extend(ix);fg.extend([f]*len(ix));rg.extend([r]*len(ix));off+=n
  ix=np.array(origins);fg=np.array(fg);rg=np.array(rg)
  candidates={'chart':q[ix],'distances':d[ix],'torsions_phi_psi_omega':periodic[ix],'combined':np.concatenate([d[ix],periodic[ix]],1),'combined_history20':np.concatenate([d[ix],periodic[ix],d[ix-20],periodic[ix-20]],1)}
  for target,ys in targets.items():
   y=ys[ix+lag].astype(float);base=ys[ix].astype(float)
   for f in range(4):
    outer=fg!=f;test=fg==f
    for name,x in candidates.items():
     x=x.astype(float);scores=[]
     for alpha in [.001,.1,1.]:
      losses=[]
      for v in sorted(set(fg[outer])):
       tr=outer&(fg!=v);va=fg==v
       pred=ridge(x,y,tr,va,alpha);losses.append(float(((pred-y[va])**2).mean()))
      scores.append(np.mean(losses))
     alpha=[.001,.1,1.][int(np.argmin(scores))];pred=ridge(x,y,outer,test,alpha)
     errors=((pred-y[test])**2).mean(1);persistence=((base[test]-y[test])**2).mean(1)
     testroots=rg[test];ratios=[]
     for r in np.unique(testroots):
      keep=testroots==r;den=persistence[keep].mean()
      if den>0:ratios.append(float(errors[keep].mean()/den))
     rows.append(dict(lag_frames=lag,target=target,features=name,outer_fold=f,alpha=alpha,inner_scores=scores,heldout_pairs=int(test.sum()),mse=float(errors.mean()),persistence_mse=float(persistence.mean()),ratio=float(errors.mean()/persistence.mean()),root_equal_median_ratio=float(np.median(ratios)),root_ratio_range=[min(ratios),max(ratios)],training_only_scaling=True))
   print('Nested prediction',lag,target,flush=True)
 if rows:write('05-predictive-validation'+suffix+'.json',dict(method='Nested group CV; groups stay together; stride20; training-only scaling and alpha selection; 20-frame history never crosses runs.',grouping='initial-conformation cohorts' if suffix else 'ancestral roots',lineage=meta,warning='Group independence unverified. Reference metric is structural similarity to NMR, not folding identity. No universal best interface. Equal-group summaries diagnose dominance; they are not equilibrium weights.',results=rows))
 if '--prediction-only' in sys.argv:return
 # Fit each partition strictly on training data, then validate multi-step kernels.
 ends=np.cumsum(lens);starts=np.r_[0,ends[:-1]]
 sample=np.concatenate([np.arange(a,b,5) for a,b in zip(starts,ends)])
 sg=np.concatenate([np.full(len(range(a,b,5)),f) for a,b,f in zip(starts,ends,folds)])
 sizes=[len(range(a,b,5)) for a,b in zip(starts,ends)];splits=np.cumsum(sizes)[:-1]
 kinetic=[];rng=np.random.default_rng(42)
 for feature,x in [('distances',d[sample]),('combined',np.concatenate([d[sample],periodic[sample]],1))]:
  x=x.astype(float)
  for fold in range(4):
   train=sg!=fold;mu=x[train].mean(0);sd=x[train].std(0);sd[sd<1e-8]=1;scaled=(x-mu)/sd
   fitix=np.flatnonzero(train);fitix=rng.choice(fitix,min(30000,len(fitix)),replace=False)
   for k in [4,8,16]:
    km=MiniBatchKMeans(n_clusters=k,random_state=42,n_init=3,batch_size=2048).fit(scaled[fitix])
    labels=list(np.split(km.predict(scaled),splits))
    training=[a for a,g in zip(labels,folds) if g!=fold];testing=[a for a,g in zip(labels,folds) if g==fold]
    for lag in [1,2,10]:
     p=normalize(counts(training,lag,k))
     vals=np.linalg.eigvals(p) if np.isfinite(p).all() else []
     times=[float(-5*lag/np.log(v.real)) for v in vals if abs(v.imag)<1e-8 and 0<v.real<1-1e-9]
     for multiple in [2,4]:
      c=counts(testing,lag*multiple,k);obs=normalize(c);pred=np.linalg.matrix_power(p,multiple)
      valid=(c.sum(1)>0)&np.isfinite(pred).all(1);tv=np.full(k,np.nan);tv[valid]=.5*np.abs(pred[valid]-obs[valid]).sum(1)
      # Resample held-out inferred roots as whole clusters, retaining correlations.
      test_root_names=sorted(set(r for r,g in zip(roots,folds) if g==fold))
      rc=np.array([counts([a for a,g,r in zip(labels,folds,roots) if g==fold and r==root],lag*multiple,k) for root in test_root_names])
      bt=[]
      for _ in range(200):
       sampled=rc[rng.integers(len(rc),size=len(rc))].sum(0);bp=normalize(sampled);mask=np.isfinite(bp).all(1)&np.isfinite(pred).all(1)
       vv=np.full(k,np.nan);vv[mask]=.5*np.abs(bp[mask]-pred[mask]).sum(1);bt.append(vv)
      with np.errstate(all='ignore'):
       import warnings
       with warnings.catch_warnings():
        warnings.simplefilter('ignore',RuntimeWarning);interval=np.nanpercentile(bt,[2.5,97.5],axis=0)
      # A one-group bootstrap repeats the same data and yields a misleading
      # zero-width interval. Keep discrepancies, but withhold such intervals.
      if len(rc)<3:interval[:]=np.nan
      kinetic.append(dict(features=feature,fold=fold,states=k,lag_frames=lag*5,multiple=multiple,slowest_positive_timescale_frames=max(times) if times else None,unsupported_training_rows=np.flatnonzero(~np.isfinite(p).all(1)).tolist(),ignored_complex_or_nonpositive_eigenvalues=sum(bool(abs(v.imag)>=1e-8 or v.real<=0) for v in vals),row_counts=c.sum(1).tolist(),row_TV=tv.tolist(),weighted_TV=float(np.average(tv[valid],weights=c.sum(1)[valid])) if valid.any() else None,max_row_TV=float(np.nanmax(tv)) if valid.any() else None,conditional_group_resampling_TV_interval=interval.tolist(),heldout_groups=len(rc),conditional_interval_status='insufficient_groups' if len(rc)<3 else 'conditional_spread_only',minimum_row_pairs=100,rare_rows=(c.sum(1)<100).tolist(),probabilities=pred.tolist(),observed=obs.tolist()))
   print('Train-only state fits',feature,fold,flush=True)
 write('07-kinetic-validation'+suffix+'.json',dict(scope='Train-only partitions, fixed seed, counts at stride5; training fit subsample <=30000. Group bootstrap conditions on fitted model; not calibrated CI or a kinetic pass certificate.',grouping='initial-conformation cohorts' if suffix else 'ancestral roots',lineage=meta,results=kinetic))

if __name__=='__main__':
 with threadpool_limits(limits=4):main()

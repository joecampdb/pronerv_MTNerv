"""Known-process check of bootstrap coverage under replicated lineage dependence.
This measures a synthetic scenario only, not coverage for the MD dataset.
"""
import numpy as np
from robustness import counts,normalize
from close_limitations import write
def main():
 rng=np.random.default_rng(42);p=np.array([[.95,.05],[.12,.88]]);cover={'cohort':[], 'false_independent_roots':[]};width={k:[] for k in cover}
 for rep in range(200):
  z=np.zeros((10,800),dtype=int)
  for t in range(1,800):z[:,t]=(rng.random(10)>=p[z[:,t-1],0]).astype(int)
  clusters=np.array([counts([r],1,2) for r in z])
  for mode,c in [('cohort',clusters),('false_independent_roots',np.repeat(clusters,10,axis=0))]:
   ix=rng.integers(len(c),size=(200,len(c)));bc=c[ix].sum(1);values=bc[:,0,1]/bc[:,0].sum(1);lo,hi=np.quantile(values,[.025,.975]);cover[mode].append(bool(lo<=p[0,1]<=hi));width[mode].append(hi-lo)
 write('07-synthetic-coverage.json',dict(seed=42,replicates=200,bootstrap_replicates=200,known_P=p.tolist(),design='10 independent synthetic Markov paths, 800 frames each; each path duplicated tenfold to model a deliberately extreme lineage dependence. Estimate P01.',results={mode:dict(empirical_coverage=float(np.mean(cover[mode])),mean_interval_width=float(np.mean(width[mode]))) for mode in cover},scope='Monte Carlo diagnostic of this known process; no claim that actual MD obeys it or that empirical intervals have calibrated coverage.'))
 print({k:np.mean(v) for k,v in cover.items()})
if __name__=='__main__':main()

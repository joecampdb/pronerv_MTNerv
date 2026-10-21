"""Executable semantics for finite stochastic kernels; no molecular closure claim."""
import numpy as np

def kernel(p):
 p=np.asarray(p,float)
 if p.ndim!=2 or not np.isfinite(p).all() or (p<0).any() or not np.allclose(p.sum(1),1,atol=1e-10):
  raise ValueError('A kernel needs finite, nonnegative rows summing to one; unsupported states cannot be imputed')
 return p

def compose(first,second):
 """Row convention: X --first--> Y --second--> Z, composite first @ second."""
 first=kernel(first);second=kernel(second)
 if first.shape[1]!=second.shape[0]:raise ValueError('Intermediate state spaces do not match')
 return first@second

def independent_product(a,b):
 """A proposed joint transition ONLY under conditional independence."""
 return np.kron(kernel(a),kernel(b))

def main():
 from robustness import ROOT, OUT, counts, normalize
 from close_limitations import write
 import json
 z=np.load(OUT/'chignolin-full-features.npz');q=z['q'];ends=np.cumsum(z['lengths'])[:-1]
 # Descriptive falsification of a naive independent interface, not a fitted model.
 labels=(q>np.median(q,axis=0)).astype(int);a=list(np.split(labels[:,0],ends));b=list(np.split(labels[:,1],ends));joint=list(np.split(labels[:,0]*2+labels[:,1],ends));rows=[]
 for lag in [1,10,50]:
  pa=normalize(counts(a,lag,2));pb=normalize(counts(b,lag,2));obs=normalize(counts(joint,lag,4));pred=independent_product(pa,pb)
  rows.append(dict(lag_frames=lag,row_TV=(.5*np.abs(obs-pred).sum(1)).tolist(),observed=obs.tolist(),independent_product=pred.tolist()))
 write('composition-contract.json',dict(objects='Finite declared state sets',morphisms='Row-stochastic kernels',composition='Matrix multiplication; identity I; numerical laws tested separately.',molecular_claim='NONE: kernel composition is algebraic. Equality to empirical longer-time dynamics requires closure/Markov validation; product composition additionally assumes independence.',interface_example='Median-split Rg and end-to-end distance; full-data descriptive test, not held-out model selection or a recommended interface.',results=rows,overlap_semantics='For sigma subset tau, witness sets satisfy W(tau) subset W(sigma): canonical witness inclusion is contravariant, a functor from the opposite face poset to finite sets. No comparison functor to the empirical path category is asserted.'))

if __name__=='__main__':main()

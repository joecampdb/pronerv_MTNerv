"""A non-probabilistic semantics for formal paths in recorded visit occurrences.

Each basin maps to its set of recorded core-entry occurrences. A route maps
to a relation of consecutive visits within the SAME trajectory. Relational
composition matches the exact intermediate occurrence, never just its label.
The free-category extension preserves composition; it need not be faithful.
This is a semantics of observations, not of autonomous/open molecular dynamics.
"""
import json,itertools
from collections import Counter,defaultdict
import numpy as np
from robustness import ROOT,OUT,carry_core
from close_limitations import write,DEST

def compose_relation(first,second):
 target=defaultdict(list)
 for a,b in second:target[a].append(b)
 return {(a,c) for a,b in first for c in target[b]}

def visits(labels):
 labels=np.asarray(labels)
 return np.flatnonzero((labels>=0)&np.r_[True,labels[1:]!=labels[:-1]])

def analyze(name,qs,centers,scale,radius,periodic):
 rel=defaultdict(set);fibers=defaultdict(set);records=[];triples=Counter();quadruples=Counter();examples={}
 for run,q in enumerate(qs):
  delta=q[:,None]-centers
  if periodic:delta=(delta+180)%360-180
  distance=np.linalg.norm(delta/scale,axis=2);z=carry_core(distance.argmin(1),distance.min(1),radius);ix=visits(z);states=z[ix].tolist();offset=len(records)
  for j,t in enumerate(ix):
   records.append([run,int(t),int(z[t])]);fibers[int(z[t])].add(offset+j)
  for j,(a,b) in enumerate(zip(states[:-1],states[1:])):rel[a,b].add((offset+j,offset+j+1))
  for j,word in enumerate(zip(states[:-2],states[1:-1],states[2:])):
   triples[word]+=1
   if word not in examples:examples[word]=dict(run=run,frames=ix[j:j+3].tolist())
  quadruples.update(zip(states[:-3],states[1:-2],states[2:-1],states[3:]))
 edges=sorted(rel);two=[];three=[]
 for a,b in edges:
  for bb,c in edges:
   if b!=bb:continue
   composite=compose_relation(rel[a,b],rel[b,c]);word=(a,b,c)
   assert len(composite)==triples[word]
   two.append(dict(word=list(word),formal=True,observed_consecutive_occurrences=len(composite),example=examples.get(word)))
   for cc,d in edges:
    if c!=cc:continue
    left=compose_relation(composite,rel[c,d]);right=compose_relation(rel[a,b],compose_relation(rel[b,c],rel[c,d]));assert left==right
    assert len(left)==quadruples[a,b,c,d]
    three.append(dict(word=[a,b,c,d],observed_consecutive_occurrences=len(left)))
 for a,b in edges:
  assert compose_relation({(i,i) for i in fibers[a]},rel[a,b])==rel[a,b]
  assert compose_relation(rel[a,b],{(i,i) for i in fibers[b]})==rel[a,b]
 records=np.array(records,dtype=np.int64);np.savez_compressed(DEST/(name+'-visit-occurrences.npz'),visits=records)
 return dict(system=name,visits=len(records),route_generators=[dict(source=a,target=b,observations=len(rel[a,b])) for a,b in edges],two_step_words=two,three_step_words=three,identity_and_associativity_checked=True,state_definition='Frozen legacy last-core labeling, descriptive only; visit-to-visit intervals include residence time. These are not newly validated metastable states.',scope='Exact finite observation semantics: basin fibers are recorded visit occurrences; generator relations link consecutive occurrences within a run. Equality of basin labels alone does not permit splicing trajectories. No rates or physical clock are required.')

def main():
 z=np.load(OUT/'chignolin-full-features.npz');qs=list(np.split(z['q'],np.cumsum(z['lengths'])[:-1]));old=json.loads((ROOT/'dist/chignolin/data.json').read_text());centers=np.array([b['features'] for b in old['basins']]);std=np.concatenate(qs[:128]).std(0)
 c=analyze('chignolin',qs,centers,std,.42,False)
 a=np.load(ROOT/'data/alanine-dipeptide-3x250ns-backbone-dihedrals.npz');qs=[np.rad2deg(a[k]) for k in a];old=json.loads((ROOT/'dist/dynamics.json').read_text());centers=np.array([b['angles'] for b in old['basins']]);aa=analyze('alanine',qs,centers,np.ones(2),25,True)
 write('empirical-path-semantics.json',dict(functor='Free(G) -> Rel: objects map to visit-occurrence fibers; generators to consecutive-visit relations; identities to diagonal relations; words to relational composites.',warning='A formal path may map to an empty relation. Different formal words may have the same relation. This functor need not be faithful, and does not identify the path category with the overlap face-poset category or compose full dynamical subsystems.',systems=[aa,c]))
 print([(s['system'],s['visits'],len(s['two_step_words'])) for s in [aa,c]])

if __name__=='__main__':main()

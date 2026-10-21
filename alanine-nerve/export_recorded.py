"""Attach verified recorded conformers to supported mobility bins and excerpts.
No synthetic molecular interpolation; transformations are rigid only.
"""
import json,warnings
import numpy as np
from robustness import ROOT,OUT
from close_limitations import DEST,RAW,write

def align(x,ref):
 x=np.asarray(x,float);ref=np.asarray(ref,float);a=x-x.mean(0);b=ref-ref.mean(0)
 u,_,vt=np.linalg.svd(a.T@b);s=np.eye(3);s[-1,-1]=np.linalg.det(u@vt)
 return a@u@s@vt

def main():
 import MDAnalysis as mda
 warnings.filterwarnings('ignore',category=UserWarning,module='MDAnalysis')
 for name in ['alanine','chignolin']:
  atlas=json.loads((DEST/(name+'-atlas.json')).read_text());h=atlas['height'];lo,hi=np.array(h['limits']);n=h['bins'];mask=np.array(h['supported'])
  if name=='chignolin':
   z=np.load(OUT/'chignolin-full-features.npz');q=z['q'];lens=z['lengths'];ends=np.cumsum(lens);starts=np.r_[0,ends[:-1]]
   u=mda.Universe(str(RAW/'topology.psf'),str(RAW/'run-0000.xtc'));ca=u.select_atoms('name CA');ref=ca.positions.copy()*.1
   def coords(run,frame):
    u.load_new(str(RAW/f'run-{run:04d}.xtc'));u.trajectory[int(frame)];return ca.positions.copy()*.1
   bonds=[[i,i+1] for i in range(9)]
   excerpts=[(0,0,100),(748,400,100)]
  else:
   z=np.load(ROOT/'data/alanine-dipeptide-3x250ns-backbone-dihedrals.npz');qs=[np.rad2deg(z[k]) for k in z];q=np.concatenate(qs);lens=[len(x) for x in qs];ends=np.cumsum(lens);starts=np.r_[0,ends[:-1]]
   a=np.load(ROOT/'data/alanine-dipeptide-3x250ns-heavy-atom-positions.npz');aa=[a[k].reshape(-1,10,3) for k in a];ref=aa[0][0]
   def coords(run,frame):return aa[run][frame]
   bonds=[[0,1],[1,2],[1,3],[3,4],[4,5],[4,6],[6,7],[6,8],[8,9]]
   excerpts=[(0,0,100),(1,50,100)]
  ij=np.clip(np.floor((q-lo)/(hi-lo)*n).astype(int),0,n-1);anchors=[]
  for i,j in zip(*np.where(mask)):
   ids=np.flatnonzero((ij[:,0]==i)&(ij[:,1]==j));center=lo+(np.array([i,j])+.5)/n*(hi-lo)
   if not len(ids):continue
   idx=int(ids[np.linalg.norm((q[ids]-center)/(hi-lo),axis=1).argmin()]);run=int(np.searchsorted(ends,idx,side='right'));frame=int(idx-starts[run]);x=coords(run,frame);aligned=align(x,ref)
   anchors.append(dict(bin=[int(i),int(j)],run=run,frame=frame,chart=q[idx].tolist(),coords_nm=aligned.tolist(),max_pair_distance_error_nm=float(np.abs(np.linalg.norm(x[:,None]-x,axis=2)-np.linalg.norm(aligned[:,None]-aligned,axis=2)).max())))
  paths=[]
  for run,start,count in excerpts:
   rows=[]
   # Load once for a contiguous recorded excerpt.
   if name=='chignolin':u.load_new(str(RAW/f'run-{run:04d}.xtc'))
   for f in range(start,min(start+count,lens[run])):
    if name=='chignolin':u.trajectory[f];x=ca.positions.copy()*.1
    else:x=aa[run][f]
    idx=int(starts[run]+f);rows.append(dict(frame=f,chart=q[idx].tolist(),coords_nm=align(x,ref).tolist()))
   paths.append(dict(run=run,frames=rows))
  write(name+'-recorded.json',dict(system=name,bonds=bonds,anchors=anchors,excerpts=paths,scope='Exact recorded sites up to rigid alignment; straight bonds/CA links are graphical guides. Atomistic positions for alanine, CA sites for CLN025. No smoothing or Cartesian interpolation. Molecular magnification is visual and independent of mobility height.',physical_frame_interval_ps=1 if name=='alanine' else None))
  print(name,len(anchors),'recorded anchors',flush=True)

if __name__=='__main__':main()

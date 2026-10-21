"""Blender 4.0: screen stored skins throughout interpolation, without repairs.
BVH overlap candidates exclude triangle pairs sharing a vertex. This is not a
continuous-time collision proof or an atomistic validity test.
"""
import json,sys
from pathlib import Path
import numpy as np
from mathutils.bvhtree import BVHTree
ROOT=Path(__file__).resolve().parent
rows=[]
for system,folder in [('alanine',ROOT/'dist'),('chignolin',ROOT/'dist/chignolin')]:
 for meta in json.loads((folder/'skins/index.json').read_text()):
  rid=meta['id'];base=np.fromfile(folder/f'skins/{rid}.bin',dtype='<f4').reshape(-1,7)[:,:3]
  f=np.fromfile(folder/f'skins/{rid}-indices.bin',dtype='<u4').reshape(-1,3).astype(int)
  targets=np.fromfile(folder/f'skins/{rid}-morph.bin',dtype='<f4').reshape(meta['morphFrames'],-1,6)[:,:,:3]
  phases=[]
  for j in range(meta['morphFrames']*4):
   q=j/4;k=int(q);w=q-k;x=targets[k]*(1-w)+targets[(k+1)%len(targets)]*w
   cross=np.cross(x[f[:,1]]-x[f[:,0]],x[f[:,2]]-x[f[:,0]]);area=np.linalg.norm(cross,axis=1)*.5
   tree=BVHTree.FromPolygons(x.tolist(),f.tolist(),all_triangles=True,epsilon=0)
   overlap=[(a,b) for a,b in tree.overlap(tree) if a<b and not set(f[a])&set(f[b])]
   phases.append(dict(phase=j/(meta['morphFrames']*4),min_area=float(area.min()),total_area=float(area.sum()),degenerate=int((area<1e-10).sum()),nonadjacent_BVH_overlap_pairs=len(overlap)))
  rows.append(dict(system=system,route=rid,samples=phases,max_overlap_candidates=max(r['nonadjacent_BVH_overlap_pairs'] for r in phases),min_sampled_area=min(r['min_area'] for r in phases),physical_validation=False))
  print(system,rid,rows[-1]['max_overlap_candidates'],flush=True)
out=ROOT/'dist/validation/08-geometry.json'
out.write_text(json.dumps(dict(scope='48 phase samples per route, including three intermediate positions between each stored target; BVH candidate overlaps, not a proof between samples; adjacent triangle crossings and inter-object collisions not certified.',remedy='Validated viewer uses discrete recorded conformations. Legacy continuous skins remain optional illustrative assets and are not promoted to molecular trajectories.',routes=rows),indent=2))

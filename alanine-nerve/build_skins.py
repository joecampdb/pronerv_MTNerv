"""Swept atomic-density envelopes at the same height and scale as the terrain."""
from pathlib import Path
import json
import numpy as np
from scipy.ndimage import map_coordinates, gaussian_filter
from scipy.spatial import cKDTree
from skimage.measure import marching_cubes

root=Path(__file__).parent
out=root/"dist"/"skins"
out.mkdir(exist_ok=True)
d=json.loads((root/"dist/dynamics.json").read_text())
free=np.array(json.loads((root/"dist/data.json").read_text())["freeEnergy"])
metadata=[]
spacing=.22
for edge in d["edges"]:
    rep=edge["representative"]
    frames=np.array(rep["molecularFrames"])
    angles=np.rad2deg(np.unwrap(np.deg2rad(rep["frameAngles"]),axis=0))
    # Dense temporal interpolation for a continuous visual sweep, not new MD.
    count=max(96,len(frames)*8)
    times=np.linspace(0,len(frames)-1,count)
    ix=np.minimum(times.astype(int),len(frames)-2)
    weight=(times-ix)[:,None,None]
    atoms=frames[ix]*(1-weight)+frames[ix+1]*weight
    a=angles[ix]*(1-weight[:,:,0])+angles[ix+1]*weight[:,:,0]
    a=(a+180)%360-180
    energy=map_coordinates(free,np.array([(a[:,0]+180)/12-.5,(a[:,1]+180)/12-.5]),order=1,mode="grid-wrap")
    centers=np.stack([a[:,0]/12,energy*1.3,a[:,1]/12],axis=1)
    atoms=atoms*3.5+centers[:,None,:]
    lo=np.floor((atoms.min((0,1))-1.6)/spacing)*spacing
    hi=atoms.max((0,1))+1.6
    shape=np.ceil((hi-lo)/spacing).astype(int)+1
    field=np.zeros(shape,np.float32)
    for mol in atoms:
        l=np.maximum(np.floor((mol.min(0)-1.5-lo)/spacing).astype(int),0)
        h=np.minimum(np.ceil((mol.max(0)+1.5-lo)/spacing).astype(int)+1,shape)
        xx,yy,zz=np.ogrid[l[0]:h[0],l[1]:h[1],l[2]:h[2]]
        local=np.zeros(h-l,np.float32)
        for atom in mol:
            c=(atom-lo)/spacing
            local+=np.exp(-((xx-c[0])**2+(yy-c[1])**2+(zz-c[2])**2)*spacing**2/(2*.36**2))
        patch=field[l[0]:h[0],l[1]:h[1],l[2]:h[2]]
        np.maximum(patch,local,out=patch)
    field=gaussian_filter(field,.45)
    vertices,faces,normals,_=marching_cubes(field,.7,spacing=(spacing,)*3)
    vertices+=lo
    _,nearest=cKDTree(atoms.reshape(-1,3)).query(vertices)
    phase=(nearest//10)/(count-1)
    # All triangles are local even when a route crosses the cut angular seam.
    assert np.max(np.linalg.norm(vertices[faces[:,0]]-vertices[faces[:,1]],axis=1))<spacing*2
    assert np.isfinite(vertices).all() and np.all((phase>=0)&(phase<=1))
    np.concatenate([vertices,normals,phase[:,None]],axis=1).astype("<f4").tofile(out/f"{edge['id']}.bin")
    faces.astype("<u4").tofile(out/f"{edge['id']}-indices.bin")
    metadata.append(dict(id=edge["id"],vertices=len(vertices),triangles=len(faces),samples=count,
                         centerHeightOffset=0,molecularScale=3.5))
(out/"index.json").write_text(json.dumps(metadata))
print(f"Built {len(metadata)} skins; {sum(m['triangles'] for m in metadata):,} triangles")

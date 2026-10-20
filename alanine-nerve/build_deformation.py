"""MD-attached material deformation of swept skins; no new MD is claimed."""
from pathlib import Path
import json
import numpy as np
from scipy.ndimage import map_coordinates

root=Path(__file__).parent; out=root/"dist/skins"
d=json.loads((root/"dist/dynamics.json").read_text())
meta=json.loads((out/"index.json").read_text())
free=np.array(json.loads((root/"dist/data.json").read_text())["freeEnergy"])
steps=12
stats=[]
for e,m in zip(d["edges"],meta):
    source=np.fromfile(out/f'{e["id"]}.bin',dtype="<f4").reshape(-1,7)
    vertices=source[:,:3].astype(float); u=source[:,6].astype(float)
    faces=np.fromfile(out/f'{e["id"]}-indices.bin',dtype="<u4").reshape(-1,3)
    rep=e["representative"]; frames=np.array(rep["molecularFrames"])
    angles=np.rad2deg(np.unwrap(np.deg2rad(rep["frameAngles"]),axis=0))
    def sample(t):
        idx=t*(len(frames)-1); i=np.minimum(idx.astype(int),len(frames)-2); w=idx-i
        a=angles[i]*(1-w[:,None])+angles[i+1]*w[:,None]
        wrapped=(a+180)%360-180
        energy=map_coordinates(free,np.array([(wrapped[:,0]+180)/12-.5,(wrapped[:,1]+180)/12-.5]),order=1,mode="grid-wrap")
        centers=np.stack([a[:,0]/12,1.3*energy,a[:,1]/12],axis=1)
        atom=(frames[i]*(1-w[:,None,None])+frames[i+1]*w[:,None,None])*3.5
        return atom+centers[:,None,:]
    original=sample(u)
    # Lift each vertex to the periodic copy nearest its attached cross-section.
    lifted=vertices.copy()
    for axis in (0,2):
        lifted[:,axis]+=30*np.round((original[:,:,axis].mean(1)-lifted[:,axis])/30)
    dist2=((original-lifted[:,None,:])**2).sum(2)
    weights=np.exp(-(dist2-dist2.min(1)[:,None])/(2*.7**2))
    weights/=weights.sum(1)[:,None]
    targets=[]
    for k in range(steps):
        t=k/steps
        tau=u+.08*np.sin(2*np.pi*(t-u))*np.sin(np.pi*u)
        assert np.all((tau>=0)&(tau<=1))
        displacement=((sample(tau)-original)*weights[:,:,None]).sum(1)
        # Smooth conflicting attachments near self-overlap, then bound excursion.
        for _ in range(2):
            acc=displacement.copy(); degree=np.ones(len(vertices))
            for a,b in ((0,1),(1,2),(2,0),(1,0),(2,1),(0,2)):
                np.add.at(acc,faces[:,a],displacement[faces[:,b]])
                np.add.at(degree,faces[:,a],1)
            displacement=acc/degree[:,None]
        length=np.linalg.norm(displacement,axis=1)
        displacement*= (1.5*np.tanh(length/1.5)/np.maximum(length,1e-12))[:,None]
        displacement[(u==0)|(u==1)]=0
        target=vertices+displacement
        cross=np.cross(target[faces[:,1]]-target[faces[:,0]],target[faces[:,2]]-target[faces[:,0]])
        normals=np.zeros_like(vertices)
        for col in range(3): np.add.at(normals,faces[:,col],cross)
        normals/=np.maximum(np.linalg.norm(normals,axis=1)[:,None],1e-12)
        # Match the original mesh's orientation.
        if (normals*source[:,3:6]).sum()<0: normals=-normals
        targets.append(np.concatenate([target,normals],axis=1))
    result=np.array(targets,dtype="<f4")
    assert np.isfinite(result).all()
    variation=np.linalg.norm(result[:,:,:3]-vertices[None],axis=2)
    assert variation.max()>1e-4
    result.tofile(out/f'{e["id"]}-morph.bin')
    m["morphFrames"]=steps
    stats.append(dict(route=e["id"],maxDisplacement=float(variation.max()),rmsDisplacement=float(np.sqrt((variation**2).mean()))))
(out/"index.json").write_text(json.dumps(meta))
(out/"deformation-validation.json").write_text(json.dumps(stats,indent=2))
print("MD-driven vertex deformation:",len(stats),"routes;",steps,"keyframes each")

"""Reproducible MD-derived geometry and face-poset nerve for a cut phi/psi chart."""
from pathlib import Path
import hashlib, itertools, json
import numpy as np
from scipy.ndimage import gaussian_filter, map_coordinates
from skimage.measure import marching_cubes

ROOT = Path(__file__).parent
OUT = ROOT / "dist"
angles = np.load(ROOT / "data/alanine-dipeptide-3x250ns-backbone-dihedrals.npz")
coords = np.load(ROOT / "data/alanine-dipeptide-3x250ns-heavy-atom-positions.npz")
a = np.concatenate([angles[k] for k in angles])
xyz = np.concatenate([coords[k].reshape(-1, 10, 3) for k in coords])
assert a.shape == (750000, 2) and xyz.shape == (750000, 10, 3)
deg = np.rad2deg(a)
n = 30
hist, _, _ = np.histogram2d(*deg.T, bins=n, range=[[-180, 180]] * 2)
smooth = gaussian_filter(hist, 0.85, mode="wrap")
free = -np.log(np.maximum(smooth, 1e-8) / smooth.max())
bins = np.clip(((deg + 180) / 360 * n).astype(int), 0, n - 1)
def energy(p):
    return float(map_coordinates(free, np.array([(p[0]+180)/12-.5, (p[1]+180)/12-.5])[:,None], order=1, mode="grid-wrap")[0])
def world(p):
    return [float(p[0]/12), energy(p)*1.3, float(p[1]/12)]
reps = []
for i, j in zip(*np.where(hist >= 25)):
    ids = np.where((bins[:,0] == i) & (bins[:,1] == j))[0]
    center = np.array([i,j])*12-174
    idx = int(ids[np.argmin(np.sum((deg[ids]-center)**2, axis=1))])
    reps.append(dict(index=idx, angles=deg[idx].tolist(), pos=world(deg[idx]), count=int(hist[i,j])))

# Smooth union of atomic Gaussian densities from actual representative conformers.
# Molecular scale and energy height are visual encodings, not a physical embedding.
lo = np.array([-18.,-3.,-18.]); spacing = .22
shape = (165,85,165)
field = np.zeros(shape, np.float32)
for r in reps:
    mol = (xyz[r["index"]]-xyz[r["index"]].mean(0))*3.5
    for atom in mol + r["pos"]:
        c = (atom-lo)/spacing
        l=np.maximum(np.floor(c-7).astype(int),0); h=np.minimum(np.ceil(c+8).astype(int),shape)
        if np.any(h<=l): continue
        xx,yy,zz=np.ogrid[l[0]:h[0],l[1]:h[1],l[2]:h[2]]
        density=np.exp(-((xx-c[0])**2+(yy-c[1])**2+(zz-c[2])**2)*spacing**2/(2*.36**2))
        field[l[0]:h[0],l[1]:h[1],l[2]:h[2]] += density
v,f,norm,_ = marching_cubes(field, level=.7, spacing=(spacing,)*3)
v += lo
ev=map_coordinates(free, np.array([(v[:,0]*12+180)/12-.5,(v[:,2]*12+180)/12-.5]),order=1,mode="grid-wrap")
np.concatenate([v,norm,ev[:,None]],axis=1).astype("<f4").tofile(OUT/"surface.bin")
f.astype("<u4").tofile(OUT/"triangles.bin")

# Cover a finite sampled chart with balls; simplex = witnessed common membership.
# Greedy centers chosen from representatives; radius fixed and disclosed.
points=np.array([r["angles"] for r in reps])
chosen=[int(np.argmax([r["count"] for r in reps]))]
while len(chosen)<18:
    ds=((points[:,None]-points[chosen])**2).sum(2).min(1)
    chosen.append(int(ds.argmax()))
centers=points[chosen]; radius=73.
witness=deg[::10]
members=np.linalg.norm(witness[:,None]-centers[None],axis=2)<=radius
simplices=set((i,) for i in range(len(centers)))
for row in np.unique(members,axis=0):
    ids=np.flatnonzero(row)
    for size in (2,3):
        simplices.update(itertools.combinations(map(int,ids),size))
simplices=sorted(simplices,key=lambda s:(len(s),s))
nodes=[]
for s in simplices:
    mask=members[:,s].all(1)
    pts=witness[mask]
    center=pts.mean(0) if len(pts) else centers[s[0]]
    idx=int(np.argmin(((deg-center)**2).sum(1)))
    nodes.append(dict(simplex=list(s),angles=center.tolist(),pos=world(center),
                      frame=idx,count=int(mask.sum()),energy=energy(center),
                      molecule=(xyz[idx]-xyz[idx].mean(0)).tolist()))
edges=[[i,j] for i,s in enumerate(simplices) for j,t in enumerate(simplices) if len(s)<len(t) and set(s)<set(t)]
edge_set=set(map(tuple,edges))
chains=[[i,j,k] for i,j in edges for k in range(len(nodes)) if (j,k) in edge_set]
assert all(set(simplices[i])<set(simplices[j])<set(simplices[k]) for i,j,k in chains)
# A small time-ordered sample of the first run; each step = 50 ps.
track=[dict(pos=world(deg[i]),angles=deg[i].tolist(),frame=i,
            molecule=(xyz[i]-xyz[i].mean(0)).round(5).tolist()) for i in range(0,250000,50)]
meta=dict(frames=len(a),runs=3,temperature=300,spacingPs=1,representatives=len(reps),
          vertices=len(v),faces=len(f),nodes=nodes,edges=edges,chains=chains,
          track=track,coverRadiusDeg=radius,witnessStride=10,
          histogram=hist.astype(int).tolist(),freeEnergy=free.round(4).tolist(),
          sources={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/"data").iterdir()})
(OUT/"data.json").write_text(json.dumps(meta,separators=(",",":")))
print(json.dumps({k:meta[k] for k in ["frames","representatives","vertices","faces"]}))
print("Nerve:",len(nodes),"objects,",len(edges),"inclusions,",len(chains),"composition triangles")

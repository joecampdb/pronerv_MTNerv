"""Build the CLN025 atlas from independent runs, with explicit sampling caveats."""
import hashlib
import itertools
import json
from pathlib import Path
import warnings

import MDAnalysis as mda
import numpy as np
from scipy.cluster.vq import kmeans2
from scipy.ndimage import gaussian_filter, map_coordinates
from scipy.spatial import cKDTree
from skimage.measure import marching_cubes

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "data/chignolin"
OUT = ROOT / "dist/chignolin"
OUT.mkdir(exist_ok=True)
(OUT / "skins").mkdir(exist_ok=True)
warnings.filterwarnings("ignore", category=UserWarning, module="MDAnalysis")


def dump(path, obj):
    path.write_text(json.dumps(obj, separators=(",", ":"), ensure_ascii=False), encoding="utf-8")


def envelope(atoms, spacing=.30, sigma=.43, sweep=False):
    """Gaussian envelope; temporal max prevents sample-count-dependent thickness."""
    lo = atoms.reshape(-1, 3).min(0) - 1.7
    hi = atoms.reshape(-1, 3).max(0) + 1.7
    shape = np.ceil((hi - lo) / spacing).astype(int) + 1
    field = np.zeros(shape, np.float32)
    for frame in atoms:
        sub = np.zeros(shape, np.float32) if sweep else field
        for atom in frame:
            c = (atom - lo) / spacing
            l = np.maximum(np.floor(c - 5).astype(int), 0)
            h = np.minimum(np.ceil(c + 6).astype(int), shape)
            x, y, z = np.ogrid[l[0]:h[0], l[1]:h[1], l[2]:h[2]]
            sub[l[0]:h[0], l[1]:h[1], l[2]:h[2]] += np.exp(
                -((x-c[0])**2 + (y-c[1])**2 + (z-c[2])**2)*spacing**2/(2*sigma**2))
        if sweep:
            np.maximum(field, sub, out=field)
    v, f, n, _ = marching_cubes(gaussian_filter(field, .45), .65, spacing=(spacing,)*3)
    return v + lo, f, n


def main():
    manifest = json.loads((SRC / "manifest.json").read_text(encoding="utf-8"))
    for rec in manifest["files"]:
        assert hashlib.sha256((SRC / rec["file"]).read_bytes()).hexdigest() == rec["sha256"]
    runs, raw_times = [], []
    reference = None
    for path in sorted(SRC.glob("run-*.xtc")):
        universe = mda.Universe(str(SRC/"topology.pdb"), str(path))
        ca = universe.select_atoms("name CA")
        assert len(ca) == 10 and "".join({"TYR":"Y","ASP":"D","PRO":"P","GLU":"E",
                                       "THR":"T","GLY":"G","TRP":"W"}[r] for r in ca.resnames) == "YYDPETGTWY"
        frames = np.array([ca.positions.copy()*.1 for _ in universe.trajectory])
        # CA coordinates, nm; this is geometric compactness, not mass-weighted Rg.
        assert np.all((np.linalg.norm(np.diff(frames, axis=1), axis=2) > .3) &
                      (np.linalg.norm(np.diff(frames, axis=1), axis=2) < .5))
        frames -= frames.mean(1, keepdims=True)
        if reference is None:
            reference = frames[0].copy()
        for k, frame in enumerate(frames):
            u, _, vt = np.linalg.svd(frame.T @ reference)
            correction = np.diag([1., 1., np.linalg.det(u @ vt)])
            frames[k] = frame @ u @ correction @ vt
        runs.append(frames)
        raw_times.append(dict(file=path.name, frames=len(frames),
                              firstPs=universe.trajectory[0].time,
                              lastPs=universe.trajectory[-1].time,
                              dtPs=universe.trajectory.dt))
    xyz = np.concatenate(runs)
    q = np.column_stack([np.sqrt((xyz**2).sum(2).mean(1)),
                         np.linalg.norm(xyz[:,0]-xyz[:,-1], axis=1)])
    low = q.min(0) - .01
    high = q.max(0) + .01
    n = 30
    hist, _, _ = np.histogram2d(*q.T, bins=n, range=list(zip(low, high)))
    density = gaussian_filter(hist, .85, mode="reflect")
    free = -np.log(np.maximum(density, 1e-8) / density.max())
    def energy(points):
        p = np.atleast_2d(points)
        return map_coordinates(free, ((p-low)/(high-low)*n-.5).T, order=1, mode="nearest")
    def world(points):
        p = np.atleast_2d(points)
        plane = (p-low)/(high-low)*30-15
        return np.column_stack([plane[:,0], 1.3*energy(p), plane[:,1]])
    world_q = world(q)
    bins = np.clip(((q-low)/(high-low)*n).astype(int), 0, n-1)
    representatives = []
    for i, j in zip(*np.where(hist >= 20)):
        ids = np.flatnonzero((bins[:,0] == i) & (bins[:,1] == j))
        target = low + (np.array([i,j])+.5)/n*(high-low)
        representatives.append(int(ids[np.argmin(((q[ids]-target)**2).sum(1))]))
    # Reduce dense overlaps while retaining the occupied chart.
    representatives = representatives[::max(1, int(np.ceil(len(representatives)/180)))]
    molscale = 2.3
    v, f, normal = envelope(xyz[representatives]*molscale + world_q[representatives,None,:])
    e = energy(low + (v[:,[0,2]]+15)/30*(high-low))
    np.column_stack([v,normal,e]).astype("<f4").tofile(OUT/"surface.bin")
    f.astype("<u4").tofile(OUT/"triangles.bin")

    # The overlap category uses a declared Euclidean chart metric, not atom-space topology.
    chart = world_q[:,[0,2]]
    selected = [int(np.argmax([hist[tuple(bins[i])] for i in representatives]))]
    pts = chart[representatives]
    while len(selected) < 14:
        selected.append(int(((pts[:,None]-pts[selected])**2).sum(2).min(1).argmax()))
    centers = pts[selected]
    witness = chart[::5]
    membership = np.linalg.norm(witness[:,None]-centers[None], axis=2) <= 5.2
    simplices = set()
    for row in np.unique(membership, axis=0):
        for size in (1,2,3):
            simplices.update(itertools.combinations(map(int, np.flatnonzero(row)), size))
    simplices = sorted(simplices, key=lambda s:(len(s), s))
    nodes = []
    for s in simplices:
        ids = np.flatnonzero(membership[:,s].all(1))*5
        center = q[ids].mean(0)
        idx = int(ids[np.argmin(((q[ids]-center)**2).sum(1))])
        nodes.append(dict(simplex=s, pos=world(center)[0].tolist(), frame=idx,
                          molecule=xyz[idx].tolist(), count=len(ids)))
    edges = [[i,j] for i,s in enumerate(simplices) for j,t in enumerate(simplices)
             if len(s)<len(t) and set(s)<set(t)]
    es = set(map(tuple, edges))
    chains = [[i,j,k] for i,j in edges for k in range(len(nodes)) if (j,k) in es]
    # Four descriptive geometric clusters, ordered by increasing CA radius of gyration.
    z = (q-q.mean(0))/q.std(0)
    c, _ = kmeans2(z[::5], 4, minit="++", seed=42, iter=50)
    c = c[np.argsort(c[:,0])]
    distances = np.linalg.norm(z[:,None]-c[None], axis=2)
    nearest = distances.argmin(1)
    in_core = distances.min(1) <= .42
    passages = {}
    exposure = np.zeros(4, int)
    offset = 0
    excluded = 0
    for run_id, run in enumerate(runs):
        previous, last = None, None
        for k in range(len(run)):
            idx = offset+k
            if in_core[idx]:
                label = int(nearest[idx])
                if previous is not None and label != previous:
                    passages.setdefault((previous,label), []).append((run_id,last,k,offset))
                previous, last = label, k
            if previous is None:
                excluded += 1
            else:
                exposure[previous] += 1
        offset += len(run)
    basins = [dict(id=i, name=chr(65+i), features=(c[i]*q.std(0)+q.mean(0)).tolist(),
                   pos=world(c[i]*q.std(0)+q.mean(0))[0].tolist(),
                   occupancy=float(exposure[i]/exposure.sum())) for i in range(4)]
    routes, metas, checks = [], [], []
    for route_id, ((source,target), events) in enumerate(sorted(passages.items())):
        duration = np.array([b-a for _,a,b,_ in events])
        event = events[int(np.argmin(abs(duration-np.median(duration))))]
        run_id,a,b,offset = event
        frame_ids = np.arange(offset+a, offset+b+1)
        sample_ids = np.linspace(0,len(frame_ids)-1,min(80,len(frame_ids)))
        # Keep exact recorded frames; temporal interpolation is only for visual skins.
        frame_ids = frame_ids[np.unique(np.round(sample_ids).astype(int))]
        atom_path = xyz[frame_ids]*molscale + world_q[frame_ids,None,:]
        def sample(t):
            loc = t*(len(atom_path)-1)
            ii = np.minimum(loc.astype(int), len(atom_path)-2)
            w = loc-ii
            return atom_path[ii]*(1-w[:,None,None])+atom_path[ii+1]*w[:,None,None]
        dense = sample(np.linspace(0,1,96))
        v, faces, normals = envelope(dense, sweep=True)
        _, attachment = cKDTree(dense.reshape(-1,3)).query(v)
        phase = (attachment//10)/95
        initial = sample(phase)
        dd = ((initial-v[:,None,:])**2).sum(2)
        weights = np.exp(-(dd-dd.min(1)[:,None])/(2*.7**2))
        weights /= weights.sum(1)[:,None]
        targets = []
        for k in range(12):
            tau = phase + .08*np.sin(2*np.pi*(k/12-phase))*np.sin(np.pi*phase)
            disp = ((sample(tau)-initial)*weights[:,:,None]).sum(1)
            for _ in range(2):
                acc, degree = disp.copy(), np.ones(len(v))
                for aa,bb in ((0,1),(1,2),(2,0),(1,0),(2,1),(0,2)):
                    np.add.at(acc, faces[:,aa], disp[faces[:,bb]])
                    np.add.at(degree, faces[:,aa], 1)
                disp = acc/degree[:,None]
            length = np.linalg.norm(disp, axis=1)
            disp *= (1.5*np.tanh(length/1.5)/np.maximum(length,1e-12))[:,None]
            disp[(phase==0)|(phase==1)] = 0
            p = v+disp
            cross = np.cross(p[faces[:,1]]-p[faces[:,0]],p[faces[:,2]]-p[faces[:,0]])
            nn = np.zeros_like(v)
            for col in range(3):
                np.add.at(nn, faces[:,col], cross)
            nn /= np.maximum(np.linalg.norm(nn,axis=1)[:,None],1e-12)
            if (nn*normals).sum()<0:
                nn = -nn
            targets.append(np.column_stack([p,nn]))
        targets = np.array(targets, dtype="<f4")
        np.column_stack([v,normals,phase]).astype("<f4").tofile(OUT/f"skins/{route_id}.bin")
        faces.astype("<u4").tofile(OUT/f"skins/{route_id}-indices.bin")
        targets.tofile(OUT/f"skins/{route_id}-morph.bin")
        metas.append(dict(id=route_id,vertices=len(v),triangles=len(faces),morphFrames=12))
        displacement = np.linalg.norm(targets[:,:,:3]-v[None],axis=2)
        assert np.isfinite(targets).all() and 0 < displacement.max() <= 1.50001
        assert np.all(displacement[:,(phase==0)|(phase==1)] < 2e-6)
        checks.append(dict(route=route_id,maxDisplacement=float(displacement.max())))
        routes.append(dict(id=route_id,source=source,target=target,count=len(events),
                           medianFrames=float(np.median(duration)),
                           run=run_id,startFrame=a,endFrame=b,
                           moleculeFrames=xyz[frame_ids].tolist(),
                           worldFrames=world_q[frame_ids].tolist()))
        print(f"Route {source}->{target}: {len(events)} passages, {len(v)} vertices", flush=True)
    pairs = [[a["id"],b["id"]] for a in routes for b in routes if a["target"]==b["source"]]
    # A typical compact and extended conformer, selected from actual recorded frames.
    cartoon_ids = [int(np.argmin(np.abs(q[:,0]-np.quantile(q[:,0],p)))) for p in (.05,.95)]
    offsets = np.concatenate([[0], np.cumsum([len(r) for r in runs])])
    cartoon_runs = [int(np.searchsorted(offsets[1:], i, side="right")) for i in cartoon_ids]
    data = dict(title="Chignolin CLN025",sequence="YYDPETGTWY",frames=len(xyz),
                runs=len(runs),nominalRunNs=50,nominalAggregateNs=len(runs)*50,
                timing="Nominal 100 ps/frame from depositor; conflicting XTC times not used",
                coordinateUnits="nm", representation="10 aligned C-alpha sites",
                chart=dict(axes=["CA radius of gyration / nm","End-to-end CA distance / nm"],
                           min=low.tolist(),max=high.tolist(),bins=n,
                           energyMeaning="Negative log pooled occupancy; not equilibrium free energy"),
                freeEnergy=free.tolist(),nodes=nodes,edges=edges,chains=chains,
                coverRadius=5.2,coverMetric="Euclidean distance in linearly rescaled 30x30 chart",
                witnessStride=5,basins=basins,routes=routes,pairs=pairs,
                excludedInitialFrames=excluded,representatives=len(representatives),
                cartoons=[dict(frame=i,run=r,localFrame=int(i-offsets[r]),features=q[i].tolist(),
                               molecule=xyz[i].tolist()) for i,r in zip(cartoon_ids,cartoon_runs)],
                provenance=manifest,rawTiming=raw_times,
                totalPassages=sum(len(v) for v in passages.values()))
    dump(OUT/"data.json", data)
    dump(OUT/"skins/index.json",metas)
    dump(OUT/"skins/deformation-validation.json",checks)
    dump(OUT/"provenance.json",manifest)
    np.savez_compressed(SRC/"processed.npz",xyz=xyz,q=q,centers=c)
    print(json.dumps({k:data[k] for k in ["frames","runs","totalPassages","excludedInitialFrames"]}))
    print("Nerve:",len(nodes),len(edges),len(chains),"paths:",len(routes),len(pairs))


if __name__ == "__main__":
    main()

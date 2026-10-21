"""Reproducible, non-publishing audit of the atlas and candidate mobility height.

Run `python robustness.py` for the legacy subset; add `--full` after
verify_full_chignolin.py completes. Outputs never overwrite viewer data.
"""
import argparse
import hashlib
import itertools
import json
import re
import warnings
import platform
import importlib.metadata
from pathlib import Path
import numpy as np
from scipy.ndimage import gaussian_filter
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'output/robustness'

def counts(labels, lag, n=4):
    """No run crossing or imputation of missing states."""
    if lag<1:raise ValueError('Lag must be a positive frame count')
    c = np.zeros((n,n), dtype=np.int64)
    for z in labels:
        a,b = z[:-lag],z[lag:]
        ok = (a>=0)&(b>=0)
        c += np.bincount(n*a[ok]+b[ok], minlength=n*n).reshape(n,n)
    return c

def normalize(c):
    total = c.sum(1)
    return np.divide(c,total[:,None],out=np.full(c.shape,np.nan,float),where=total[:,None]>0)

def carry_core(nearest, distance, radius):
    core = np.where(distance<=radius,nearest,-1)
    last = np.maximum.accumulate(np.where(core>=0,np.arange(len(core)),-1))
    return np.where(last>=0,core[np.maximum(last,0)],-1)

def metric_features(xyz):
    a,b = np.triu_indices(xyz.shape[1],1)
    return np.linalg.norm(xyz[:,a]-xyz[:,b],axis=2)

def mobility(features,lag):
    """RMS change of internal pair distances; translation/rotation invariant, nm."""
    return np.sqrt(np.mean((features[lag:]-features[:-lag])**2,axis=1))

def provenance_group(member):
    # File names encode epochs and apparent parents. These are provenance clues,
    # not a declaration that roots are statistically independent.
    directory = Path(member).parent.name
    child = re.match(r'(e\d+s\d+)',directory)
    parent = re.search(r'_(e\d+s\d+)p\d+f\d+',directory)
    epoch = re.match(r'e(\d+)s',directory)
    return dict(child=child.group(1) if child else directory,
                parent=parent.group(1) if parent else None,
                epoch=int(epoch.group(1)) if epoch else -1)

def lineage_groups(timing):
    """Keep all descendants of a filename-inferred root in one fold."""
    parents={x['child']:x['parent'] for x in timing}
    if len(parents)!=len(timing):raise ValueError('Duplicate lineage identifiers')
    roots=[];missing=set()
    for x in timing:
        node=x['child'];seen=set()
        while parents.get(node) is not None:
            if node in seen:raise ValueError('Cycle in inferred restart genealogy')
            seen.add(node);node=parents[node]
            if node not in parents:missing.add(node)
        roots.append(node)
    names,counts=np.unique(roots,return_counts=True)
    loads=np.zeros(4,int);mapping={}
    for i in np.argsort(-counts,kind='stable'):
        fold=int(loads.argmin());mapping[names[i]]=fold;loads[fold]+=counts[i]
    return roots,[mapping[x] for x in roots],dict(inferred_roots=len(names),largest_root_runs=int(counts.max()),
        missing_parents=sorted(missing),fold_run_counts=loads.tolist(),
        warning='Filename-derived genealogy, not verified restart metadata or independent initial conditions.')

def load_chignolin(full):
    import MDAnalysis as mda
    warnings.filterwarnings('ignore',category=UserWarning,module='MDAnalysis')
    folder = ROOT / ('data/chignolin-full' if full else 'data/chignolin')
    manifest = json.loads((folder/'manifest.json').read_text(encoding='utf-8'))
    records = [r for r in manifest['files'] if r['file'].endswith('.xtc')]
    cache = OUT / ('chignolin-full-features.npz' if full else 'chignolin-features.npz')
    digest = hashlib.sha256(json.dumps(manifest,sort_keys=True).encode()).hexdigest()
    if cache.exists():
        z = np.load(cache)
        if str(z['manifest_hash'])==digest and 'torsions' in z:
            ends=np.cumsum(z['lengths'])[:-1]
            return list(np.split(z['q'],ends)),list(np.split(z['distances'],ends)),json.loads(str(z['audit']))
    qs=[];ds=[];times=[];neighbor=[];torsions=[]
    for k,r in enumerate(records):
        path=folder/r['file']
        if hashlib.sha256(path.read_bytes()).hexdigest()!=r['sha256']:
            raise ValueError(f'Checksum mismatch: {path}')
        u=mda.Universe(str(folder/'topology.pdb'),str(path));ca=u.select_atoms('name CA')
        assert len(ca)==10
        seq=''.join({'TYR':'Y','ASP':'D','PRO':'P','GLU':'E','THR':'T','GLY':'G','TRP':'W'}[x] for x in ca.resnames)
        assert seq=='YYDPETGTWY'
        from MDAnalysis.lib.distances import calc_dihedrals
        bb=u.atoms[[int(res.atoms.select_atoms('name '+name).indices[0])
                    for res in ca.residues for name in ['N','CA','C']]]
        backbone=np.array([bb.positions.copy()*.1 for _ in u.trajectory]).reshape(-1,10,3,3)
        xyz=backbone[:,:,1,:]
        phi=calc_dihedrals(backbone[:,:-1,2].reshape(-1,3),backbone[:,1:,0].reshape(-1,3),
                          backbone[:,1:,1].reshape(-1,3),backbone[:,1:,2].reshape(-1,3)).reshape(-1,9)
        psi=calc_dihedrals(backbone[:,:-1,0].reshape(-1,3),backbone[:,:-1,1].reshape(-1,3),
                          backbone[:,:-1,2].reshape(-1,3),backbone[:,1:,0].reshape(-1,3)).reshape(-1,9)
        torsions.append(np.concatenate([phi,psi],axis=1).astype(np.float32))
        centered=xyz-xyz.mean(1,keepdims=True)
        qs.append(np.column_stack([np.sqrt((centered**2).sum(2).mean(1)),np.linalg.norm(xyz[:,0]-xyz[:,-1],axis=1)]))
        ds.append(metric_features(xyz).astype(np.float32))
        sep=np.linalg.norm(np.diff(xyz,axis=1),axis=2)
        neighbor.append([float(sep.min()),float(sep.max())])
        times.append(dict(file=r['file'],frames=len(xyz),first=float(u.trajectory[0].time),last=float(u.trajectory[-1].time),dt=float(u.trajectory.dt),**provenance_group(r['member'])))
        if (k+1)%128==0:print(f'Parsed {k+1}/{len(records)} CLN025 runs',flush=True)
    audit=dict(full_archive_verified=manifest.get('fullArchiveVerified',False),runs=len(qs),frames=sum(map(len,qs)),
               timing=times,neighbor_range_nm=np.array(neighbor).tolist(),manifest_hash=digest,
               lineage_caution='Epoch/parent identifiers parsed from filenames, not verified restart metadata.')
    np.savez_compressed(cache,q=np.concatenate(qs),distances=np.concatenate(ds),torsions=np.concatenate(torsions),lengths=[len(x) for x in qs],manifest_hash=digest,audit=json.dumps(audit))
    return qs,ds,audit

def kinetics(labels,lags,groups):
    models=[]
    for lag in lags:
        c=counts(labels,lag);p=normalize(c)
        record=dict(lag_frames=lag,counts=c.tolist(),probabilities=p.tolist(),supported_rows=(c.sum(1)>0).tolist())
        if np.isfinite(p).all():
            ev=np.linalg.eigvals(p)
            valid=sorted([float(v.real) for v in ev if abs(v.imag)<1e-8 and 0<v.real<1-1e-10],reverse=True)
            record['implied_times_frames']=[float(-lag/np.log(v)) for v in valid]
            record['ignored_complex_or_nonpositive_eigenvalues']=int(sum(abs(v.imag)>=1e-8 or v.real<=0 for v in ev))
            # Stationary probabilities are diagnostics only, not equilibrium claims.
            vals,vec=np.linalg.eig(p.T)
            pi=vec[:,np.argmin(abs(vals-1))].real;pi/=pi.sum()
            record['stationary_diagnostic']=pi.tolist()
            record['flux_asymmetry_l1']=float(np.abs(pi[:,None]*p-(pi[:,None]*p).T).sum()/2)
            held=[]
            for group in sorted(set(groups)):
                train=[z for z,g in zip(labels,groups) if g!=group]
                test=[z for z,g in zip(labels,groups) if g==group]
                pt=normalize(counts(train,lag))
                for multiple in [2,4]:
                    ct=counts(test,lag*multiple);obs=normalize(ct)
                    pred=np.linalg.matrix_power(pt,multiple)
                    supported=(ct.sum(1)>0)&np.isfinite(pred).all(1)
                    if supported.any():
                        tv=.5*np.nansum(abs(obs-pred),axis=1)
                        held.append(dict(group=int(group),multiple=multiple,max_row_TV=float(tv[supported].max()),
                                         weighted_row_TV=float(np.average(tv[supported],weights=ct.sum(1)[supported])),
                                         supported_rows=np.flatnonzero(supported).tolist(),
                                         observed=obs.tolist(),predicted=pred.tolist()))
            record['heldout_ck']=held
        models.append(record)
    return models

def height(qs,distances,lag,bins,limits,block_length,seed=42,cluster_ids=None):
    """Conditional structural displacement, with cluster/bootstrap spread.

    No smoothing, no fabricated heights in unsupported bins, no physical clock
    assumed for CLN025. Blocks never synthesize transitions across boundaries.
    """
    low,high=np.asarray(limits[0]),np.asarray(limits[1]);B=bins*bins
    bc=[];bs=[];runids=[]
    for rid,(q,d) in enumerate(zip(qs,distances)):
        val=mobility(d,lag);xy=q[:-lag]
        ij=np.floor((xy-low)/(high-low)*bins).astype(int)
        valid=((ij>=0)&(ij<bins)).all(1)
        ids=np.clip(ij,0,bins-1);idx=ids[:,0]*bins+ids[:,1]
        for start in range(0,len(val),block_length):
            # Keep pairs wholly inside each block (including lag).
            end=min(start+block_length-lag,len(val))
            if end<=start:continue
            ok=valid[start:end];ii=idx[start:end][ok];vv=val[start:end][ok]
            bc.append(np.bincount(ii,minlength=B));bs.append(np.bincount(ii,weights=vv,minlength=B));runids.append(rid)
    bc=np.array(bc);bs=np.array(bs);count=bc.sum(0)
    mean=np.divide(bs.sum(0),count,out=np.full(B,np.nan),where=count>0)
    support=(bc>0).sum(0)
    runsupport=np.array([np.unique(np.array(runids)[bc[:,i]>0]).size for i in range(B)])
    if cluster_ids is not None:
        names=sorted(set(cluster_ids));blockgroups=np.array([cluster_ids[i] for i in runids])
        bc=np.array([bc[blockgroups==g].sum(0) for g in names])
        bs=np.array([bs[blockgroups==g].sum(0) for g in names])
        cluster_support=(bc>0).sum(0)
    else:cluster_support=support
    rng=np.random.default_rng(seed);boot=[]
    for _ in range(200):
        chosen=rng.integers(0,len(bc),len(bc));den=bc[chosen].sum(0)
        boot.append(np.divide(bs[chosen].sum(0),den,out=np.full(B,np.nan),where=den>0))
    with warnings.catch_warnings():
        warnings.simplefilter('ignore',RuntimeWarning)
        ci=np.nanpercentile(boot,[2.5,97.5],axis=0)
    shown=(count>=100)&(support>=5)&(runsupport>=min(3,len(qs)))&(cluster_support>=3)
    return dict(lag_frames=lag,block_length=block_length,bins=bins,limits=[low.tolist(),high.tolist()],
                height_nm=mean.reshape(bins,bins).tolist(),count=count.reshape(bins,bins).tolist(),
                supported=shown.reshape(bins,bins).tolist(),block_support=support.reshape(bins,bins).tolist(),
                run_support=runsupport.reshape(bins,bins).tolist(),
                cluster_support=cluster_support.reshape(bins,bins).tolist(),
                resampling_unit='inferred ancestral root' if cluster_ids is not None else 'within-run blocks',
                conditional_resampling_interval_nm=ci.reshape(2,bins,bins).tolist(),
                uncertainty_caution='Conditional block/run-resampling spread; not a calibrated confidence interval. Adaptive lineage and three-run alanine limits remain.')

def gf2_rank(columns):
    pivots={}
    for col in columns:
        while col:
            pivot=col.bit_length()-1
            if pivot in pivots:col^=pivots[pivot]
            else:pivots[pivot]=col;break
    return len(pivots)

def complex_stats(membership):
    sets=[set() for _ in range(4)]
    for row in np.unique(membership,axis=0):
        vertices=np.flatnonzero(row).tolist()
        for n in range(1,5):sets[n-1].update(itertools.combinations(vertices,n))
    simplices=[sorted(s) for s in sets];ranks=[0]
    for k in range(1,4):
        index={s:i for i,s in enumerate(simplices[k-1])}
        ranks.append(gf2_rank([sum(1<<index[f] for f in itertools.combinations(s,k)) for s in simplices[k]]))
    return dict(simplices=[len(s) for s in simplices],betti_0_1_2=[len(simplices[k])-ranks[k]-ranks[k+1] for k in range(3)],
                truncated_beta2=len(simplices[2])-ranks[2],max_membership=int(membership.sum(1).max()))

def topology(angles):
    hist=np.histogram2d(*angles.T,bins=30,range=[[-180,180]]*2)[0]
    points=np.array([[i*12-174,j*12-174] for i,j in zip(*np.where(hist>=25))])
    ids=[int(np.argmax([hist[int((p[0]+180)//12),int((p[1]+180)//12)] for p in points]))]
    while len(ids)<18:
        delta=(points[:,None]-points[ids]+180)%360-180
        ids.append(int((delta**2).sum(2).min(1).argmax()))
    centers=points[ids];rows=[]
    for periodic in [False,True]:
        for stride in [10,50]:
            delta=angles[::stride,None]-centers[None]
            if periodic:delta=(delta+180)%360-180
            distances=np.linalg.norm(delta,axis=2)
            for radius in [55,65,73,85]:
                rows.append(dict(periodic=periodic,stride=stride,radius_deg=radius,**complex_stats(distances<=radius)))
    return dict(centers_deg=centers.tolist(),sensitivity=rows,
                scope='Periodic farthest-point cover; comparison holds centers fixed. Betti numbers are for the finite witnessed complex, not configuration space.')

def mesh_audit(folder):
    metas=json.loads((folder/'skins/index.json').read_text());rows=[]
    for rid,meta in enumerate(metas):
        base=np.fromfile(folder/f'skins/{rid}.bin',dtype='<f4').reshape(-1,7)[:,:3]
        faces=np.fromfile(folder/f'skins/{rid}-indices.bin',dtype='<u4').reshape(-1,3)
        warp=np.fromfile(folder/f'skins/{rid}-morph.bin',dtype='<f4').reshape(meta['morphFrames'],meta['vertices'],6)[:,:,:3]
        edges=np.sort(np.concatenate([faces[:,[0,1]],faces[:,[1,2]],faces[:,[0,2]]]),axis=1)
        unique,multiplicity=np.unique(edges,axis=0,return_counts=True)
        graph=csr_matrix((np.ones(len(unique)),(unique[:,0],unique[:,1])),shape=(len(base),len(base)))
        areas=[];degenerate=[]
        for pts in [base,*warp]:
            area=np.linalg.norm(np.cross(pts[faces[:,1]]-pts[faces[:,0]],pts[faces[:,2]]-pts[faces[:,0]]),axis=1)*.5
            areas.append(float(area.sum()));degenerate.append(int((area<1e-10).sum()))
        rows.append(dict(route=rid,components=int(connected_components(graph,directed=False,return_labels=False)),
                         boundary_edges=int((multiplicity==1).sum()),nonmanifold_edges=int((multiplicity>2).sum()),
                         degenerate_triangles_max=max(degenerate),area_ratio_range=[min(areas)/areas[0],max(areas)/areas[0]],
                         max_displacement=float(np.linalg.norm(warp-base,axis=2).max())))
    return dict(routes=rows,scope='Combinatorial mesh and keyframe geometry checks only; no self-intersection, collision or physical validity guarantee.')

def clean(x):
    if isinstance(x,dict):return {k:clean(v) for k,v in x.items()}
    if isinstance(x,list):return [clean(v) for v in x]
    if isinstance(x,float) and not np.isfinite(x):return None
    return x

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--full',action='store_true');args=parser.parse_args()
    OUT.mkdir(parents=True,exist_ok=True)
    raw=np.load(ROOT/'data/alanine-dipeptide-3x250ns-backbone-dihedrals.npz')
    qs=[np.rad2deg(raw[k]).astype(float) for k in raw]
    atomic=np.load(ROOT/'data/alanine-dipeptide-3x250ns-heavy-atom-positions.npz')
    ds=[metric_features(atomic[k].reshape(-1,10,3)) for k in atomic]
    legacy=json.loads((ROOT/'dist/dynamics.json').read_text())
    centers=np.array([b['angles'] for b in legacy['basins']])
    systems={}
    for name,coords,dist,centers,scale,radius,lags,lag,limits,block in [
        ('alanine',qs,ds,centers,np.ones(2),25,[1,10,50,100,250,500,1000],100,[[-180,-180],[180,180]],5000),
    ]:
        labels=[];instant=[];sensitivity=[]
        for q in coords:
            dis=np.linalg.norm((q[:,None]-centers+180)%360-180,axis=2)
            instant.append(dis.argmin(1));labels.append(carry_core(dis.argmin(1),dis.min(1),radius))
        for rad in [15,20,25,30]:
            zz=[]
            for q in coords:
                dis=np.linalg.norm((q[:,None]-centers+180)%360-180,axis=2)
                zz.append(carry_core(dis.argmin(1),dis.min(1),rad))
            sensitivity.append(dict(radius=rad,passages=sum(int(((z[1:]!=z[:-1])&(z[:-1]>=0)).sum()) for z in zz)))
        systems[name]=dict(frames=sum(map(len,coords)),runs=len(coords),clock='1 ps/frame',
                           legacy_core_models=kinetics(labels,lags,list(range(len(coords)))),
                           instantaneous_models=kinetics(instant,lags,list(range(len(coords)))),
                           core_sensitivity=sensitivity,
                           mobility=height(coords,dist,lag,16,limits,block),
                           topology=topology(np.concatenate(coords)),mesh=mesh_audit(ROOT/'dist'))
    cq,cd,audit=load_chignolin(args.full)
    # Freeze legacy chart scaling and centers to isolate dataset-selection effects.
    sq,_,_=load_chignolin(False) if args.full else (cq,cd,audit)
    std=np.concatenate(sq).std(0)
    old=json.loads((ROOT/'dist/chignolin/data.json').read_text())
    cc=np.array([b['features'] for b in old['basins']])
    labels=[];instant=[]
    for q in cq:
        dis=np.linalg.norm((q[:,None]-cc)/std,axis=2)
        instant.append(dis.argmin(1));labels.append(carry_core(dis.argmin(1),dis.min(1),.42))
    epochs=np.array([t['epoch'] for t in audit['timing']])
    unique=sorted(set(epochs));groupmap={e:min(3,i*4//len(unique)) for i,e in enumerate(unique)}
    groups=[groupmap[e] for e in epochs]
    roots,rootfolds,lineage=lineage_groups(audit['timing'])
    audit['lineage']=lineage
    allq=np.concatenate(cq)
    systems['chignolin']=dict(frames=sum(map(len,cq)),runs=len(cq),clock='Unresolved; frame-index lags only',provenance=audit,
        validation_split='Held-out filename-inferred ancestral roots; root independence remains unproven. Legacy states are fixed and not independently selected.',
        legacy_core_models=kinetics(labels,[1,2,5,10,20,50],rootfolds),
        instantaneous_models=kinetics(instant,[1,2,5,10,20,50],rootfolds),
        epoch_sensitivity_models=kinetics(labels,[1,10,50],groups),
        mobility=height(cq,cd,10,16,[allq.min(0)-.01,allq.max(0)+.01],500,cluster_ids=roots),mesh=mesh_audit(ROOT/'dist/chignolin'))
    report=dict(status='Diagnostic audit, not a validated kinetic or equilibrium model',seed=42,systems=systems,
                software=dict(python=platform.python_version(),packages={name:importlib.metadata.version(name) for name in ['numpy','scipy','MDAnalysis']}),
                audit_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                interface_hypothesis='Periodic torsions for alanine; nonlocal distances/contacts plus periodic backbone torsions for CLN025. Select on held-out predictive sufficiency, not visual appeal.')
    path=OUT/('full-audit.json' if args.full else 'subset-audit.json')
    path.write_text(json.dumps(clean(report),indent=2,allow_nan=False),encoding='utf-8')
    print(path,flush=True)

if __name__=='__main__':main()

"""Screening diagnostics, not a validated kinetic model or equilibrium estimator."""
import argparse
import csv
import itertools
import json
import subprocess
from pathlib import Path
import numpy as np
from scipy.cluster.vq import kmeans2
from scipy.spatial.distance import cdist


def unwrap_chain(x, box):
    delta = np.diff(x, axis=0)
    delta -= box*np.rint(delta/box)
    return np.vstack([x[0], x[0]+np.cumsum(delta, axis=0)])


def metrics(x, box, contact=.5, separation=4):
    """Lengths are nm. Chain must be ordered and unwrapped."""
    y=x-x.mean(axis=0)
    eig=np.linalg.eigvalsh(y.T@y/len(y))
    rg=np.sqrt(eig.sum())
    anis=1.5*np.sum(eig**2)/eig.sum()**2-.5
    dist=cdist(x,x)
    mask=np.triu(np.ones(dist.shape,dtype=bool),k=separation)
    contacts=np.sum((dist<contact)&mask)/len(x)
    tang=x[2:]-x[:-2]; tang/=np.linalg.norm(tang,axis=1)[:,None]
    order=np.linalg.eigvalsh(1.5*tang.T@tang/len(tang)-.5*np.eye(3))[-1]
    bonds=np.diff(x,axis=0)
    norm=np.cross(bonds[:-1],bonds[1:]); norm/=np.maximum(np.linalg.norm(norm,axis=1)[:,None],1e-12)
    # Consecutive plane normals alternate in an all-trans zigzag.
    trans=np.mean(np.sum(norm[:-1]*norm[1:],axis=1)<-np.cos(np.pi/6))
    # Conservative lower bound; calculate exact image distance only near boundary.
    image_lower=float(np.min(box-np.ptp(x,axis=0)))
    image_distance=image_lower
    exact=False
    if image_lower<2.4:
        image_distance=min(float(cdist(x,x+np.array(s)*box).min())
                           for s in itertools.product([-1,0,1],repeat=3) if s!=(0,0,0))
        exact=True
    return dict(rg_nm=float(rg),anisotropy=float(anis),contacts_per_carbon=float(contacts),
                nematic_order=float(order),trans_fraction=float(trans),
                image_distance_or_lower_bound_nm=image_distance,image_distance_exact=int(exact),
                max_cc_bond_nm=float(np.linalg.norm(bonds,axis=1).max()))


def committed_labels(labels, times, dwell_ps):
    """Require uninterrupted occupancy; ambiguous (-1) points reset commitment.

    Return accepted entries, not individual flickers; no rate interpretation.
    """
    events=[]; committed=None; candidate=None; start=None
    for label,t in zip(labels,times):
        if label<0:
            candidate=None; start=None; continue
        if label!=candidate:
            candidate=int(label); start=float(t)
        if t-start>=dwell_ps and candidate!=committed:
            events.append((float(t),candidate))
            committed=candidate
    return events


def extract(folder, stride, ac=None):
    import MDAnalysis as mda
    from MDAnalysis.lib.distances import distance_array
    info=json.loads((folder/'metadata.json').read_text())
    # GRO atom names/order suffice here; avoid TPR-version coupling in MDAnalysis.
    topology=folder/'prod.gro'
    if not topology.exists(): topology=folder/'relax.gro'
    u=mda.Universe(str(topology),str(folder/'prod.xtc'))
    n=info['ncarbon']; carb=u.atoms[:n]
    if list(carb.names)!=['C'+str(i+1) for i in range(n)]:
        raise ValueError('Unexpected backbone atom order')
    water=u.select_atoms('resname SOL and name OW')
    rows=[]
    for ts in u.trajectory[::stride]:
        if not np.allclose(ts.dimensions[3:],90):
            raise ValueError('This analyzer requires the configured orthorhombic box')
        box=ts.dimensions[:3]/10
        x=unwrap_chain(carb.positions/10,box)
        row=metrics(x,box,contact=(ac or {}).get('contact_nm',.5),
                    separation=(ac or {}).get('minimum_sequence_separation',4))
        hydration=distance_array(carb.positions,water.positions,box=ts.dimensions)
        row.update(time_ps=float(ts.time),hydration_waters=int(np.sum(hydration.min(axis=0)<4.5)))
        rows.append(row)
    if not rows: raise ValueError('No trajectory frames')
    with (folder/'observables.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
    plot(folder,rows,None)
    return rows


def energy_checks(folder, gmx):
    """Block diagnostics; thresholds are screening heuristics, not equilibration proof."""
    diagnostics={}; warnings=[]
    for stage, terms in [('npt',['Temperature','Density']), ('prod',['Temperature'])]:
        if not (folder/f'{stage}.edr').exists():
            warnings.append('missing '+stage+' energy'); continue
        output=folder/f'{stage}.quality.xvg'
        proc=subprocess.run([gmx,'energy','-f',str(folder/f'{stage}.edr'),'-o',str(output)],
                            input='\n'.join(terms)+'\n0\n',text=True,capture_output=True)
        if proc.returncode:
            warnings.append('energy extraction failed: '+stage); continue
        raw=[l for l in output.read_text().splitlines() if l and l[0] not in '#@']
        values=np.loadtxt(raw,ndmin=2)
        if len(values)<20:
            warnings.append('too few energy samples: '+stage); continue
        tail=values[len(values)//2:]
        for col,term in enumerate(terms,1):
            blocks=np.array_split(tail[:,col],2)
            averages=[float(b.mean()) for b in blocks]
            diagnostics[stage+'_'+term]=dict(last_half_mean=float(tail[:,col].mean()),quarter_means=averages)
            if term=='Temperature' and abs(tail[:,col].mean()-300)>5:
                warnings.append('mean temperature outside 300 +/- 5 K')
            if term=='Density' and abs(averages[1]-averages[0])/np.mean(averages)>.01:
                warnings.append('NPT density block means differ by >1%; extend equilibration')
    return diagnostics,warnings


def analyze(root, stride, discard_ns, gmx='gmx'):
    manifest=json.loads((root/'manifest.json').read_text())
    ac=manifest['config']['analysis']
    report=dict(smoke=manifest['smoke'],notice='Discovery screening only. No equilibrium populations or validated rates inferred.',systems={})
    features=['rg_nm','anisotropy','contacts_per_carbon','nematic_order','trans_fraction']
    for system,spec in manifest['config']['systems'].items():
        entries=[x for x in manifest['replicates'] if x['system']==system]
        data=[]; missing=[]; quality=[]
        for entry in entries:
            folder=root/entry['relative_path']
            if not (folder/'prod.xtc').exists():
                missing.append(entry['relative_path']); continue
            rows=extract(folder,stride,ac)
            thermo,warnings=energy_checks(folder,gmx)
            if min(r['image_distance_or_lower_bound_nm'] for r in rows)<ac['minimum_image_distance_nm']:
                warnings.append('periodic-image proximity')
            if max(r['max_cc_bond_nm'] for r in rows)>.20:
                warnings.append('backbone bond distortion')
            if not (folder/'prod.done.json').exists(): warnings.append('production incomplete')
            for logfile in folder.glob('*.log'):
                content=logfile.read_text(errors='replace')
                if 'LINCS WARNING' in content or 'Fatal error:' in content:
                    warnings.append('simulation error in '+logfile.name)
            quality.append(dict(replica=entry['relative_path'],warnings=warnings,
                                thermodynamic_checks=thermo,
                                saved_end_ns=rows[-1]['time_ps']/1000))
            kept=[r for r in rows if r['time_ps']>=discard_ns*1000]
            if len(kept)>=20: data.append((entry,kept))
        result=dict(missing=missing,quality=quality,decision='INSUFFICIENT_DATA')
        if data:
            x=np.array([[r[f] for f in features] for _,rows in data for r in rows])
            mean=x.mean(axis=0); scale=x.std(axis=0); scale[scale<1e-8]=1
            z=(x-mean)/scale
            if len(z)>50 and np.max(np.std(z,axis=0))>.1:
                centers,_=kmeans2(z,2,minit='++',seed=174209)
                distances=cdist(z,centers)
                labels=np.argmin(distances,axis=1)
                margin=np.abs(distances[:,0]-distances[:,1])/np.maximum(distances.sum(axis=1),1e-12)
                labels[margin<.15]=-1
                pos=0; summaries=[]
                for entry,rows in data:
                    labs=labels[pos:pos+len(rows)]; pos+=len(rows)
                    times=np.array([r['time_ps'] for r in rows])
                    counts={}
                    for dwell in [ac['dwell_ps']/2,ac['dwell_ps'],ac['dwell_ps']*2]:
                        events=committed_labels(labs,times,dwell)
                        counts[str(dwell)]={'0_to_1':sum(a[1]==0 and b[1]==1 for a,b in zip(events,events[1:])),
                                           '1_to_0':sum(a[1]==1 and b[1]==0 for a,b in zip(events,events[1:]))}
                    summaries.append(dict(replica=entry['relative_path'],preparation=entry['preparation'],
                                          committed_crossings=counts,ambiguous_fraction=float(np.mean(labs<0))))
                    folder=root/entry['relative_path']
                    np.savetxt(folder/'candidate_states.csv',np.column_stack([times,labs]),delimiter=',',header='time_ps,candidate_state',comments='')
                    plot(folder,rows,labs)
                base=str(ac['dwell_ps'])
                # JSON float/int keys are normalized explicitly below.
                def get(s): return s['committed_crossings'].get(base,s['committed_crossings'].get(str(float(ac['dwell_ps']))))
                forward=sum(get(s)['0_to_1'] for s in summaries)
                reverse=sum(get(s)['1_to_0'] for s in summaries)
                recurrent=sum(min(get(s).values())>0 for s in summaries)
                result.update(features=features,feature_mean=mean.tolist(),feature_scale=scale.tolist(),
                              candidate_centers_standardized=centers.tolist(),replicates=summaries,
                              forward_crossings=forward,reverse_crossings=reverse,recurrent_replicates=recurrent)
                if not missing and not any(q['warnings'] for q in quality):
                    if min(forward,reverse)>=ac['minimum_events_per_direction'] and recurrent>=ac['minimum_replicates_with_recurrence']:
                        result['decision']='CANDIDATE_FOR_KINETIC_VALIDATION'
                    elif forward+reverse==0:
                        result['decision']='NO_RECURRENCE_DETECTED_REVIEW_SLOWNESS_OR_SINGLE_BASIN'
                    else: result['decision']='EXTEND_OR_REVISE_STATE_DEFINITION'
        if manifest['smoke']: result['decision']='SMOKE_ONLY_NO_SCIENTIFIC_DECISION'
        report['systems'][system]=result
    save=root/'screening_report.json'; save.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


def plot(folder,rows,labels):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axes=plt.subplots(4,1,figsize=(10,8),sharex=True)
    t=np.array([r['time_ps'] for r in rows])/1000
    for ax,key in zip(axes,['rg_nm','contacts_per_carbon','nematic_order','hydration_waters']):
        ax.plot(t,[r[key] for r in rows],lw=.6); ax.set_ylabel(key)
    axes[-1].set_xlabel('Production time (ns)')
    fig.tight_layout(); fig.savefig(folder/'screening.png',dpi=140); plt.close(fig)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('root',type=Path)
    p.add_argument('--stride',type=int,default=10); p.add_argument('--discard-ns',type=float,default=20)
    p.add_argument('--gmx',default='gmx')
    a=p.parse_args()
    if a.stride<1 or a.discard_ns<0: p.error('stride must be positive and discard nonnegative')
    analyze(a.root.resolve(),a.stride,a.discard_ns,a.gmx)

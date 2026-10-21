"""Scientific diagnostic figures; geometry is never used as evidence of validity."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection,Poly3DCollection
from robustness import ROOT,OUT

def main():
    path=OUT/('full-audit.json' if (OUT/'full-audit.json').exists() else 'subset-audit.json')
    report=json.loads(path.read_text());systems=report['systems']
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    fig,axs=plt.subplots(2,2,figsize=(12,8),layout='constrained')
    for col,(name,s) in enumerate(systems.items()):
        for key,label,style in [('legacy_core_models','Last-core labels','-o'),('instantaneous_models','Nearest-center labels','--s')]:
            models=s[key];lag=[m['lag_frames'] for m in models]
            times=[m['implied_times_frames'][0] if m.get('implied_times_frames') else np.nan for m in models]
            axs[0,col].plot(lag,times,style,label=label)
            error=[max([h['weighted_row_TV'] for h in m.get('heldout_ck',[])] or [np.nan]) for m in models]
            axs[1,col].plot(lag,error,style,label=label)
        axs[0,col].set(title=f'{name.capitalize()}: implied slowest timescale',xlabel='Lag (frames)',ylabel='Timescale (frames)',xscale='log')
        axs[1,col].set(title='Held-out CK discrepancy',xlabel='Lag (frames)',ylabel='Maximum fold/multiple weighted TV',xscale='log',ylim=(0,1))
        axs[0,col].legend(fontsize=9)
    fig.suptitle('Model diagnostics precede mechanistic interpretation',size=16)
    fig.savefig(OUT/'kinetic-diagnostics.png',dpi=180);plt.close(fig)

    s=systems['chignolin'];h=s['mobility'];v=np.array(h['height_nm'],float);mask=np.array(h['supported'])
    ci=np.array(h['conditional_resampling_interval_nm'],float);lo,hi=np.array(h['limits']);bins=h['bins']
    x=np.linspace(lo[0],hi[0],bins,endpoint=False)+(hi[0]-lo[0])/bins/2
    y=np.linspace(lo[1],hi[1],bins,endpoint=False)+(hi[1]-lo[1])/bins/2
    xx,yy=np.meshgrid(x,y,indexing='ij');v[~mask]=np.nan
    fig=plt.figure(figsize=(13,8),layout='constrained')
    ax=fig.add_subplot(2,2,1,projection='3d')
    ax.plot_surface(xx,yy,v,cmap='viridis',edgecolor='.5',linewidth=.2,antialiased=True)
    ax.set(xlabel='CA Rg (nm)',ylabel='End-to-end (nm)',zlabel='RMS internal-distance change (nm)',title='Candidate height: structural mobility at 10 frames')
    ax.view_init(32,-58)
    ax=fig.add_subplot(2,2,2)
    plot=ax.pcolormesh(x,y,v.T,cmap='viridis',shading='nearest')
    fig.colorbar(plot,ax=ax,label='Mean displacement (nm)');ax.set(title='Supported conditional means',xlabel='CA Rg (nm)',ylabel='End-to-end (nm)')
    ax=fig.add_subplot(2,2,3);width=ci[1]-ci[0];width[~mask]=np.nan
    plot=ax.pcolormesh(x,y,width.T,cmap='magma',shading='nearest')
    fig.colorbar(plot,ax=ax,label='Resampling interval width (nm)');ax.set(title='Conditional resampling spread, not calibrated CI',xlabel='CA Rg (nm)',ylabel='End-to-end (nm)')
    ax=fig.add_subplot(2,2,4)
    plot=ax.pcolormesh(x,y,np.array(h['run_support']).T,cmap='cividis',shading='nearest')
    fig.colorbar(plot,ax=ax,label='Runs contributing to each bin');ax.set(title='Coverage is shown, not filled in',xlabel='CA Rg (nm)',ylabel='End-to-end (nm)')
    fig.suptitle(f'CLN025: {s["frames"]:,} frames, {s["runs"]:,} trajectories | a measured height, not free energy',size=15)
    fig.savefig(OUT/'mobility-height.png',dpi=180);plt.close(fig)

    # Re-embed the existing abstract nerve in a measured height without silently
    # declaring it to be a new cover of the full-deposit state space.
    legacy=json.loads((ROOT/'dist/chignolin/data.json').read_text())
    oldlo=np.array(legacy['chart']['min']);oldhi=np.array(legacy['chart']['max'])
    q=np.array([n['pos'] for n in legacy['nodes']])[:,[0,2]]
    q=oldlo+(q+15)/30*(oldhi-oldlo)
    ij=np.floor((q-lo)/(hi-lo)*bins).astype(int)
    valid=((ij>=0)&(ij<bins)).all(1);ij=np.clip(ij,0,bins-1)
    valid &= mask[ij[:,0],ij[:,1]]
    hv=np.array(h['height_nm'],float)[ij[:,0],ij[:,1]]
    xyz=np.column_stack([q,hv]);edges=np.array(legacy['edges']);faces=np.array(legacy['chains'])
    shown_edges=edges[valid[edges].all(1)];shown_faces=faces[valid[faces].all(1)]
    fig=plt.figure(figsize=(12,5),layout='constrained')
    for k,(elev,azim) in enumerate([(28,-60),(48,120)]):
        ax=fig.add_subplot(1,2,k+1,projection='3d')
        ax.add_collection3d(Poly3DCollection(xyz[shown_faces],facecolors=(.1,.5,.5,.10),edgecolors='none'))
        ax.add_collection3d(Line3DCollection(xyz[shown_edges],colors='black',linewidths=.6))
        ax.scatter(*xyz[valid].T,s=12,c=hv[valid],cmap='viridis')
        for idx in np.flatnonzero(valid):
            a,b=ij[idx];ax.plot([q[idx,0]]*2,[q[idx,1]]*2,ci[:,a,b],color='.5',alpha=.45,linewidth=.6)
        limits_low=xyz[valid].min(0);limits_high=xyz[valid].max(0)
        limits_low[2]=np.nanmin(ci[:,ij[valid,0],ij[valid,1]])
        limits_high[2]=np.nanmax(ci[:,ij[valid,0],ij[valid,1]])
        margin=(limits_high-limits_low)*.08+1e-5
        ax.set(xlim=(limits_low[0]-margin[0],limits_high[0]+margin[0]),
               ylim=(limits_low[1]-margin[1],limits_high[1]+margin[1]),
               zlim=(max(0,limits_low[2]-margin[2]),limits_high[2]+margin[2]),
               xlabel='CA Rg (nm)',ylabel='End-to-end (nm)',zlabel='Displacement (nm)')
        ax.view_init(elev,azim)
    fig.suptitle(f'Legacy CLN025 nerve with mobility height: {valid.sum()}/{len(valid)} supported vertices\n'
                 'Vertical bars: conditional resampling spread; unsupported vertices omitted',size=13)
    fig.savefig(OUT/'mobility-nerve.png',dpi=180);plt.close(fig)
    exported=dict(scope='Existing overlap nerve re-embedded using candidate mobility height; not a refitted full-deposit cover.',
                  height_units='nm',lag_frames=10,nodes=[dict(id=i,chart_nm=q[i].tolist(),supported=bool(valid[i]),
                      height_nm=float(hv[i]) if valid[i] else None) for i in range(len(valid))],edges=legacy['edges'],faces=legacy['chains'])
    (OUT/'mobility-nerve.json').write_text(json.dumps(exported,indent=2,allow_nan=False))

    rows=systems['alanine']['topology']['sensitivity'];fig,ax=plt.subplots(figsize=(11,5),layout='constrained')
    for periodic in [False,True]:
        r=[x for x in rows if x['periodic']==periodic and x['stride']==10]
        label='Periodic metric' if periodic else 'Cut chart'
        ax.plot([x['radius_deg'] for x in r],[x['truncated_beta2'] for x in r],'-o',label=label+': triangles only')
        ax.plot([x['radius_deg'] for x in r],[x['betti_0_1_2'][2] for x in r],'--s',label=label+': tetrahedra included')
    ax.set(xlabel='Cover radius (degrees)',ylabel='Second Betti number over GF(2)',title='Truncation can manufacture apparent 2-dimensional holes')
    ax.legend();fig.savefig(OUT/'topology-sensitivity.png',dpi=180);plt.close(fig)
    print('Rendered diagnostics from',path)

if __name__=='__main__':main()

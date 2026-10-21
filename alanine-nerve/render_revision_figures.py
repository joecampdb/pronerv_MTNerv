"""Scientific figures from the measured revision, with explicit missing support."""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection,Line3DCollection
from close_limitations import ROOT,DEST
OUT=ROOT/'paper/figures';OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'savefig.facecolor':'white'})

def nerve(ax,d,elev,azim,annotate=False):
 c=d['cover'];nodes=c['nodes'];valid=np.array([n['supported'] for n in nodes]);xyz=np.array([[*n['chart'],n['height_nm'] or 0] for n in nodes])
 def allowed(ids):
  return valid[list(ids)].all() and not (d['system']=='alanine' and np.any(np.ptp(xyz[list(ids),:2],axis=0)>180))
 edges=[e for e in c['edges'] if allowed(e)];chains=[f for f in c['chains'] if allowed(f)]
 if chains:ax.add_collection3d(Poly3DCollection(xyz[chains],facecolors=(.4,.4,.4,.055),edgecolors='none'))
 if edges:ax.add_collection3d(Line3DCollection(xyz[edges],colors='black',linewidths=.45,alpha=.55))
 for size,marker in [(1,'o'),(2,'s'),(3,'^')]:
  select=valid&np.array([len(n['simplex'])==size for n in nodes]);ax.scatter(*xyz[select].T,s=15,marker=marker,c='white',edgecolors='black',linewidths=.55,depthshade=False)
 if annotate and chains:
  f=chains[len(chains)//2]
  for i in f:ax.text(*xyz[i],f' v{i}',size=9)
  ax.text2D(.02,.98,'Example: '+' ⊂ '.join('{'+','.join(map(str,nodes[i]['simplex']))+'}' for i in f),transform=ax.transAxes,fontsize=8)
 for n in nodes:
  if n['supported']:
   x,y=n['chart'];low,high=n['interval_nm'];ax.plot([x,x],[y,y],[low,high],c='.6',lw=.4,alpha=.4)
 ax.auto_scale_xyz(xyz[valid,0],xyz[valid,1],xyz[valid,2]);ax.view_init(elev,azim)
 ax.set(xlabel='φ (degrees)' if d['system']=='alanine' else 'Cα Rg (nm)',ylabel='ψ (degrees)' if d['system']=='alanine' else 'End-to-end (nm)',zlabel='Mobility (nm)')
 ax.tick_params(labelsize=8)

def main():
 systems=[json.loads((DEST/(n+'-atlas.json')).read_text()) for n in ['alanine','chignolin']]
 for d in systems:
  fig=plt.figure(figsize=(13,6.2),layout='constrained')
  for i,(e,a) in enumerate([(28,-58),(55,120)]):nerve(fig.add_subplot(1,2,i+1,projection='3d'),d,e,a,True)
  supported=sum(n['supported'] for n in d['cover']['nodes'])
  fig.suptitle(f"{d['system'].capitalize()}: measured-height overlap nerve | {supported}/{len(d['cover']['nodes'])} supported vertices\n"
   'Edges: inclusions · plates: composable inclusion chains · bars: conditional spread',fontsize=13)
  legend=[Line2D([0],[0],marker=m,color='black',linestyle='none',markerfacecolor='white',label=l) for m,l in [('o','Cover set'),('s','Pair intersection'),('^','Triple intersection')]]
  fig.legend(handles=legend,loc='lower center',ncol=3,bbox_to_anchor=(.5,-.02))
  fig.savefig(OUT/(d['system']+'-measured-nerve.png'),dpi=180,bbox_inches='tight');plt.close(fig)
 fig=plt.figure(figsize=(13,9),layout='constrained')
 for row,d in enumerate(systems):
  h=d['height'];v=np.array(h['height_nm'],float);mask=np.array(h['supported']);v[~mask]=np.nan;lo,hi=np.array(h['limits']);n=h['bins']
  x=np.linspace(lo[0],hi[0],n+1);y=np.linspace(lo[1],hi[1],n+1)
  ax=fig.add_subplot(2,2,row*2+1);plot=ax.pcolormesh(x,y,v.T,cmap='viridis',shading='flat');fig.colorbar(plot,ax=ax,label='Mean structural mobility (nm)')
  ax.set(title=f"{d['system'].capitalize()} | lag {h['lag_frames']} frames | {mask.sum()} supported bins",xlabel='φ (degrees)' if row==0 else 'Cα Rg (nm)',ylabel='ψ (degrees)' if row==0 else 'End-to-end (nm)')
  ax=fig.add_subplot(2,2,row*2+2,projection='3d');nerve(ax,d,30,-60);ax.set_title('Same measured field, categorical overlay')
 fig.suptitle('Revised Figure 9: a declared observable replaces illustrative occupancy height\nAlanine: pair-weighted mean, 100 ps lag. CLN025: root-balanced mean, 10-frame lag; clock unresolved.',fontsize=13)
 fig.savefig(OUT/'measured-height-revision.png',dpi=180);plt.close(fig)
 # Predictive diagnostics use the coarser initial-preparation grouping when present.
 suffix='-initial-cohorts' if (DEST/'05-predictive-validation-initial-cohorts.json').exists() else ''
 p=json.loads((DEST/('05-predictive-validation'+suffix+'.json')).read_text())['results']
 k=json.loads((DEST/('07-kinetic-validation'+suffix+'.json')).read_text())['results']
 fig,axs=plt.subplots(1,2,figsize=(12,4.6),layout='constrained')
 features=['chart','distances','torsions_phi_psi_omega','combined','combined_history20']
 for target,label in [('distances','Future Cα distances'),('omega_periodic','Future peptide omega'),('NMR_distance_deviation_nm','Future NMR-distance deviation')]:
  values=[[r['ratio'] for r in p if r['features']==f and r['target']==target and r['lag_frames']==10] for f in features]
  axs[0].plot(range(5),[np.median(v) for v in values],'-o',label=label)
 axs[0].axhline(1,color='.4',ls='--');axs[0].set(xticks=range(5),xticklabels=['Chart','Distances','Torsions','Combined','+ history'],ylabel='Median outer-fold MSE / persistence',title='Nested prediction at 10 frames');axs[0].tick_params(axis='x',rotation=20);axs[0].legend(fontsize=8)
 for feature,style in [('distances','-o'),('combined','--s')]:
  for key,label in [('weighted_TV','weighted rows'),('max_row_TV','worst row')]:
   val=[[r[key] for r in k if r['features']==feature and r['states']==states and r['lag_frames']==10 and r['multiple']==2 and r[key] is not None] for states in [4,8,16]]
   axs[1].plot([4,8,16],[np.median(v) for v in val],style,label=feature+', '+label)
 axs[1].set(xlabel='Train-fitted state count',ylabel='Median held-out total variation',title='CK discrepancy at 2 × 10 frames',ylim=(0,1));axs[1].legend(fontsize=8)
 fig.suptitle('CLN025: initial-cohort holdout diagnostics, not a kinetic validation certificate',fontsize=13)
 fig.savefig(OUT/'prediction-kinetics-revision.png',dpi=180);plt.close(fig)
 print('Revised figures saved',flush=True)

if __name__=='__main__':main()

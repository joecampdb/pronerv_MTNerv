"""Exploratory held-out feature sufficiency screen; not interface selection.

Predict future CA distance vectors, with training-only scaling and linear ridge
regression. Compare with persistence. Filename-inferred roots are held out together.
"""
import argparse,json
from pathlib import Path
import numpy as np
from robustness import OUT,lineage_groups

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--full',action='store_true');args=parser.parse_args()
    z=np.load(OUT/('chignolin-full-features.npz' if args.full else 'chignolin-features.npz'))
    q=z['q'];d=z['distances'];tors=z['torsions'];audit=json.loads(str(z['audit']))
    lengths=z['lengths'];epoch=np.array([x['epoch'] for x in audit['timing']])
    roots,folds,lineage=lineage_groups(audit['timing'])
    rows=[]
    for lag in [1,10,50]:
        start=0;origins=[];groups=[]
        for n,g in zip(lengths,folds):
            ix=np.arange(start,start+n-lag,5);origins.extend(ix);groups.extend([g]*len(ix));start+=n
        origins=np.array(origins);groups=np.array(groups)
        y=d[origins+lag].astype(float);persistence=d[origins].astype(float)
        tf=np.concatenate([np.sin(tors[origins]),np.cos(tors[origins])],axis=1)
        candidates={'Rg_end_to_end':q[origins], 'all_CA_distances':d[origins],
                    'backbone_sin_cos':tf,'distances_plus_torsions':np.concatenate([d[origins],tf],axis=1)}
        for group in sorted(set(groups)):
            train=groups!=group;test=groups==group
            ymean=y[train].mean(0);den=((y[test]-ymean)**2).mean()
            base=((y[test]-persistence[test])**2).mean()
            for name,x in candidates.items():
                mu=x[train].mean(0);std=x[train].std(0);std[std<1e-8]=1
                xt=(x[train]-mu)/std;xe=(x[test]-mu)/std
                a=xt.T@xt/len(xt)+np.eye(xt.shape[1])*1e-3
                weights=np.linalg.solve(a,xt.T@(y[train]-ymean)/len(xt))
                mse=float(((xe@weights+ymean-y[test])**2).mean())
                rows.append(dict(lag_frames=lag,heldout_root_group=int(group),features=name,
                                 train_pairs=int(train.sum()),test_pairs=int(test.sum()),
                                 rmse_nm=float(np.sqrt(mse)),R2_vs_training_mean=float(1-mse/den),
                                 mse_ratio_to_persistence=float(mse/base)))
    out=dict(method='Fixed ridge 0.001; stride 5; entire held-out inferred root lineages; no hyperparameter tuning',lineage=lineage,
             warning='An exploratory predictive screen; inferred roots are not proven independent preparations. Not validated interfaces or folding kinetics.',results=rows)
    path=OUT/('full-feature-screen.json' if args.full else 'subset-feature-screen.json')
    path.write_text(json.dumps(out,indent=2),encoding='utf-8');print(path)

if __name__=='__main__':main()

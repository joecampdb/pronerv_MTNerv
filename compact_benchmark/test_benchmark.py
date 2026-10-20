import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import json
import numpy as np
import torch
from geometry import torsions,rebuild,features
from models import Model,loss
from run import indices

def chain():
    rng=np.random.default_rng(7)
    return np.cumsum(rng.normal(size=(50,3)),axis=0).astype("float32")

def test_internal_coordinate_roundtrip_and_equivariance():
    x=chain();x-=x.mean(0);phi=torsions(x)
    assert np.max(np.abs(rebuild(x,phi)-x))<1e-4
    q,_=np.linalg.qr(np.random.default_rng(2).normal(size=(3,3)))
    if np.linalg.det(q)<0:q[:,-1]*=-1
    assert np.allclose(rebuild(x@q+7,phi),rebuild(x,phi)@q,atol=1e-4)
    assert np.allclose(rebuild(x@q+7,phi,center=False),rebuild(x,phi,center=False)@q+7,atol=1e-4)

def test_matching_capacity_and_invariance():
    cfg=json.loads((Path(__file__).parent/"config.json").read_text())
    torch.set_num_threads(1);x=chain();h=np.ones(50)*8
    q,_=np.linalg.qr(np.random.default_rng(3).normal(size=(3,3)))
    if np.linalg.det(q)<0:q[:,-1]*=-1
    counts=[]
    for kind in ["matrix_gnn","sheaf"]:
        torch.manual_seed(7);model=Model(kind,cfg);counts.append(sum(p.numel() for p in model.parameters()))
        f=features(x,x,h,h)
        def output(a):return model(torch.tensor(a[None],dtype=torch.float32),torch.tensor(a[None],dtype=torch.float32),torch.tensor(f[None]))
        first=output(x);second=output(x@q+2)
        for a,b in zip(first,second):assert torch.allclose(a,b,atol=2e-5)
        objective,*_=loss(first,torch.tensor(torsions(x)[None]),torch.tensor(h[None]),.1)
        objective.backward()
        assert all(layer[0].weight.grad.abs().sum()>0 for layer in model.maps)
    assert counts[0]==counts[1]

def test_split_uses_history_and_target_boundaries_not_future_label():
    data={"time_ns":np.arange(0,10.1,.1),"compact":np.ones(101,dtype=bool)}
    data["compact"][30]=False
    ids=indices(data,[2,4])
    assert 29 in ids and 30 not in ids
    assert np.all(data["time_ns"][ids-1]>=2-1e-6)
    assert np.all(data["time_ns"][ids+1]<=4+1e-6)

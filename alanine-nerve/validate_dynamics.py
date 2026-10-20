"""Independent checks against raw samples, not against the rendering."""
from pathlib import Path
import json
import numpy as np
root=Path(__file__).parent
d=json.loads((root/"dist/dynamics.json").read_text())
raw=np.load(root/"data/alanine-dipeptide-3x250ns-backbone-dihedrals.npz")
atomic=np.load(root/"data/alanine-dipeptide-3x250ns-heavy-atom-positions.npz")
centers=np.array([b["angles"] for b in d["basins"]])
counts=[]
for key in raw:
    angles=np.rad2deg(raw[key]).astype(float)
    distances=np.linalg.norm((angles[:,None]-centers+180)%360-180,axis=2)
    # Independent count: delete non-core samples and count remaining changes.
    core=distances.argmin(1)[distances.min(1)<=25]
    changed=core[:-1]!=core[1:]
    c=np.zeros((4,4),int)
    np.add.at(c,(core[:-1][changed],core[1:][changed]),1)
    counts.append(c)
    shifted=np.linalg.norm((angles[:,None]+[360,-360]-centers+180)%360-180,axis=2)
    assert np.allclose(distances,shifted,atol=1e-10)
for e in d["edges"]:
    assert e["perRunCounts"]==[int(c[e["source"],e["target"]]) for c in counts]
    rep=e["representative"]
    assert 0<=rep["startPs"]<rep["endPs"]<250000
    arr=np.rad2deg(raw[f'arr_{rep["run"]-1}'])
    expected=atomic[f'arr_{rep["run"]-1}'][rep["startPs"]:rep["endPs"]+1].reshape(-1,10,3).astype(float)
    expected-=expected.mean(1,keepdims=True)
    assert np.allclose(rep["molecularFrames"],expected,atol=5.1e-8,rtol=0)
    assert len(rep["molecularFrames"])==len(rep["frameAngles"])==rep["endPs"]-rep["startPs"]+1
    assert np.allclose(rep["frameAngles"],arr[rep["startPs"]:rep["endPs"]+1],atol=1e-6)
    for p,t in [(rep["angles"][0],rep["startPs"]),(rep["angles"][-1],rep["endPs"])]:
        assert np.max(np.abs((np.array(p)-arr[t]+180)%360-180))<1e-4
for lag,model in d["lagModels"].items():
    count=np.array(model["counts"])
    assert np.array_equal(count,np.array(model["perRunCounts"]).sum(0))
    assert count.sum()==sum(250000-int(lag)-n for n in d["initialUnassignedFrames"])
    assert np.allclose(model["probabilities"],count/count.sum(1)[:,None])
assert len(d["chains"])==25
assert all(d["edges"][a]["target"]==d["edges"][b]["source"] for a,b in d["chains"])
print("PASS: independent passage counts, periodic invariance, route provenance, run-safe lag counts, probabilities, and composition endpoints")

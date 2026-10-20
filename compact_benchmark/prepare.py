"""Extract per-carbon hydration from completed trajectories; preserve frozen labels."""
import hashlib,json,sys
from pathlib import Path
import numpy as np
import MDAnalysis as mda
from MDAnalysis.lib.distances import distance_array
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from analyze import unwrap_chain
OUT=ROOT/"compact_benchmark/data";OUT.mkdir(exist_ok=True)
definition=hashlib.sha256((ROOT/"transition_definition.json").read_bytes()).hexdigest()
assert definition==json.loads((ROOT/"reports/transition_events/report.json").read_text())["definition_sha256"]
for rep in ["rep01","rep02"]:
    folder=ROOT/"runs/PE25"/rep
    assert (folder/"prod.done.json").exists()
    u=mda.Universe(str(folder/"prod.gro"),str(folder/"prod.xtc"))
    water=u.select_atoms("resname SOL and name OW")
    xs=[]; hs=[]; ts=[]
    for frame in range(20000,100001,100):
        t=u.trajectory[frame];assert abs(t.time-frame)<.1
        x=unwrap_chain(u.atoms[:50].positions/10,t.dimensions[:3]/10)
        h=(distance_array(u.atoms[:50].positions,water.positions,box=t.dimensions)<4.5).sum(1)
        xs.append(x-x.mean(0));hs.append(h);ts.append(t.time/1000)
    labels=np.genfromtxt(ROOT/f"reports/transition_events/{rep}_states.csv",delimiter=",",names=True)
    core=labels["core_label_minus1_undecided_0_C_1_E"][np.arange(2000,10001,10)]==0
    np.savez_compressed(OUT/f"{rep}.npz",x=np.array(xs,dtype="float32"),h=np.array(hs,dtype="float32"),time_ns=ts,compact=core)
    print(rep,"prepared",flush=True)
provenance={"definition_sha256":definition,"sampling_ps":100,"coordinates":"Ordered, unwrapped backbone; translation removed; no per-frame rotational fit.",
            "hydration":"Per-carbon count of water oxygens within 0.45 nm (not a sum of unique waters).",
            "sources":{}}
for rep in ["rep01","rep02"]:
    folder=ROOT/"runs/PE25"/rep
    provenance["sources"][rep]={"completion":json.loads((folder/"prod.done.json").read_text()),
        "xtc_size":(folder/"prod.xtc").stat().st_size,"data_sha256":hashlib.sha256((OUT/f"{rep}.npz").read_bytes()).hexdigest()}
(OUT/"provenance.json").write_text(json.dumps(provenance,indent=2))

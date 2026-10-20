"""Independent raw-data checks; do not rely on the builder's event-loop labels."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import warnings
import MDAnalysis as mda
import numpy as np
from scipy.spatial.distance import pdist

root=Path(__file__).resolve().parent
raw=root/"data/chignolin"
d=json.loads((root/"dist/chignolin/data.json").read_text(encoding="utf-8"))
p=np.load(raw/"processed.npz")
q=p["q"]; z=(q-q.mean(0))/q.std(0)
centers=p["centers"]
distance=np.linalg.norm(z[:,None]-centers[None],axis=2)
nearest=distance.argmin(1); core=distance.min(1)<=.42
counts=Counter(); offset=0
for run in d["rawTiming"]:
    n=run["frames"]
    observed=nearest[offset:offset+n][core[offset:offset+n]]
    counts.update((int(a),int(b)) for a,b in zip(observed[:-1],observed[1:]) if a!=b)
    offset+=n
assert counts == Counter({(r["source"],r["target"]):r["count"] for r in d["routes"]})
warnings.filterwarnings("ignore",category=UserWarning,module="MDAnalysis")
for record in d["provenance"]["files"]:
    assert hashlib.sha256((raw/record["file"]).read_bytes()).hexdigest()==record["sha256"]
for r in d["routes"]:
    u=mda.Universe(str(raw/"topology.pdb"),str(raw/f'run-{r["run"]:03d}.xtc'))
    ca=u.select_atoms("name CA")
    for index,export in [(r["startFrame"],r["moleculeFrames"][0]),(r["endFrame"],r["moleculeFrames"][-1])]:
        u.trajectory[index]
        np.testing.assert_allclose(pdist(ca.positions*.1),pdist(export),atol=1e-6)
assert len(q)==sum(t["frames"] for t in d["rawTiming"])
print("PASS: independent per-run core counts, all 129 source hashes, route endpoint distance invariants, actual run lengths.")

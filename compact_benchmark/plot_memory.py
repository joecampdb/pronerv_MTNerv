"""Plot completed benchmark contact memory without changing training."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
out=Path(__file__).resolve().parents[1]/"reports/compact_benchmark"
r=json.loads((out/"results.json").read_text())
fig,axes=plt.subplots(1,2,figsize=(11,4),layout="constrained")
for ax,source in zip(axes,["rep01","rep02"]):
    subset=[a for a in r if a["source"]==source]
    keys=list(subset[0]["rollout"]["reference_contact_memory"])
    x=np.array(list(map(float,keys)))
    ax.plot(x,[subset[0]["rollout"]["reference_contact_memory"][k] for k in keys],"k--o",label="Matched MD continuations")
    for name,color in [("matrix_gnn","#507c9f"),("sheaf","#bd803c")]:
        y=np.array([[a["rollout"]["generated_contact_memory"][k] for k in keys] for a in subset if a["model"]==name])
        ax.plot(x,y.mean(0),"-o",color=color,label=name)
        ax.fill_between(x,y.min(0),y.max(0),color=color,alpha=.15)
    target="rep02" if source=="rep01" else "rep01"
    ax.set(title=f"Train {source} → test {target}",xlabel="Lag (ns)",ylabel="Normalized contact memory")
    ax.legend(fontsize=8)
fig.suptitle("5 ns rollouts from held-out compact initial states\nShading: seed range. Memory scores do not override physical-validity failures.",fontsize=11)
fig.savefig(out/"contact_memory.png",dpi=160)

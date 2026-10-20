import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/"reports/compact_benchmark"
r=json.loads((OUT/"results.json").read_text())
groups=[]
for source in ["rep01","rep02"]:
    for model in ["matrix_gnn","sheaf"]:
        items=[x for x in r if x["source"]==source and x["model"]==model]
        if not items: continue
        fields={"test_NLL":[a["test"]["torsion_nll_per_angle"] for a in items],
                "memory_RMSE":[a["rollout"]["contact_memory_RMSE"] for a in items],
                "clash_fraction":[a["rollout"]["generated"]["nonlocal_clash_fraction"] for a in items],
                "reference_clash_fraction":[a["rollout"]["reference"]["nonlocal_clash_fraction"] for a in items],
                "Rg_relative_error":[abs(a["rollout"]["generated"]["rg_mean_nm"]/a["rollout"]["reference"]["rg_mean_nm"]-1) for a in items],
                "contacts_relative_error":[abs(a["rollout"]["generated"]["contacts_mean"]/a["rollout"]["reference"]["contacts_mean"]-1) for a in items]}
        groups.append(dict(source=source,model=model,seeds=len(items),parameters=items[0]["parameters"],
            metrics={k:dict(mean=float(np.mean(v)),min=float(min(v)),max=float(max(v))) for k,v in fields.items()}))
summary=dict(groups=groups,complete=(OUT/"complete.json").exists(),
             caveat="Seed ranges are not independent-trajectory confidence intervals. Physical rollout failures preclude a dynamics-superiority claim.")
summary["rollout_issues"]=[f"{g['source']} {g['model']}" for g in groups
    if g["metrics"]["clash_fraction"]["mean"]>g["metrics"]["reference_clash_fraction"]["mean"]+.05
    or g["metrics"]["Rg_relative_error"]["mean"]>.10 or g["metrics"]["contacts_relative_error"]["mean"]>.10]
summary["decision"]="NO_VALIDATED_DYNAMICS_ADVANTAGE_ROLLOUT_FAILURES" if summary["rollout_issues"] else "REVIEW_PAIRED_HELDOUT_SCORES_NO_CONFIRMATORY_CLAIM"
(OUT/"summary.json").write_text(json.dumps(summary,indent=2))
fig,axs=plt.subplots(1,3,figsize=(12,4),layout="constrained")
labels=[g["source"]+"\n"+g["model"] for g in groups]
for ax,key,title in zip(axs,["test_NLL","memory_RMSE","clash_fraction"],["Held-out torsion NLL / angle","Contact-memory RMSE","Generated clash fraction"]):
    values=[g["metrics"][key]["mean"] for g in groups]
    ax.bar(np.arange(len(groups)),values,color=["#507c9f" if g["model"]=="matrix_gnn" else "#bd803c" for g in groups])
    ax.errorbar(np.arange(len(groups)),values,yerr=[[v-g["metrics"][key]["min"] for v,g in zip(values,groups)],
                [g["metrics"][key]["max"]-v for v,g in zip(values,groups)]],fmt="none",color="black",capsize=3)
    ax.set_xticks(np.arange(len(groups)),labels,fontsize=8);ax.set_title(title,fontsize=10)
fig.suptitle("Compact-dynamics development benchmark • bars: seed means; whiskers: seed ranges")
fig.savefig(OUT/"benchmark.png",dpi=160)
print(json.dumps(summary,indent=2))

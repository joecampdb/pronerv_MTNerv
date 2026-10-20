"""Frozen PE25 core-state detector. Analyze completed replicas only."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent

def classify(rows, cfg):
    """Trailing medians use no future data; first full window is required."""
    times=np.array([r["time_ps"] for r in rows],dtype=float)
    values=np.array([[r[k] for k in ["rg_nm","contacts_per_carbon","hydration_waters"]] for r in rows])
    if not np.isfinite(values).all() or not np.isfinite(times).all():
        raise ValueError("Nonfinite observables")
    dt=cfg["sampling_ps"]
    if len(times)<2 or not np.allclose(np.diff(times),dt,atol=.01):
        raise ValueError("Missing, duplicate or irregular samples; cannot infer continuous residence")
    n=max(1,int(round(cfg["smoothing_ps"]/dt)))
    smooth=np.full(values.shape,np.nan)
    for i in range(n-1,len(values)):
        smooth[i]=np.median(values[i-n+1:i+1],axis=0)
    c=cfg["compact"]; e=cfg["expanded"]
    compact=(smooth[:,0]<=c["rg_max_nm"]) & (smooth[:,1]>=c["contacts_min"]) & (smooth[:,2]<=c["hydration_max"])
    expanded=(smooth[:,0]>=e["rg_min_nm"]) & (smooth[:,1]<=e["contacts_max"]) & (smooth[:,2]>=e["hydration_min"])
    if np.any(compact & expanded): raise ValueError("Core states overlap")
    labels=np.full(len(times),-1,dtype=int); labels[compact]=0; labels[expanded]=1
    return times,labels,smooth

def detect(times, labels, dwell_ps, discard_ns=0):
    """Commitments and completed C-E-C cycles; initial E is not an expansion."""
    last=None; candidate=None; start=None; entries=[]; cycles=[]; open_cycle=None
    for t,label in zip(times,labels):
        if t<discard_ns*1000: continue
        if label<0:
            candidate=None; start=None; continue
        if label!=candidate:
            candidate=int(label); start=float(t)
        if t-start>=dwell_ps and candidate!=last:
            event=dict(state="C" if candidate==0 else "E",core_entry_ns=start/1000,
                       confirmed_ns=float(t)/1000)
            entries.append(event)
            if last==0 and candidate==1:
                open_cycle={"expanded_core_entry_ns":start/1000,"expansion_confirmed_ns":float(t)/1000}
            elif last==1 and candidate==0 and open_cycle is not None:
                open_cycle.update(compact_core_return_ns=start/1000,recollapse_confirmed_ns=float(t)/1000)
                cycles.append(open_cycle); open_cycle=None
            last=candidate
    return dict(commitments=entries,cycles=cycles,complete_cycles=len(cycles),
                unfinished_expansion=open_cycle,initial_committed_state=entries[0]["state"] if entries else None)

def variants(cfg):
    yield "primary",cfg
    for dwell in [100,500,1000]:
        yield f"dwell_{dwell}ps",dict(cfg,commitment_ps=dwell)
    for smooth in [50,200]:
        yield f"smooth_{smooth}ps",dict(cfg,smoothing_ps=smooth)
    for discard in [10,40]:
        yield f"discard_{discard}ns",dict(cfg,discard_ns=discard)
    yield "strict",dict(cfg,expanded=dict(rg_min_nm=.90,contacts_max=1.2,hydration_min=100))
    yield "loose",dict(cfg,expanded=dict(rg_min_nm=.80,contacts_max=1.5,hydration_min=92))

def main():
    from analyze import extract,energy_checks
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--gmx",default=str(ROOT/"vendor/gromacs-install/bin/gmx"))
    args=p.parse_args()
    definition=ROOT/"transition_definition.json"
    cfg=json.loads(definition.read_text())
    out=ROOT/"reports/transition_events"; out.mkdir(parents=True,exist_ok=True)
    manifest=json.loads((ROOT/"runs/manifest.json").read_text())
    report=dict(definition=cfg,definition_sha256=hashlib.sha256(definition.read_bytes()).hexdigest(),
                replicas={},pending=[],notice="Calibration on replica 1; other replicas are prospective. Counts are not independent events or validated rates.")
    for entry in manifest["replicates"]:
        if entry["system"]!="PE25": continue
        folder=ROOT/"runs"/entry["relative_path"]
        if not (folder/"prod.done.json").exists():
            report["pending"].append(entry["relative_path"]); continue
        cache=out/(folder.name+"_observables.json")
        if cache.exists(): rows=json.loads(cache.read_text())
        elif folder.name=="rep01":
            rows=json.loads((ROOT/"reports/PE25_rep01/observables.json").read_text())
        else:
            rows=extract(folder,10)
        if rows[-1]["time_ps"]<100000: raise ValueError("Completed trajectory shorter than 100 ns")
        cache.write_text(json.dumps(rows))
        results={}
        for name,config in variants(cfg):
            times,labels,smooth=classify(rows,config)
            results[name]=detect(times,labels,config["commitment_ps"],config["discard_ns"])
        robust=[]
        for cycle in results["primary"]["cycles"]:
            if all(any(max(cycle["expanded_core_entry_ns"],other["expanded_core_entry_ns"]) <
                           min(cycle["compact_core_return_ns"],other["compact_core_return_ns"])
                       for other in results[variant]["cycles"])
                   for variant in ["strict","dwell_500ps","smooth_50ps","smooth_200ps"]):
                robust.append(cycle)
        times,labels,smooth=classify(rows,cfg)
        baseline=(times>=20000)&(times<60000)
        baseline_result=detect(times[baseline],labels[baseline],cfg["commitment_ps"])
        thermo,warnings=energy_checks(folder,args.gmx)
        if min(r["image_distance_or_lower_bound_nm"] for r in rows)<2.4: warnings.append("periodic-image proximity")
        if max(r["max_cc_bond_nm"] for r in rows)>.2: warnings.append("backbone bond distortion")
        for path in folder.glob("*.log"):
            text=path.read_text(errors="replace")
            if "LINCS WARNING" in text or "Fatal error:" in text: warnings.append("numerical error: "+path.name)
        item=dict(preparation=entry["preparation"],role="calibration" if folder.name=="rep01" else "prospective",
                  results=results,robust_cycles=robust,early_window_check=baseline_result,thermodynamics=thermo,warnings=warnings)
        report["replicas"][entry["relative_path"]]=item
        np.savetxt(out/(folder.name+"_states.csv"),np.column_stack([times,labels,smooth]),
                   delimiter=",",header="time_ps,core_label_minus1_undecided_0_C_1_E,median_rg_nm,median_contacts,median_hydration",comments="")
        plot(out,folder.name,times,labels,smooth,cfg,results["primary"])
    qualifying=[]
    for name,item in report["replicas"].items():
        r=item["results"]
        if item["role"]=="prospective" and not item["warnings"] and len(item["robust_cycles"])>=2:
            qualifying.append(name)
    report["qualifying_prospective_replicas"]=qualifying
    report["decision"]="PROSPECTIVE_RECURRENCE_SUPPORTED" if len(qualifying)>=2 else ("PENDING_PROSPECTIVE_DATA" if report["pending"] else "RECURRENCE_CRITERION_NOT_MET")
    (out/"report.json").write_text(json.dumps(report,indent=2))
    print(json.dumps({name:{v:r["complete_cycles"] for v,r in item["results"].items()} for name,item in report["replicas"].items()},indent=2))
    print(report["decision"],report["pending"])

def plot(out,name,times,labels,smooth,cfg,result):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig,axes=plt.subplots(4,1,figsize=(11,8),sharex=True)
    bounds=[(cfg["compact"]["rg_max_nm"],cfg["expanded"]["rg_min_nm"]),
            (cfg["compact"]["contacts_min"],cfg["expanded"]["contacts_max"]),
            (cfg["compact"]["hydration_max"],cfg["expanded"]["hydration_min"])]
    for i,(ax,title) in enumerate(zip(axes,["Rg (nm)","Contacts / carbon","Hydration waters"])):
        ax.plot(times/1000,smooth[:,i],lw=.8,color="#315776")
        ax.axhline(bounds[i][0],color="#348650",ls="--",label="Compact boundary")
        ax.axhline(bounds[i][1],color="#c07829",ls="--",label="Expanded boundary")
        ax.set_ylabel(title)
    axes[0].legend(loc="upper left",fontsize=8)
    axes[3].scatter(times/1000,labels,s=1,color="#315776")
    axes[3].set_yticks([-1,0,1],["Undecided","Compact","Expanded"])
    axes[3].set_xlabel("Production time (ns)")
    for ax in axes:
        ax.axvline(cfg["discard_ns"],color="gray",ls=":")
        for cycle in result["cycles"]:
            ax.axvspan(cycle["expanded_core_entry_ns"],cycle["compact_core_return_ns"],color="#e5af61",alpha=.25)
    fig.suptitle(f"{name}: frozen joint-core definition; {result['complete_cycles']} completed expansion–recollapse cycles\n100 ps trailing medians; 200 ps core commitment. Shading includes intervening undecided frames.")
    fig.tight_layout(); fig.savefig(out/(name+"_events.png"),dpi=150); plt.close(fig)

if __name__=="__main__": main()

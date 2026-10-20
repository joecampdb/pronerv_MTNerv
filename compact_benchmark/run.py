"""CPU-only, two-fold whole-replica transfer benchmark; no simulation modifications."""
import os
os.environ.setdefault("OMP_NUM_THREADS","2")
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
import torch
from models import Model,loss
from geometry import features,torsions,rebuild,contacts,observables

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
def indices(data,interval):
    t=data["time_ns"]; ids=np.arange(1,len(t)-1)
    # History, current and target all belong to the same temporal block.
    return ids[(t[ids-1]>=interval[0]-1e-6)&(t[ids+1]<=interval[1]+1e-6)&data["compact"][ids]]

def load(rep):
    z=dict(np.load(HERE/f"data/{rep}.npz"))
    z["features"]=np.array([features(z["x"][i],z["x"][max(0,i-1)],z["h"][i],z["h"][max(0,i-1)]) for i in range(len(z["x"]))])
    z["phi"]=torsions(z["x"])
    return z

def batch(data,ids):
    return [torch.tensor(v,dtype=torch.float32) for v in
            [data["x"][ids],data["x"][ids-1],data["features"][ids],data["phi"][ids+1],data["h"][ids+1]]]

def evaluate(model,data,ids,cfg):
    model.eval(); total=np.zeros(3); n=0
    with torch.no_grad():
        for group in np.array_split(ids,max(1,int(np.ceil(len(ids)/32)))):
            b=batch(data,group); vals=loss(model(*b[:3]),*b[3:],cfg["hydration_weight"])
            total+=np.array([v.item() for v in vals])*len(group);n+=len(group)
    return dict(zip(["objective","torsion_nll_per_angle","hydration_log_mse"],(total/n).tolist()))

def memory(c,p):
    y=c.astype(float)-p;out={}
    for lag in [1,2,5,10,20]:
        a=y[:,:-lag];b=y[:,lag:]
        den=np.sqrt(np.sum(a*a)*np.sum(b*b))
        out[str(lag/10)]=float(np.sum(a*b)/den) if den>0 else None
    return out

def rollout(model,data,cfg,seed):
    rng=np.random.default_rng(seed+7000);starts=[]
    for t in cfg["rollout_starts_ns"]:
        i=int(np.argmin(abs(data["time_ns"]-t)))
        if data["compact"][i] and i+cfg["rollout_steps"]<len(data["x"]): starts.append(i)
    if not starts: raise RuntimeError("No eligible rollout initial states")
    ids=np.repeat(starts,cfg["rollout_repeats"]);x=data["x"][ids].copy();prev=data["x"][ids-1].copy()
    h=data["h"][ids].copy();hp=data["h"][ids-1].copy()
    generated=[x.copy()];clipped=0;clash=[];model.eval()
    with torch.no_grad():
        for step in range(cfg["rollout_steps"]):
            f=np.array([features(a,b,c,d) for a,b,c,d in zip(x,prev,h,hp)])
            mu,k,logits,hyd=model(torch.tensor(x),torch.tensor(prev),torch.tensor(f))
            mu=mu.numpy();k=k.numpy();probs=torch.softmax(logits,-1).numpy()
            component=np.array([rng.choice(len(p),p=p) for p in probs])
            chosen_mu=np.array([mu[j,:,v] for j,v in enumerate(component)])
            chosen_k=np.array([k[j,:,v] for j,v in enumerate(component)])
            phi=rng.vonmises(chosen_mu,chosen_k)
            new=np.array([rebuild(a,b) for a,b in zip(x,phi)],dtype="float32")
            predicted=hyd.numpy();clipped+=int(np.sum((predicted<0)|(predicted>np.log(101))))
            hp,h=h,np.expm1(np.clip(predicted,0,np.log(101))).astype("float32")
            prev,x=x,new;generated.append(x.copy())
    generated=np.stack(generated,axis=1)
    ref=np.array([data["x"][i:i+cfg["rollout_steps"]+1] for i in starts])
    def summarize(arr):
        cc=np.array([[contacts(frame) for frame in traj] for traj in arr])
        oo=[observables(frame) for traj in arr for frame in traj[1:]]
        return cc,dict(rg_mean_nm=float(np.mean([v["rg_nm"] for v in oo])),
                      rg_std_nm=float(np.std([v["rg_nm"] for v in oo])),
                      contacts_mean=float(np.mean([v["contacts_per_carbon"] for v in oo])),
                      nonlocal_clash_fraction=float(np.mean([v["nonlocal_clash"] for v in oo])))
    gc,gs=summarize(generated);rc,rs=summarize(ref);p=rc.mean((0,1))
    gm=memory(gc,p);rm=memory(rc,p)
    err=float(np.sqrt(np.mean([(gm[k]-rm[k])**2 for k in gm])))
    return dict(starts_ns=data["time_ns"][starts].tolist(),generated=gs,reference=rs,
                generated_contact_memory=gm,reference_contact_memory=rm,contact_memory_RMSE=err,
                hydration_clipped_fraction=clipped/(len(ids)*50*cfg["rollout_steps"]),
                reference_note="Matched 5 ns continuations from held-out compact initial states; no future-state filtering. Reference contact mean used only for evaluation.",
                geometry_note="Bond lengths/angles retained from each rollout initial state. No clash rejection, thermostat, force field or Metropolis correction."),generated

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--smoke",action="store_true");args=parser.parse_args()
    cfg=json.loads((HERE/"config.json").read_text())
    if args.smoke: cfg.update(epochs=1,seeds=[17],rollout_steps=25,rollout_repeats=1,rollout_starts_ns=[25])
    torch.set_num_threads(cfg["torch_threads"])
    out=ROOT/"reports"/("compact_benchmark_smoke" if args.smoke else "compact_benchmark");out.mkdir(exist_ok=True)
    provenance=json.loads((HERE/"data/provenance.json").read_text())
    assert provenance["definition_sha256"]==hashlib.sha256((ROOT/"transition_definition.json").read_bytes()).hexdigest()
    codehash={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in HERE.glob("*.py")}
    runmeta=dict(config=cfg,code_sha256=codehash,data=provenance,torch_version=torch.__version__,started=time.time())
    (out/"run_manifest.json").write_text(json.dumps(runmeta,indent=2))
    data={rep:load(rep) for rep in ["rep01","rep02"]};results=[];splits={}
    for source,target in [("rep01","rep02"),("rep02","rep01")]:
        tr=indices(data[source],cfg["train_ns"]);va=indices(data[source],cfg["validation_ns"]);te=indices(data[target],cfg["test_ns"])
        assert max(data[source]["time_ns"][tr+1])<min(data[source]["time_ns"][va-1])
        splits[source]=dict(train_replica=source,test_replica=target,
            train_times_ns=data[source]["time_ns"][tr].tolist(),validation_times_ns=data[source]["time_ns"][va].tolist(),
            test_times_ns=data[target]["time_ns"][te].tolist(),selection="Current compact label only; no target conditioning.")
        (out/"splits.json").write_text(json.dumps(splits,indent=2))
        for seed in cfg["seeds"]:
            counts=[]
            for kind in cfg["models"]:
                torch.manual_seed(seed);rng=np.random.default_rng(seed)
                model=Model(kind,cfg);counts.append(sum(p.numel() for p in model.parameters()))
                f=data[source]["features"][tr]
                model.feature_mean.copy_(torch.tensor(f.mean((0,1))))
                model.feature_scale.copy_(torch.tensor(np.maximum(f.std((0,1)),.1)))
                optimizer=torch.optim.AdamW(model.parameters(),lr=cfg["learning_rate"],weight_decay=1e-4)
                best=float("inf");best_state=None;history=[]
                for epoch in range(cfg["epochs"]):
                    model.train()
                    for group in np.array_split(rng.permutation(tr),int(np.ceil(len(tr)/cfg["batch_size"]))):
                        b=batch(data[source],group);optimizer.zero_grad()
                        total,*_=loss(model(*b[:3]),*b[3:],cfg["hydration_weight"])
                        if not torch.isfinite(total): raise RuntimeError("Nonfinite training loss")
                        total.backward();torch.nn.utils.clip_grad_norm_(model.parameters(),1.0);optimizer.step()
                    val=evaluate(model,data[source],va,cfg);history.append(val)
                    if val["objective"]<best:
                        best=val["objective"];best_state={k:v.detach().clone() for k,v in model.state_dict().items()};best_epoch=epoch+1
                    if (epoch+1)%5==0:
                        print(source,kind,seed,"epoch",epoch+1,"validation",round(val["objective"],4),flush=True)
                model.load_state_dict(best_state)
                tag=f"{source}_to_{target}_{kind}_seed{seed}"
                torch.save(best_state,out/(tag+".pt"))
                heldout=evaluate(model,data[target],te,cfg)
                dynamics,generated=rollout(model,data[target],cfg,seed)
                item=dict(source=source,target=target,model=kind,seed=seed,parameters=counts[-1],
                    train_pairs=len(tr),validation_pairs=len(va),test_pairs=len(te),best_epoch=best_epoch,
                    validation=history[best_epoch-1],test=heldout,rollout=dynamics)
                results.append(item);np.savez_compressed(out/(tag+"_rollout.npz"),x=generated)
                (out/"results.json").write_text(json.dumps(results,indent=2))
                (out/(tag+"_history.json")).write_text(json.dumps(history,indent=2))
                print(tag,"NLL",round(heldout["torsion_nll_per_angle"],4),"memory RMSE",round(dynamics["contact_memory_RMSE"],4),
                      "clashes",round(dynamics["generated"]["nonlocal_clash_fraction"],3),flush=True)
            assert len(set(counts))==1,"Capacity mismatch"
    (out/"complete.json").write_text(json.dumps({"finished":time.time(),"runs":len(results)}))

if __name__=="__main__": main()

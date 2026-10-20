"""Identical-capacity invariant encoders plus a shared SE(3)-equivariant torsion decoder.

These are edge-conditioned matrix GNNs, not a reproduction of the EGNN paper.
Restriction maps act on scalar latent channels. Proper rotation/translation
equivariance follows from invariant features and internal-coordinate reconstruction.
Reflection equivariance is not claimed for signed torsion features.
"""
import math
import torch
from torch import nn

class Model(nn.Module):
    def __init__(self,kind,cfg):
        super().__init__();self.kind=kind;self.cfg=cfg
        w=cfg["width"];d=cfg["stalk_dim"];self.d=d;self.groups=w//d
        self.embed=nn.Sequential(nn.Linear(8,w),nn.SiLU(),nn.Linear(w,w))
        self.maps=nn.ModuleList([nn.Sequential(nn.Linear(2*w+5,w),nn.SiLU(),nn.Linear(w,d*d)) for _ in range(cfg["layers"])])
        self.updates=nn.ModuleList([nn.Sequential(nn.Linear(2*w,w),nn.SiLU(),nn.Linear(w,w),nn.LayerNorm(w)) for _ in self.maps])
        k=cfg["mixture_components"]
        self.torsion_head=nn.Sequential(nn.Linear(4*w,w),nn.SiLU(),nn.Linear(w,3*k))
        self.mix=nn.Linear(w,k)
        self.hydration=nn.Linear(w,1)
        self.register_buffer("feature_mean",torch.zeros(8))
        self.register_buffer("feature_scale",torch.ones(8))
        sep=(torch.arange(50)[:,None]-torch.arange(50)[None,:]).abs()
        self.register_buffer("sep",sep)
    def forward(self,x,previous,features):
        h=self.embed((features-self.feature_mean)/self.feature_scale)
        distance=torch.linalg.vector_norm(x[:,:,None]-x[:,None,:],dim=-1).clamp_min(1e-6)
        old=torch.linalg.vector_norm(previous[:,:,None]-previous[:,None,:],dim=-1)
        bond=(self.sep==1).expand(len(x),-1,-1)
        edges=torch.stack([distance,old,distance-old,bond.float(),self.sep.expand(len(x),-1,-1).float()/49],dim=-1)
        weight=torch.where(distance<.9,.5*(1+torch.cos(math.pi*distance/.9)),torch.zeros_like(distance))
        weight=torch.where(bond,torch.ones_like(weight),weight)*(self.sep>0)
        degree=weight.sum(-1,keepdim=True).clamp_min(1)
        for maps,update in zip(self.maps,self.updates):
            hi=h[:,:,None,:].expand(-1,-1,50,-1);hj=h[:,None,:,:].expand(-1,50,-1,-1)
            # Transposing endpoints reuses the exact same map for the opposite incidence.
            a=.25*torch.tanh(maps(torch.cat([hi,hj,edges],-1))).reshape(len(x),50,50,self.d,self.d)
            a=a+torch.eye(self.d,device=x.device)*.5
            b=a.transpose(1,2)
            vi=h.reshape(len(x),50,self.groups,self.d)[:,:,None]
            vj=h.reshape(len(x),50,self.groups,self.d)[:,None,:]
            av=torch.einsum("bijnm,bijgm->bijgn",a,vi.expand(-1,-1,50,-1,-1))
            bv=torch.einsum("bijnm,bijgm->bijgn",b,vj.expand(-1,50,-1,-1,-1))
            if self.kind=="sheaf":
                message=-torch.einsum("bijmn,bijgm->bijgn",a,av-bv)
            elif self.kind=="matrix_gnn":
                message=bv-av
            else: raise ValueError(self.kind)
            aggregate=(message.reshape(len(x),50,50,-1)*weight[:,:,:,None]).sum(2)/degree
            h=h+update(torch.cat([h,aggregate],-1))
        z=torch.cat([h[:,:-3],h[:,1:-2],h[:,2:-1],h[:,3:]],-1)
        raw=self.torsion_head(z).reshape(len(x),47,self.cfg["mixture_components"],3)
        mu=torch.atan2(raw[...,0],raw[...,1]+1e-5)
        kappa=.05+29.95*torch.sigmoid(raw[...,2])
        hyd=self.hydration(h).squeeze(-1)
        return mu,kappa,self.mix(h.mean(1)),hyd

def loss(output,target_phi,target_h,hydration_weight):
    mu,kappa,logits,hyd=output
    log_i0=torch.log(torch.special.i0e(kappa))+kappa
    logp=(kappa*torch.cos(target_phi[:,:,None]-mu)-math.log(2*math.pi)-log_i0).sum(1)
    nll=-torch.logsumexp(torch.log_softmax(logits,-1)+logp,-1).mean()/47
    hydration_mse=((hyd-torch.log1p(target_h))**2).mean()
    return nll+hydration_weight*hydration_mse,nll,hydration_mse

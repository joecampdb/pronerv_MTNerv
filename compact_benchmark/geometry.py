import numpy as np

def torsions(x):
    b=np.diff(x,axis=-2)
    n1=np.cross(b[...,:-2,:],b[...,1:-1,:])
    n2=np.cross(b[...,1:-1,:],b[...,2:,:])
    unit=b[...,1:-1,:]/np.linalg.norm(b[...,1:-1,:],axis=-1,keepdims=True)
    return np.arctan2(np.sum(np.cross(n1,n2)*unit,axis=-1),np.sum(n1*n2,axis=-1))

def rebuild(x,phi,center=True):
    """Retain current bond lengths/angles and first-three-atom pose."""
    y=np.empty_like(x); y[:3]=x[:3]
    b=np.diff(x,axis=0); lengths=np.linalg.norm(b,axis=1)
    cos=np.sum(-b[:-1]*b[1:],axis=1)/(lengths[:-1]*lengths[1:])
    angles=np.arccos(np.clip(cos,-1,1))
    for k in range(3,len(x)):
        e=y[k-1]-y[k-2];e/=np.linalg.norm(e)
        normal=np.cross(y[k-2]-y[k-3],e);normal/=np.linalg.norm(normal)
        side=np.cross(normal,e)
        direction=-np.cos(angles[k-2])*e+np.sin(angles[k-2])*(np.cos(phi[k-3])*side+np.sin(phi[k-3])*normal)
        y[k]=y[k-1]+lengths[k-1]*direction
    return y-y.mean(0) if center else y

def features(x,previous,hydration,previous_hydration):
    def descriptors(z):
        b=np.diff(z,axis=0); l=np.linalg.norm(b,axis=1)
        a=np.zeros(len(z)); a[1:-1]=np.sum(b[:-1]*b[1:],axis=1)/(l[:-1]*l[1:])
        phi=torsions(z); co=np.zeros(len(z));si=co.copy()
        co[1:-2]=np.cos(phi);si[1:-2]=np.sin(phi)
        return a,co,si
    a,c,s=descriptors(x);pa,pc,ps=descriptors(previous)
    return np.stack([np.log1p(hydration),np.log1p(previous_hydration),a,pa,c,s,pc,ps],axis=-1).astype("float32")

def contacts(x):
    d=np.linalg.norm(x[:,None,:]-x[None,:,:],axis=-1)
    return d[np.triu_indices(len(x),4)]<.5

def observables(x):
    y=x-x.mean(0);eig=np.linalg.eigvalsh(y.T@y/len(x))
    d=np.linalg.norm(x[:,None,:]-x[None,:,:],axis=-1)
    return dict(rg_nm=float(np.sqrt(eig.sum())),contacts_per_carbon=float(contacts(x).sum()/len(x)),
                nonlocal_clash=bool(np.any(d[np.triu_indices(len(x),3)]<.25)))

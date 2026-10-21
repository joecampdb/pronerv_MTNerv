"""Ordered, evidence-producing remediation of the manuscript limitations.

No equilibrium, physical-clock, or configuration-space theorem is inferred.
Run stages in order: provenance, chemistry, models, topology, geometry, delivery.
Large raw coordinates remain outside Git; compact results go to dist/validation.
"""
import argparse, hashlib, itertools, json, platform, tarfile, warnings
from pathlib import Path
import numpy as np
from robustness import ROOT, OUT, clean, lineage_groups, counts, normalize, height, complex_stats
DEST=ROOT/'dist/validation'; DEST.mkdir(exist_ok=True)
RAW=ROOT/'data/chignolin-full'

def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  while b:=f.read(4*1024**2):h.update(b)
 return h.hexdigest()

def write(name,data):
 (DEST/name).write_text(json.dumps(clean(data),indent=2,allow_nan=False),encoding='utf-8')

def provenance():
 m=json.loads((RAW/'manifest.json').read_text());bad=[]
 for f in m['files']:
  if sha(RAW/f['file'])!=f['sha256']:bad.append(f['file'])
 if bad:raise ValueError(bad)
 extras=[];configuration=[]
 with tarfile.open(RAW/'chignolin_trajectories.tar.gz') as tar:
  for member in tar:
   if not member.isfile() or member.name.endswith('.xtc'):continue
   extras.append(member.name)
   if member.name=='filtered/filtered.psf':(RAW/'topology.psf').write_bytes(tar.extractfile(member).read())
   elif not member.name.endswith(('.pdb','.numframes')):configuration.append(member.name)
 audit=json.loads((OUT/'full-audit.json').read_text())['systems']['chignolin']
 write('01-provenance.json',dict(files_verified=len(m['files']),runs=audit['runs'],frames=audit['frames'],archive_sha256=sha(RAW/'chignolin_trajectories.tar.gz'),archive_matches_manifest=sha(RAW/'chignolin_trajectories.tar.gz')==m['archiveSHA256'],psf_sha256=sha(RAW/'topology.psf'),configuration_members=configuration,nontrajectory_member_count=len(extras),clock_status='UNRESOLVED: XTC interval 100000 ps conflicts with depositor nominal 100 ps; no production configuration in archive.',physical_time_enabled=False,equilibrium_free_energy_enabled=False,source='https://doi.org/10.6084/m9.figshare.13858898'))
 print('1-3: verified sources; clock and equilibrium claims gated',flush=True)

def minimum_image(delta,box):
 """Orthorhombic minimum-image displacement; reject unsupported boxes."""
 box=np.asarray(box)
 if box.shape[-1]!=6 or not np.allclose(box[...,3:],90,atol=.01):raise ValueError('Non-orthorhombic/missing box requires triclinic reconstruction')
 lengths=box[...,:3]
 while lengths.ndim<delta.ndim:lengths=np.expand_dims(lengths,-2)
 return delta-lengths*np.round(delta/lengths)

def chemistry():
 import MDAnalysis as mda
 from MDAnalysis.lib.distances import calc_dihedrals
 import urllib.request
 warnings.filterwarnings('ignore',category=UserWarning,module='MDAnalysis')
 ref=RAW/'2rvd.pdb'
 if not ref.exists():urllib.request.urlretrieve('https://files.rcsb.org/download/2RVD.pdb',ref)
 u=mda.Universe(str(RAW/'topology.psf'),str(RAW/'run-0000.xtc'))
 pdb=mda.Universe(str(RAW/'topology.pdb'))
 assert np.array_equal(u.atoms.names,pdb.atoms.names)
 ca=u.select_atoms('name CA');res=ca.residues
 assert ''.join({'TYR':'Y','ASP':'D','PRO':'P','GLU':'E','THR':'T','GLY':'G','TRP':'W'}[r.resname] for r in res)=='YYDPETGTWY'
 bb=np.array([[r.atoms.select_atoms('name '+n).indices[0] for n in ['N','CA','C']] for r in res])
 refu=mda.Universe(str(ref));refca=refu.select_atoms('name CA and chainID A')
 assert list(refca.resnames)==list(ca.resnames)
 ra,rb=np.triu_indices(10,3);refds=[]
 for ts in refu.trajectory:refds.append(np.linalg.norm(refca.positions[ra]-refca.positions[rb],axis=1)*.1)
 refds=np.array(refds)
 # The reference is an ensemble, not a thresholded native-state assignment.
 bonds=u.bonds.indices;protein_bonds=bonds[(bonds<175).all(1)]
 masses=u.atoms.masses;heavy=protein_bonds[(masses[protein_bonds]>2).all(1)]
 manifest=json.loads((RAW/'manifest.json').read_text());records=[r for r in manifest['files'] if r['file'].endswith('.xtc')]
 omega=[];nmr=[];rows=[];snapshots=[];changed=0
 for k,r in enumerate(records):
  u.load_new(str(RAW/r['file']))
  xyz=np.array([u.atoms.positions.copy()*.1 for ts in u.trajectory]);boxes=np.array([ts.dimensions.copy() for ts in u.trajectory]);boxes[:,:3]*=.1
  rawbb=xyz[:,bb.reshape(-1),:]
  steps=np.diff(rawbb,axis=1);corrected=minimum_image(steps,boxes)
  changes=np.any(abs(corrected-steps)>1e-5,axis=(1,2));changed+=int(changes.sum())
  whole=np.concatenate([rawbb[:,:1],rawbb[:,:1]+np.cumsum(corrected,axis=1)],axis=1).reshape(-1,10,3,3)
  ca_xyz=whole[:,:,1]
  om=calc_dihedrals(whole[:,:-1,1].reshape(-1,3),whole[:,:-1,2].reshape(-1,3),whole[:,1:,0].reshape(-1,3),whole[:,1:,1].reshape(-1,3)).reshape(-1,9)
  omega.append(om.astype('f4'))
  dd=np.linalg.norm(ca_xyz[:,ra]-ca_xyz[:,rb],axis=2)
  nmr.append(np.sqrt(np.mean((dd[:,None,:]-refds[None,:,:])**2,axis=2)).min(1).astype('f4'))
  bd=np.linalg.norm(minimum_image(xyz[:,heavy[:,1]]-xyz[:,heavy[:,0]],boxes),axis=2)
  rows.append(dict(file=r['file'],frames=len(xyz),pbc_changed_frames=int(changes.sum()),heavy_bond_min_nm=float(bd.min()),heavy_bond_max_nm=float(bd.max()),cis_counts=(np.abs(om)<np.pi/2).sum(0).tolist(),suspect_bond_frames=int(((bd<.10)|(bd>.20)).any(1).sum())))
  if k in [0,748,1000,2500]:
   for f in np.linspace(0,len(xyz)-1,min(12,len(xyz)),dtype=int):snapshots.append(dict(run=k,frame=int(f),ca_nm=(ca_xyz[f]-ca_xyz[f].mean(0)).tolist(),omega_rad=om[f].tolist(),reference_distance_rms_nm=float(nmr[-1][f])))
  if (k+1)%500==0:print('Chemistry',k+1,flush=True)
 np.savez_compressed(OUT/'chemical-features.npz',omega=np.concatenate(omega),reference_distance_rms_nm=np.concatenate(nmr))
 write('04-chemistry.json',dict(sequence='YYDPETGTWY',atom_count=len(u.atoms),bond_count=len(u.bonds),protein_atom_count=175,excluded_ions=2,terminal_atoms={'N':list(res[0].atoms.names),'C':list(res[-1].atoms.names)},caps='PSF/PDB contain CAY/CY/OY N-terminal acetyl atoms and NT/CAT C-terminal methylamide atoms; capped simulation differs from an uncapped reference.',mass_caution='PSF stores nominal masses; deposit describes hydrogen mass repartitioning. Do not infer the integrator masses from this PSF.',reference='PDB 2RVD: 20-member NMR ensemble, CA-distance comparison only, no native threshold or folding assignment',reference_sha256=sha(ref),pbc_changed_frames=changed,heavy_bond_screen_nm=[.10,.20],screen_caution='Broad anomaly screen, not force-field energy validation; no frames silently removed.',runs=rows,reference_metric_quantiles_nm=np.quantile(np.concatenate(nmr),[0,.25,.5,.75,1]).tolist(),cis_counts=np.sum([r['cis_counts'] for r in rows],axis=0).tolist()))
 write('recorded-conformations.json',dict(scope='Recorded whole-backbone CA coordinates; no Cartesian interpolation or physical clock.',frames=snapshots))
 if changed:raise ValueError('PBC changes detected: old feature cache must be replaced before downstream inference')
 print('4: PSF mapping, all-frame bonds/PBC/omega and NMR reference complete',flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('stage',choices=['provenance','chemistry']);a=p.parse_args();globals()[a.stage]()

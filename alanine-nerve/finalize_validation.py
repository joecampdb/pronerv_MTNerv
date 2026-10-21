"""Record source/output provenance and tested dependency versions, without publishing."""
import importlib.metadata as metadata,json,platform,sys
from packaging.requirements import Requirement
from close_limitations import ROOT,DEST,write,sha

def main():
 names=['numpy','scipy','scikit-learn','scikit-image','MDAnalysis','matplotlib','threadpoolctl','requests','Pillow'];versions={};pending=list(names)
 while pending:
  name=pending.pop()
  if name.lower() in {n.lower() for n in versions}:continue
  try:
   versions[name]=metadata.version(name)
   for raw in metadata.requires(name) or []:
    r=Requirement(raw)
    if r.marker is None or r.marker.evaluate({'extra':''}):pending.append(r.name)
  except metadata.PackageNotFoundError:versions[name]='MISSING'
 write('environment.json',dict(python=platform.python_version(),implementation=platform.python_implementation(),platform=sys.platform,machine=platform.machine(),dependencies=versions,blender='4.0.0 / Cycles; OptiX used for measured stills; CPU fallback in script',node_lock='package-lock.json',scope='Tested environment inventory, not a promise of bitwise reproducibility across platforms or GPU drivers.'))
 statuses=[
  ('Dataset scale and selection','acquisition resolved; ensemble completeness not established',['01-provenance.json']),
  ('Timing conflict','unresolved provenance; physical-time export disabled',['01-provenance.json']),
  ('Adaptive sampling and comparability','root-balanced descriptive estimand and cohort sensitivity; equilibrium weights not established',['initial-cohorts.json','chignolin-pooled-height.json','chignolin-atlas.json']),
  ('Chemical identity and cartoons','full-frame mapping, bond/PBC/omega screens and NMR reference; no folding assignment',['04-chemistry.json','04-alanine-chemistry.json']),
  ('Projection and state definitions','nested grouped multifeature/multitarget prediction; no selected sufficient interface',['05-predictive-validation.json','05-predictive-validation-initial-cohorts.json']),
  ('Categorical claims','periodic metric, full maximal simplices, closure tests; no configuration-space theorem',['alanine-atlas.json','chignolin-atlas.json','06-topology-height-sensitivity.json']),
  ('Statistical and dynamical validation','train-only partition diagnostics, conditional cohort resampling, synthetic coverage and empirical path semantics; kinetics unvalidated',['07-kinetic-validation-initial-cohorts.json','07-synthetic-coverage.json','composition-contract.json','empirical-path-semantics.json']),
  ('Deformation and geometry','legacy skins screened and isolated; measured playback uses exact recorded frames; no physical smooth field',['08-geometry.json','alanine-recorded.json','chignolin-recorded.json']),
  ('Rendering and software constraints','dependency pins, numerical invariants, Chrome/Edge and mobile checks; no universal hardware guarantee',['09-browser-checks.json','environment.json']),
  ('Publication and reproducibility scope','local coherent source/data/figure revision; open limitations compiled; public release/PDF unchanged',[])
 ]
 write('limitation-register.json',dict(author='Joseph Campagna, PSM',date='2026-10-21',overall='All original categories addressed to the extent of available evidence; NOT all scientific limitations resolved.',categories=[dict(order=i+1,limitation=n,status=s,evidence=e) for i,(n,s,e) in enumerate(statuses)]))
 sources=list(ROOT.glob('*.py'))+list((ROOT/'tests').glob('*.py'))+list((ROOT/'paper').glob('*.tex'))+[ROOT/'paper/render_measured_blender.py',ROOT/'paper/camera_fit.py',ROOT/'paper/refit_measured.py',ROOT/'dist/measured.html',ROOT/'dist/measured.js',ROOT/'package-lock.json',ROOT/'requirements-validation.lock.txt',ROOT/'test-measured.mjs',ROOT/'VALIDATION.md']
 files=[p for p in DEST.glob('*.json') if p.name!='artifact-manifest.json']+list(DEST.glob('*.npz'))+list((ROOT/'paper/figures').glob('*measured*.png'))+[ROOT/'paper/figures/prediction-kinetics-revision.png']
 write('artifact-manifest.json',dict(source_sha256={str(p.relative_to(ROOT)).replace('\\','/'):sha(p) for p in sources if p.exists()},output_sha256={str(p.relative_to(ROOT)).replace('\\','/'):sha(p) for p in files},note='Raw MD hashes are in the acquisition manifest; generation uses recorded data. No secrets, local usernames or absolute environment paths are exported.'))
 print('Wrote environment, ordered limitation register and artifact hashes.')

if __name__=='__main__':main()

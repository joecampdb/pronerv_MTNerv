"""Launch the local serial screening queue detached, with persistent logs/PID."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import hashlib

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('root',type=Path)
p.add_argument('--gmx',required=True)
p.add_argument('--threads',type=int,default=8)
a=p.parse_args(); root=a.root.resolve()
if not (root/'manifest.json').exists(): p.error('Build the run tree first')
gmx=shutil.which(a.gmx)
if not gmx: p.error('GROMACS executable not found')
pidfile=root/'queue.pid'
if pidfile.exists():
    try:
        os.kill(int(pidfile.read_text()),0)
    except ProcessLookupError:
        pass
    else:
        p.error('Recorded queue PID is still active; inspect it before launching another queue')
snapshot=root/'workflow_code'; snapshot.mkdir(exist_ok=True)
hashes={}
for name in ['pilot.py','run_screen.py','analyze.py']:
    source=Path(__file__).with_name(name); target=snapshot/name
    if target.exists() and target.read_bytes()!=source.read_bytes():
        p.error('Workflow code differs from existing snapshot; use a fresh run tree')
    if not target.exists(): shutil.copy2(source,target)
    hashes[name]=hashlib.sha256(target.read_bytes()).hexdigest()
(snapshot/'sha256.json').write_text(json.dumps(hashes,indent=2))
command=[sys.executable,str(snapshot/'run_screen.py'),str(root),
         '--gmx',str(Path(gmx).resolve()),'--threads',str(a.threads)]
with (root/'queue.log').open('a') as log:
    proc=subprocess.Popen(command,stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,
                          start_new_session=True,cwd=Path(__file__).resolve().parent)
pidfile.write_text(str(proc.pid)+'\n')
print(json.dumps(dict(pid=proc.pid,log=str(root/'queue.log'),command=command),indent=2))

"""Launch the local serial screening queue detached, with persistent logs/PID."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

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
command=[sys.executable,str(Path(__file__).with_name('run_screen.py')),str(root),
         '--gmx',str(Path(gmx).resolve()),'--threads',str(a.threads)]
with (root/'queue.log').open('a') as log:
    proc=subprocess.Popen(command,stdin=subprocess.DEVNULL,stdout=log,stderr=subprocess.STDOUT,
                          start_new_session=True,cwd=Path(__file__).resolve().parent)
pidfile.write_text(str(proc.pid)+'\n')
print(json.dumps(dict(pid=proc.pid,log=str(root/'queue.log'),command=command),indent=2))

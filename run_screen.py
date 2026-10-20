"""Serial local queue: one GPU simulation at a time, checkpoint-safe.

Touch STOP in the output directory to stop between replicas. For an active
mdrun send SIGTERM to that mdrun PID; GROMACS writes a checkpoint. Do not kill -9.
"""
import argparse
import json
from pathlib import Path
import subprocess
import shutil
import sys
import time

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('root',type=Path)
p.add_argument('--gmx',default='gmx')
p.add_argument('--threads',type=int,default=8)
p.add_argument('--maxh',type=float,default=12,help='Per-stage wall-time checkpoint limit')
p.add_argument('--once',action='store_true',help='One pass; do not repeat checkpointed stages')
a=p.parse_args(); root=a.root.resolve()
manifest=json.loads((root/'manifest.json').read_text())
# Shorter PE25 systems first, so control diagnostics arrive early.
entries=sorted(manifest['replicates'],key=lambda x:(x['system'],x['replicate']))
for entry in entries:
    folder=root/entry['relative_path']
    while not (folder/'prod.done.json').exists():
        if (root/'STOP').exists(): sys.exit('STOP file found; queue stopped')
        if shutil.disk_usage(root).free < 60*1024**3:
            sys.exit('Less than 60 GiB free: queue stopped before the next MD invocation')
        status=dict(replica=entry['relative_path'],updated=time.time(),state='running')
        (root/'queue_status.json').write_text(json.dumps(status,indent=2))
        cmd=[sys.executable,str(Path(__file__).with_name('pilot.py')),'run',str(folder),
             '--gmx',a.gmx,'--threads',str(a.threads),'--maxh',str(a.maxh)]
        result=subprocess.run(cmd)
        if result.returncode:
            status['state']='failed'; status['returncode']=result.returncode
            (root/'queue_status.json').write_text(json.dumps(status,indent=2))
            sys.exit(result.returncode)
        if a.once: break
(root/'queue_status.json').write_text(json.dumps(dict(state='pass_finished',updated=time.time()),indent=2))

"""Solvate and preprocess all replicas without executing minimization or MD."""
import argparse
import json
from pathlib import Path
from pilot import run

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('root',type=Path); p.add_argument('--gmx',default='gmx')
a=p.parse_args(); root=a.root.resolve()
manifest=json.loads((root/'manifest.json').read_text())
for entry in manifest['replicates']:
    print('Preflight:',entry['relative_path'],flush=True)
    run(argparse.Namespace(replica=str(root/entry['relative_path']),gmx=a.gmx,
                           threads=1,maxh=None,until='prepare'))
print('All replicas solvated and parameter-complete.',flush=True)

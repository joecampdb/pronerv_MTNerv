"""Print compact progress without loading trajectories or requiring GROMACS."""
import argparse
import json
import re
from pathlib import Path

p=argparse.ArgumentParser(description=__doc__); p.add_argument('root',type=Path)
a=p.parse_args(); root=a.root.resolve()
manifest=json.loads((root/'manifest.json').read_text())
print('SMOKE ONLY' if manifest['smoke'] else 'SCIENTIFIC SCREEN: 2000 ns target production')
print(f'{"Replica":18} {"Stage":10} {"Stage ns":>10} {"ns/day":>10}')
for entry in manifest['replicates']:
    folder=root/entry['relative_path']; stage='not started'; ns=0.; speed='-'
    for s in ['em','nvt','npt','relax','prod']:
        log=folder/f'{s}.log'
        if log.exists():
            stage=s; text=log.read_text(errors='replace')
            pairs=re.findall(r'Step\s+Time\s*\n\s*(\d+)\s+([\d.Ee+-]+)',text)
            if pairs and s!='em': ns=float(pairs[-1][1])/1000
            matches=re.findall(r'Performance:\s+([\d.]+)',text)
            if matches: speed=matches[-1]
    if (folder/'prod.done.json').exists(): stage='complete'
    print(f'{entry["relative_path"]:18} {stage:10} {ns:10.3f} {speed:>10}')

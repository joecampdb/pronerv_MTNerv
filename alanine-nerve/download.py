import urllib.request, concurrent.futures
from pathlib import Path
base='https://ftp.imp.fu-berlin.de/pub/cmb-data/'
files=['alanine-dipeptide-3x250ns-heavy-atom-positions.npz','alanine-dipeptide-3x250ns-backbone-dihedrals.npz','alanine-dipeptide-nowater.pdb']
def get(f):
 p=Path(__file__).parent / 'data' / f
 p.parent.mkdir(exist_ok=True)
 urllib.request.urlretrieve(base+f,p)
 print(f,p.stat().st_size,flush=True)
with concurrent.futures.ThreadPoolExecutor() as e: list(e.map(get,files))


"""Download, checksum and safely unpack the complete published CLN025 archive."""
import hashlib
import json
from pathlib import Path
import tarfile
import urllib.request
import concurrent.futures
import shutil

ROOT = Path(__file__).resolve().parent
DEST = ROOT / 'data/chignolin-full'

def main():
    DEST.mkdir(parents=True, exist_ok=True)
    metadata = json.load(urllib.request.urlopen('https://api.figshare.com/v2/articles/13858898', timeout=60))
    record = next(f for f in metadata['files'] if f['id'] == 26424614)
    archive = DEST / record['name']
    if not archive.exists():
        partial = archive.with_suffix('.part')
        offset = partial.stat().st_size if partial.exists() else 0
        ranges = [(start,min(start+16*1024**2,record['size'])-1)
                  for start in range(offset,record['size'],16*1024**2)]
        def fetch(bounds):
            start,end=bounds; target=DEST/f'segment-{start}.part'
            if target.exists() and target.stat().st_size==end-start+1:return target
            request=urllib.request.Request(record['download_url']+f'?segment={start}',
                                           headers={'Range':f'bytes={start}-{end}'})
            with urllib.request.urlopen(request,timeout=120) as src,target.open('wb') as dst:
                if src.status!=206 or src.headers.get('Content-Range')!=f'bytes {start}-{end}/{record["size"]}':
                    raise ValueError('Server did not honor the exact requested range')
                shutil.copyfileobj(src,dst,1024**2)
            if target.stat().st_size!=end-start+1:raise ValueError('Incomplete range')
            print(f'Fetched range ending at {end/1024**2:.0f} MiB',flush=True)
            return target
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            parts=list(pool.map(fetch,ranges))
        with partial.open('ab') as dst:
            for part in parts:
                with part.open('rb') as src:shutil.copyfileobj(src,dst,1024**2)
        partial.replace(archive)
    md5, sha = hashlib.md5(), hashlib.sha256()
    with archive.open('rb') as stream:
        while chunk := stream.read(4 * 1024**2):
            md5.update(chunk); sha.update(chunk)
    if archive.stat().st_size != record['size'] or md5.hexdigest() != record['computed_md5']:
        raise ValueError('Archive integrity failed; no extraction performed')
    files = []; count = 0
    with tarfile.open(archive, 'r:gz') as tar:
        for member in tar:
            name = Path(member.name).name
            if not member.isfile() or name.startswith('.'):
                continue
            if name != 'filtered.pdb' and not name.endswith('.xtc'):
                continue
            local = 'topology.pdb' if name == 'filtered.pdb' else f'run-{count:04d}.xtc'
            payload = tar.extractfile(member).read()
            (DEST / local).write_bytes(payload)
            files.append(dict(file=local, member=member.name, bytes=len(payload), sha256=hashlib.sha256(payload).hexdigest()))
            if name.endswith('.xtc'): count += 1
    manifest = dict(article=metadata, archiveMD5=md5.hexdigest(), archiveSHA256=sha.hexdigest(),
                    fullArchiveVerified=True, runs=count, files=files,
                    caution='Complete deposit, not an equilibrium ensemble; adaptive lineage independence is unverified.')
    (DEST / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'Verified complete archive; extracted {count} trajectories.', flush=True)

if __name__ == '__main__': main()

"""Download selected mdCATH domains (CC BY 4.0; Mirarchi, Giorgino, De Fabritiis 2024).

Files come from https://huggingface.co/datasets/compsciencelab/mdCATH (data/mdcath_dataset_<id>.h5).
Each H5 holds one domain: pdbProteinAtoms plus coords/forces/dssp/box per temperature
(320,348,379,413,450 K) and replica (0-4); 1 ns between saved frames; Angstrom units.
SHA-256 of every file is recorded in data/mdcath/manifest.json.
"""
import hashlib, json, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEST = ROOT / "data/mdcath"
BASE = "https://huggingface.co/datasets/compsciencelab/mdCATH/resolve/main/data/"


def main(ids):
    DEST.mkdir(parents=True, exist_ok=True)
    mpath = DEST / "manifest.json"
    manifest = json.loads(mpath.read_text()) if mpath.exists() else {}
    for did in ids:
        fn = f"mdcath_dataset_{did}.h5"; local = DEST / fn
        if did in manifest and local.exists() and local.stat().st_size == manifest[did]["bytes"]:
            print("have", did, flush=True); continue
        t0 = time.time(); url = BASE + fn
        for attempt in range(3):
            try:
                urllib.request.urlretrieve(url, local); break
            except Exception as e:
                print("retry", did, e, flush=True); time.sleep(10)
        h = hashlib.sha256()
        with open(local, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 24), b""): h.update(chunk)
        manifest[did] = dict(url=url, file=fn, bytes=local.stat().st_size, sha256=h.hexdigest(),
                             downloaded=time.strftime("%Y-%m-%dT%H:%M:%S"), seconds=round(time.time()-t0, 1),
                             license="CC BY 4.0", source="compsciencelab/mdCATH (Hugging Face)")
        mpath.write_text(json.dumps(manifest, indent=2))
        print("got", did, local.stat().st_size, "bytes in", round(time.time()-t0), "s", flush=True)


if __name__ == "__main__":
    ids = sys.argv[1:] or json.loads((ROOT / "catalog/mdcath_selection.json").read_text())["domains"]
    main(ids)

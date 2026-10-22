"""Download selected MD17 / MD22 ab initio MD trajectories (sGDML, quantum-machine.org).

Each npz contains R (frames, atoms, 3) in Angstrom, z atomic numbers, E, F.
MD17: DFT (PBE+vdW-TS) MD at 500 K, 0.5 fs steps (Chmiela et al. 2017).
MD22: DFT MD at 400-500 K (Chmiela et al. 2023). Files are recorded with SHA-256.
Usage: python acquire_sgdml.py [names...]   (default: the catalog list below)
"""
import hashlib, json, sys, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEST = ROOT / "data/sgdml"
BASE = "https://www.quantum-machine.org/gdml/data/npz/"
FILES = {
    # MD22 (Chmiela et al., Sci. Adv. 2023)
    "md22_Ac-Ala3-NHMe": "md22_Ac-Ala3-NHMe.npz",
    "md22_DHA": "md22_DHA.npz",
    "md22_stachyose": "md22_stachyose.npz",
    "md22_AT-AT": "md22_AT-AT.npz",
    "md22_AT-AT-CG-CG": "md22_AT-AT-CG-CG.npz",
    # MD17 (Chmiela et al., Sci. Adv. 2017)
    "md17_ethanol": "md17_ethanol.npz",
    "md17_malonaldehyde": "md17_malonaldehyde.npz",
    "md17_aspirin": "md17_aspirin.npz",
    "md17_uracil": "md17_uracil.npz",
    "md17_salicylic": "md17_salicylic.npz",
    "md17_toluene": "md17_toluene.npz",
    "md17_naphthalene": "md17_naphthalene.npz",
    "md17_paracetamol": "paracetamol_dft.npz",
    "md17_azobenzene": "azobenzene_dft.npz",
}


def main(names):
    DEST.mkdir(parents=True, exist_ok=True)
    manifest_path = DEST / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    for name in names:
        fn = FILES[name]; url = BASE + fn; local = DEST / fn
        if name in manifest and local.exists() and local.stat().st_size == manifest[name]["bytes"]:
            print("have", name, flush=True); continue
        t0 = time.time()
        # Pre-existing copy from the MD22 speed test is reused if present.
        alt = ROOT / "data/md22" / fn
        if alt.exists() and not local.exists():
            alt.replace(local)
        else:
            urllib.request.urlretrieve(url, local)
        payload = local.read_bytes()
        manifest[name] = dict(url=url, file=fn, bytes=len(payload),
                              sha256=hashlib.sha256(payload).hexdigest(),
                              downloaded=time.strftime("%Y-%m-%dT%H:%M:%S"),
                              seconds=round(time.time() - t0, 1))
        manifest_path.write_text(json.dumps(manifest, indent=2))
        print("got", name, len(payload), "bytes", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:] or list(FILES))

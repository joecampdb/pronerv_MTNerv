"""Download a deterministic, bounded subset of the CC BY 4.0 CLN025 archive.

Stream the first 128 non-hidden XTC members in archive order. Never concatenate
independent runs. Individual SHA-256 checksums and archive member names are saved.
"""
import hashlib
import json
from pathlib import Path
import tarfile
import urllib.request

ROOT = Path(__file__).resolve().parent
DEST = ROOT / "data/chignolin"
URL = "https://ndownloader.figshare.com/files/26424614"
COUNT = 128


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    records = []
    with urllib.request.urlopen(URL, timeout=120) as response:
        with tarfile.open(fileobj=response, mode="r|gz") as archive:
            count = 0
            for member in archive:
                name = Path(member.name).name
                if not member.isfile() or name.startswith("."):
                    continue
                if name != "filtered.pdb" and not name.endswith(".xtc"):
                    continue
                payload = archive.extractfile(member).read()
                local = "topology.pdb" if name == "filtered.pdb" else f"run-{count:03d}.xtc"
                (DEST / local).write_bytes(payload)
                records.append(dict(member=member.name, file=local, bytes=len(payload),
                                    sha256=hashlib.sha256(payload).hexdigest()))
                if name.endswith(".xtc"):
                    count += 1
                    if count % 32 == 0:
                        print(f"Downloaded {count}/{COUNT} trajectories", flush=True)
                    if count == COUNT:
                        break
    assert count == COUNT and (DEST / "topology.pdb").exists()
    manifest = dict(source=URL, doi="10.6084/m9.figshare.13858898",
                    authors=["Adrià Pérez Culubret", "Gianni De Fabritiis"],
                    license="CC BY 4.0", variant="CLN025",
                    sequence="YYDPETGTWY", temperatureK=350,
                    selection="First 128 non-hidden XTC members in archive order",
                    fullArchiveMD5="b1007669e66c97621d22041846e43139",
                    fullArchiveVerified=False, files=records)
    (DEST / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("Saved subset and per-file checksums; full archive was not downloaded.")


if __name__ == "__main__":
    main()

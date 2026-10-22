"""Build every catalog system that has data, in parallel processes. Skips systems with a finished summary.json
unless --force. Usage: python build_all.py [--workers 4] [--only family|group] [--force] [ids...]"""
import argparse
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist/systems"


def run_one(sid):
    out = DIST / sid
    out.mkdir(parents=True, exist_ok=True)
    log = out / "build.log"
    t0 = time.time()
    with open(log, "w") as f:
        env = {**os.environ, "OMP_NUM_THREADS": "4", "MKL_NUM_THREADS": "4", "OPENBLAS_NUM_THREADS": "4"}
        r = subprocess.run([sys.executable, str(ROOT / "build_system.py"), sid], stdout=f, stderr=subprocess.STDOUT, cwd=ROOT, env=env)
    return sid, r.returncode, round(time.time() - t0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--only", default=None, help="family or group filter")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    subprocess.run([sys.executable, "-m", "fluidnerve.catalog"], cwd=ROOT, check=True)
    catalog = json.loads((ROOT / "catalog/systems.json").read_text())["systems"]
    todo = []
    for s in catalog:
        if args.ids and s["id"] not in args.ids:
            continue
        if args.only and args.only not in (s.get("family"), s["group"]):
            continue
        done = (DIST / s["id"] / "summary.json").exists()
        lock = DIST / s["id"] / "build.log"
        building = lock.exists() and not done and (time.time() - lock.stat().st_mtime) < 1800 and not args.force
        if (done and not args.force) or building:
            continue
        todo.append(s["id"])
    print(len(todo), "systems to build", flush=True)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        for sid, rc, secs in ex.map(run_one, todo):
            print(sid, "ok" if rc == 0 else f"FAILED rc={rc}", f"{secs}s", flush=True)


if __name__ == "__main__":
    main()

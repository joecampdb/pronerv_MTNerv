"""Export every built nerve as homotopy.io material.

For each dist/systems/<id>/nerve.json this writes, under dist/homotopy/<id>/ :
  base.ops.json / base.hom     oriental encoding of the witnessed cover complex (<= 18 vertices; 3-cells = tetrahedra)
  poset.ops.json / poset.hom   oriental encoding of the order complex of the face poset (faces of dim <= 3)
  README.md                    sizes, semantics and a click script for manual construction
The .hom files are produced by vendor/homotopy-rs/target/release/nerve_hom (see docs/homotopy-io-instructions.md).
Usage: python export_homotopy.py [ids...] [--max-generators 4000]
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fluidnerve.homotopy_export import oriental_ops, complex_from_nerve, click_script, write_ops  # noqa: E402

ROOT = Path(__file__).resolve().parent
NERVE_HOM = ROOT / "vendor/homotopy-rs/target/release/nerve_hom.exe"
OUT = ROOT / "dist/homotopy"


def export_system(sid, max_generators=4000):
    nerve = json.loads((ROOT / "dist/systems" / sid / "nerve.json").read_text())
    summary = json.loads((ROOT / "dist/systems" / sid / "summary.json").read_text())
    out = OUT / sid
    out.mkdir(parents=True, exist_ok=True)
    report = dict(id=sid, label=summary["label"], encodings={})
    md = [f"# homotopy.io export: {summary['label']} (`{sid}`)", "",
          "Two oriental encodings of the same witnessed cover (see docs/homotopy-io-instructions.md).",
          "Import a `.hom` file through the project panel (top-left button) in https://beta.homotopy.io.", ""]
    for kind in ("base", "poset"):
        V, E, T, Q, labels = complex_from_nerve(nerve, kind)
        n_gen = len(V) + len(E) + len(T) + len(Q)
        title = f"{summary['label']} — {'witnessed cover complex' if kind == 'base' else 'face-poset order complex'}"
        abstr = ("Oriental encoding: 0-cells are cover sets, 1-cells pairwise overlaps (i<j), 2-cells triple overlaps, "
                 "3-cells quadruple overlaps." if kind == "base" else
                 "Oriental encoding of the order complex of the face poset: 0-cells are faces, 1-cells strict inclusions, "
                 "2-cells composable pairs, 3-cells length-three chains.")
        rec = dict(vertices=len(V), edges=len(E), triangles=len(T), tetrahedra=len(Q), generators=n_gen)
        if n_gen > max_generators:
            rec["status"] = f"skipped: {n_gen} generators exceed --max-generators {max_generators}"
            md.append(f"## {kind}: {rec['status']}")
        else:
            ops, _ = oriental_ops(V, E, T, Q, labels, title=title, author="pronerv fluid-nerve pipeline", abstr=abstr)
            write_ops(out / f"{kind}.ops.json", ops)
            hom = out / f"{kind}.hom"
            r = subprocess.run([str(NERVE_HOM), str(out / f"{kind}.ops.json"), str(hom)], capture_output=True, text=True)
            rec["status"] = "ok" if r.returncode == 0 else f"nerve_hom failed: {r.stderr[-500:]}"
            rec["nerve_hom_output"] = r.stdout.strip()[-300:]
            md.append(f"## {kind}: {rec['status']}")
            md.append("")
            md.append(click_script(V, E, T, Q, labels))
        md.append("")
        report["encodings"][kind] = rec
    (out / "README.md").write_text("\n".join(md), encoding="utf-8")
    (out / "export.json").write_text(json.dumps(report, indent=1))
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--max-generators", type=int, default=4000)
    args = ap.parse_args()
    ids = args.ids or sorted(p.name for p in (ROOT / "dist/systems").iterdir() if (p / "nerve.json").exists())
    index = {}
    for sid in ids:
        rep = export_system(sid, args.max_generators)
        index[sid] = rep["encodings"]
        print(sid, {k: (v["generators"], v["status"][:40]) for k, v in rep["encodings"].items()}, flush=True)
    (OUT / "index.json").write_text(json.dumps(index, indent=1))


if __name__ == "__main__":
    main()

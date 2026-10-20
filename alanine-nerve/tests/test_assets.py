"""Offline checks of the shipped scientific and rendering contract."""
import itertools
import json
from pathlib import Path
import unittest
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def read(p):
    return json.loads(p.read_text(encoding="utf-8"))


class AtlasAssets(unittest.TestCase):
    def test_overlap_categories(self):
        for folder in [ROOT/"dist", ROOT/"dist/chignolin"]:
            d = read(folder/"data.json")
            s = [set(n["simplex"]) for n in d["nodes"]]
            expected = {(i,j) for i,a in enumerate(s) for j,b in enumerate(s) if a < b}
            self.assertEqual(expected, set(map(tuple,d["edges"])))
            chains = {(i,j,k) for i,j in expected for k in range(len(s)) if (j,k) in expected}
            self.assertEqual(chains, set(map(tuple,d["chains"])))
            self.assertTrue(all((i,k) in expected for i,j,k in chains))

    def test_chignolin_composition_and_source_bounds(self):
        d = read(ROOT/"dist/chignolin/data.json")
        routes = d["routes"]
        expected = {(a["id"],b["id"]) for a in routes for b in routes if a["target"]==b["source"]}
        self.assertEqual(expected, set(map(tuple,d["pairs"])))
        self.assertEqual(sum(r["count"] for r in routes), d["totalPassages"])
        self.assertEqual(sum(t["frames"] for t in d["rawTiming"]), d["frames"])
        for r in routes:
            self.assertLess(r["startFrame"],r["endFrame"])
            self.assertLess(r["endFrame"],d["rawTiming"][r["run"]]["frames"])
            self.assertEqual(len(r["moleculeFrames"]),len(r["worldFrames"]))
            self.assertEqual(np.array(r["moleculeFrames"]).shape[1:],(10,3))
        for c in d["cartoons"]:
            self.assertLess(c["localFrame"],d["rawTiming"][c["run"]]["frames"])

    def test_meshes_and_morph_targets(self):
        for folder in [ROOT/"dist",ROOT/"dist/chignolin"]:
            base=np.fromfile(folder/"surface.bin",dtype="<f4").reshape(-1,7)
            faces=np.fromfile(folder/"triangles.bin",dtype="<u4")
            self.assertTrue(np.isfinite(base).all())
            self.assertLess(faces.max(),len(base))
            for m in read(folder/"skins/index.json"):
                i=m["id"]
                v=np.fromfile(folder/f"skins/{i}.bin",dtype="<f4").reshape(-1,7)
                f=np.fromfile(folder/f"skins/{i}-indices.bin",dtype="<u4")
                targets=np.fromfile(folder/f"skins/{i}-morph.bin",dtype="<f4").reshape(m["morphFrames"],-1,6)
                self.assertEqual(len(v),m["vertices"])
                self.assertLess(f.max(),len(v))
                self.assertTrue(np.isfinite(targets).all())
                delta=np.linalg.norm(targets[:,:,:3]-v[None,:,:3],axis=2)
                self.assertLessEqual(delta.max(),1.50001)
                self.assertGreater(np.ptp(targets[:,:,:3],axis=0).max(),1e-4)
                end=(v[:,6]==0)|(v[:,6]==1)
                self.assertTrue(np.all(delta[:,end]<3e-6))

    def test_sources_and_distribution_files(self):
        m=read(ROOT/"dist/chignolin/provenance.json")
        self.assertEqual(len(m["files"]),129)
        self.assertEqual(len({r["member"] for r in m["files"]}),129)
        for f in m["files"]:
            self.assertEqual(len(f["sha256"]),64)
        for p in ["dist/index.html","dist/chignolin.html","dist/atlas.css","dist/paper.pdf"]:
            self.assertTrue((ROOT/p).is_file(),p)
        self.assertTrue((ROOT/"dist/paper.pdf").read_bytes().startswith(b"%PDF"))


if __name__ == "__main__":
    unittest.main()

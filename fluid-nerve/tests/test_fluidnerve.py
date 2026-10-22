"""Offline consistency tests for fluidnerve on synthetic data (no trajectories or network needed).
Run: python -m unittest discover -s tests -v   (from fluid-nerve/)"""
import sys
import unittest
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from fluidnerve import geometry as G, nerve as N, field as F, filtration as FL  # noqa: E402
from fluidnerve.homotopy_export import oriental_ops, complex_from_nerve  # noqa: E402


class GeometryTests(unittest.TestCase):
    def test_kabsch_recovers_rotation(self):
        rng = np.random.default_rng(0)
        P = rng.normal(size=(5, 12, 3))
        P -= P.mean(1, keepdims=True)
        q = rng.normal(size=4)
        q /= np.linalg.norm(q)
        a, b, c, d = q
        R = np.array([[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)],
                      [2*(b*c+a*d), a*a-b*b+c*c-d*d, 2*(c*d-a*b)],
                      [2*(b*d-a*c), 2*(c*d+a*b), a*a-b*b-c*c+d*d]])
        Q = P @ R
        aligned = G.align_pairs(Q, P)
        self.assertLess(np.abs(aligned - Q).max(), 1e-9)

    def test_dihedral_known_values(self):
        p0 = np.array([[1., 0, 0]]); p1 = np.array([[0., 0, 0]]); p2 = np.array([[0., 0, 1]]); p3 = np.array([[0., 1, 1]])
        self.assertAlmostEqual(abs(G.dihedral(p0, p1, p2, p3)[0]), 90.0, places=9)

    def test_pca_chart_explains_planar_data(self):
        rng = np.random.default_rng(1)
        t = rng.uniform(0, 2*np.pi, 2000)
        X = np.stack([np.cos(t), np.sin(t), 0.01*rng.normal(size=2000)], 1)[:, None, :]
        X = np.concatenate([X, -X], 1)
        qs, info = G.pca_chart([X])
        self.assertGreater(sum(info["explained"]), 0.99)


class NerveTests(unittest.TestCase):
    def circle_points(self, n=4000):
        rng = np.random.default_rng(2)
        t = rng.uniform(0, 2*np.pi, n)
        r = 1 + 0.05*rng.normal(size=n)
        return np.stack([r*np.cos(t), r*np.sin(t)], 1)

    def test_circle_cover_has_one_loop(self):
        q = self.circle_points()
        limits = N.chart_limits(q)
        nerve, M, bits = N.build_nerve(q, limits, None, bins=30, n_centers=12, radius=0.7)
        self.assertEqual(nerve["betti_0_1_2"][0], 1)
        self.assertEqual(nerve["betti_0_1_2"][1], 1)
        self.assertEqual(nerve["betti_0_1_2"][2], 0)
        # every inclusion is strict and every chain composes
        sets = [set(n["simplex"]) for n in nerve["nodes"]]
        self.assertTrue(all(sets[i] < sets[j] for i, j in nerve["edges"]))
        self.assertTrue(all(sets[i] < sets[j] < sets[k] for i, j, k in nerve["chains"]))

    def test_gf2_rank_and_betti_of_tetrahedron_boundary(self):
        faces = N.faces_from_maximal([0b0111, 0b1011, 0b1101, 0b1110], 3)  # hollow tetrahedron
        betti, counts = N.betti_numbers(faces, 2)
        self.assertEqual(betti, [1, 0, 1])
        self.assertEqual(counts, {0: 4, 1: 6, 2: 4})

    def test_maximal_masks(self):
        self.assertEqual(N.maximal_masks([0b1, 0b11, 0b110, 0b10]), [0b11, 0b110])


class FieldTests(unittest.TestCase):
    def test_drift_of_linear_flow(self):
        # chart points advance by (0.1, 0) per frame; distances constant -> h = 0, v = (0.1 tau, 0)
        n = 3000
        q = np.stack([np.linspace(0, 10, n), np.zeros(n)], 1)
        d = np.ones((n, 3))
        x = np.zeros((n, 4, 3)); x[:, :, 0] = np.arange(4)
        fld = F.field_at_lag([q], [d], [x], 5, [[-.5, -1], [10.5, 1]], 10, None, 50, bootstrap=10)
        sup = fld["support"]
        self.assertTrue(sup.any())
        self.assertLess(np.nanmax(fld["h"][sup]), 1e-9)
        self.assertLess(np.abs(fld["v"][sup][:, 0] - 5*10/(n-1)).max(), 1e-9)
        self.assertLess(np.abs(fld["v"][sup][:, 1]).max(), 1e-12)

    def test_periodic_wrap(self):
        self.assertAlmostEqual(G.wrap_delta(np.array([350.])[0], 360), -10.0)


class FiltrationTests(unittest.TestCase):
    def test_fluid_filtration_is_monotone_and_connects(self):
        # two disjoint clusters visited alternately along one run
        M = np.zeros((200, 2), bool)
        M[:100, 0] = True; M[100:, 1] = True
        res = FL.fluid_filtration([M], [1, 5, 50])
        b0 = [r["betti"][0] for r in res["rows"]]
        self.assertEqual(b0[0], 2)
        self.assertEqual(b0[1], 1)   # at tau=1 the frames at the boundary witness both
        self.assertTrue(all(a >= b for a, b in zip(b0, b0[1:])))
        self.assertEqual(res["first_connected_tau"], 1)
        pairs0 = res["pairs"]["0"]
        self.assertEqual(sum(1 for b, d in pairs0 if d is None), 1)

    def test_persistence_pairs_toy(self):
        # square boundary born at 0, filled by two triangles at index 2 -> one 1-class with (0, 2)
        birth = {(0,): 0, (1,): 0, (2,): 0, (3,): 0, (0, 1): 0, (1, 2): 0, (2, 3): 0, (0, 3): 0,
                 (0, 2): 2, (0, 1, 2): 2, (0, 2, 3): 2}
        pairs = FL.persistence_pairs(birth, 2)
        self.assertIn((0, 2), pairs[1])
        self.assertEqual(sum(1 for b, d in pairs[0] if d is None), 1)

    def test_flooding_torus_and_plane(self):
        F_plane = np.full((10, 10), 3.0); F_plane[2:8, 2:8] = 1.0; F_plane[4:6, 4:6] = 2.0  # an annulus at level 1
        res = FL.flooding_filtration(F_plane, None, n_levels=4)
        lv1 = next(r for r in res["rows"] if abs(r["level"] - 1.0) < 1e-9)
        self.assertEqual(lv1["betti"][:2], [1, 1])
        F_torus = np.zeros((6, 6))
        res = FL.flooding_filtration(F_torus, 360.0, n_levels=2)
        self.assertEqual(res["rows"][-1]["betti"], [1, 2, 1])


class HomotopyExportTests(unittest.TestCase):
    def test_oriental_ops_counts(self):
        nerve = dict(maximal_simplices=[[0, 1, 2, 3], [3, 4]])
        V, E, T, Q, L = complex_from_nerve(nerve, "base")
        self.assertEqual((len(V), len(E), len(T), len(Q)), (5, 7, 4, 1))
        ops, gens = oriental_ops(V, E, T, Q)
        self.assertEqual(len(gens), 17)
        self.assertEqual(sum(1 for o in ops if o["op"] == "zero"), 5)
        V, E, T, Q, L = complex_from_nerve(nerve, "poset")
        self.assertEqual(len(V), 17)  # 15 faces of the tetrahedron + {4} + {3,4}
        self.assertTrue(all(a < b for a, b in E))


if __name__ == "__main__":
    unittest.main()

"""Scientific invariants for the diagnostic estimators (no trajectory downloads)."""
import sys
from pathlib import Path
import unittest
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import robustness as r

class RobustnessTests(unittest.TestCase):
    def test_inferred_descendants_share_holdout_fold(self):
        t=[dict(child='a',parent=None),dict(child='b',parent='a'),dict(child='c',parent='b'),dict(child='d',parent=None)]
        roots,folds,meta=r.lineage_groups(t)
        self.assertEqual(roots[:3],['a']*3)
        self.assertEqual(len(set(folds[:3])),1)
        self.assertEqual(meta['largest_root_runs'],3)

    def test_lineage_cycle_rejected(self):
        with self.assertRaises(ValueError):
            r.lineage_groups([dict(child='a',parent='b'),dict(child='b',parent='a')])

    def test_no_cross_run_transition(self):
        c=r.counts([np.array([0,0]),np.array([1,1])],1,n=2)
        np.testing.assert_array_equal(c,np.eye(2,dtype=int))

    def test_missing_row_is_not_absorbing_state(self):
        p=r.normalize(np.array([[3,1],[0,0]]))
        self.assertTrue(np.isnan(p[1]).all())
        np.testing.assert_allclose(p[0],[.75,.25])

    def test_core_memory_resets(self):
        x=r.carry_core(np.array([1,0,1]),np.array([2.,.1,2.]),.5)
        np.testing.assert_array_equal(x,[-1,0,0])

    def test_mobility_is_rigid_motion_invariant(self):
        rng=np.random.default_rng(2);x=rng.normal(size=(30,10,3))
        rotation=np.linalg.qr(rng.normal(size=(3,3)))[0]
        np.testing.assert_allclose(r.metric_features(x),r.metric_features(x@rotation+17),atol=1e-12)
        stationary=np.repeat(x[:1],20,axis=0)
        np.testing.assert_allclose(r.mobility(r.metric_features(stationary),5),0)

    def test_tetrahedron_fills_spurious_truncation_hole(self):
        full=r.complex_stats(np.ones((1,4),bool))
        self.assertEqual(full['truncated_beta2'],1)
        self.assertEqual(full['betti_0_1_2'],[1,0,0])

    def test_disconnected_complex(self):
        result=r.complex_stats(np.eye(3,dtype=bool))
        self.assertEqual(result['betti_0_1_2'],[3,0,0])

    def test_known_markov_chain_semigroup(self):
        rng=np.random.default_rng(7);p=np.array([[.85,.15],[.3,.7]])
        runs=[]
        for _ in range(8):
            z=np.zeros(10000,dtype=int)
            for t in range(1,len(z)):z[t]=int(rng.random()>=p[z[t-1],0])
            runs.append(z)
        one=r.normalize(r.counts(runs,1,n=2));four=r.normalize(r.counts(runs,4,n=2))
        np.testing.assert_allclose(np.linalg.matrix_power(one,4),four,atol=.015)

if __name__=='__main__':unittest.main()

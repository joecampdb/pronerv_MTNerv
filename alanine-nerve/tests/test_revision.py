"""Scientific and semantic invariants of the measured revision."""
import unittest,sys,json,itertools
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from close_limitations import minimum_image,DEST
from build_validated_atlas import periodic_delta,maximal_masks,masks_to_faces
from export_recorded import align
from composition_contract import kernel,compose,independent_product
from empirical_path_semantics import compose_relation,visits
from robustness import height,initial_cohort_groups

class RevisionInvariants(unittest.TestCase):
 def test_minimum_image_reconstructs_crossing(self):
  x=np.array([[[3.9,0,0],[-3.9,0,0]]]);box=np.array([[4,4,4,90,90,90]])
  np.testing.assert_allclose(minimum_image(x,box),[[[-.1,0,0],[.1,0,0]]])
  with self.assertRaises(ValueError):minimum_image(x,[4,4,4,90,80,90])
 def test_periodic_seam_is_short(self):
  np.testing.assert_allclose(periodic_delta([179,-179],[-179,179],360),[-2,2])
 def test_maximal_simplex_keeps_high_dimensional_information(self):
  maxima=maximal_masks([0,1,3,7,15,16]);self.assertEqual(set(maxima),{15,16})
  full=masks_to_faces(maxima);self.assertIn((0,1,2,3),full)
  for face in full:
   for k in range(1,len(face)):self.assertTrue(set(itertools.combinations(face,k)).issubset(full))
 def test_rigid_alignment_keeps_distances_and_handedness(self):
  rng=np.random.default_rng(22);x=rng.normal(size=(10,3));ref=rng.normal(size=(10,3));y=align(x,ref)
  np.testing.assert_allclose(np.linalg.norm(x[:,None]-x,axis=2),np.linalg.norm(y[:,None]-y,axis=2),atol=1e-12)
  self.assertEqual(np.sign(np.linalg.det(x[1:4]-x[0])),np.sign(np.linalg.det(y[1:4]-y[0])))
 def test_stochastic_category_identity_and_associativity(self):
  rng=np.random.default_rng(9)
  def p(a,b):
   x=rng.random((a,b));return x/x.sum(1)[:,None]
  a,b,c=p(2,3),p(3,4),p(4,2)
  np.testing.assert_allclose(compose(compose(a,b),c),compose(a,compose(b,c)),atol=1e-14)
  np.testing.assert_allclose(compose(np.eye(2),a),a)
  np.testing.assert_allclose(compose(a,np.eye(3)),a)
  with self.assertRaises(ValueError):compose(a,a)
  with self.assertRaises(ValueError):kernel([[np.nan,0]])
 def test_path_semantics_cannot_splice_equal_basin_labels_across_runs(self):
  # Both intermediate occurrences have label B but are distinct observations.
  first={('run0:A','run0:B')};other={('run1:B','run1:C')}
  self.assertEqual(compose_relation(first,other),set())
  self.assertEqual(compose_relation(first,{('run0:B','run0:C')}),{('run0:A','run0:C')})
  np.testing.assert_array_equal(visits([-1,-1,0,0,1,1,0]),[2,4,6])
 def test_product_semantics_requires_joint_observation_check(self):
  p=np.array([[.9,.1],[.2,.8]]);q=np.array([[.7,.3],[.4,.6]])
  np.testing.assert_allclose(independent_product(p,q).sum(1),1)
  np.testing.assert_allclose(np.linalg.matrix_power(independent_product(p,q),3),independent_product(np.linalg.matrix_power(p,3),np.linalg.matrix_power(q,3)))
 def test_root_dominance_masks_falsely_supported_bin(self):
  # Three roots touch the bin, but essentially all evidence is from one root.
  qs=[np.zeros((n,2)) for n in [2000,20,20]]
  ds=[np.zeros((len(q),3)) for q in qs]
  h=height(qs,ds,1,1,[[-1,-1],[1,1]],100,cluster_ids=['a','b','c'])
  self.assertEqual(h['cluster_support'],[[3]])
  self.assertLess(h['effective_resampling_units'][0][0],1.1)
  self.assertFalse(h['supported'][0][0])
 def test_witness_inclusion_is_contravariant(self):
  members=[{0,1,2},{0,1},{1,2},{0}]
  for a in [{0},{1},{0,1}]:
   for b in [{0,1},{1,2},{0,1,2}]:
    if a<b:
     wa={i for i,x in enumerate(members) if a<=x};wb={i for i,x in enumerate(members) if b<=x}
     self.assertLessEqual(wb,wa)
 def test_hierarchical_resampling_keeps_root_balanced_estimand(self):
  qs=[np.zeros((100,2)) for _ in range(4)];ds=[np.repeat((np.arange(100)*i)[:,None],3,axis=1) for i in range(4)]
  h=height(qs,ds,1,1,[[-1,-1],[1,1]],25,cluster_ids=['a','b','c','d'],estimator='root-balanced',bootstrap_groups=['A','A','B','C'])
  self.assertAlmostEqual(h['height_nm'][0][0],1.5)
  self.assertAlmostEqual(h['effective_resampling_units'][0][0],16/6)
  self.assertEqual(h['resampling_unit'],'inferred initial-conformation cohort')
  with self.assertRaises(ValueError):height(qs,ds,1,1,[[-1,-1],[1,1]],25,cluster_ids=['a','a','c','d'],bootstrap_groups=['A','B','B','C'])
 def test_initial_cohorts_never_split_descendants(self):
  timing=[dict(child='e1s1',parent=None),dict(child='e1s2',parent=None),dict(child='e2s1',parent='e1s1')]
  records=[dict(member='filtered/e1s1_chignolin_50ns_0/x.xtc'),dict(member='filtered/e1s2_chignolin_50ns_0/x.xtc')]
  groups,folds,_=initial_cohort_groups(timing,records)
  self.assertEqual(groups,['0','0','0']);self.assertEqual(len(set(folds)),1)

class RevisedAssets(unittest.TestCase):
 def test_too_few_holdout_groups_cannot_give_zero_width_certainty(self):
  d=json.loads((DEST/'07-kinetic-validation-initial-cohorts.json').read_text())
  for r in d['results']:
   if r['heldout_groups']<3:
    self.assertEqual(r['conditional_interval_status'],'insufficient_groups')
    self.assertTrue(all(x is None for row in r['conditional_group_resampling_TV_interval'] for x in row))
 def test_full_cover_and_missing_height_contract(self):
  for name in ['alanine','chignolin']:
   d=json.loads((DEST/(name+'-atlas.json')).read_text());c=d['cover'];faces={tuple(n['simplex']) for n in c['nodes']}
   self.assertEqual(faces,set(masks_to_faces([sum(1<<i for i in f) for f in c['maximal_simplices']],3)))
   sets=[set(n['simplex']) for n in c['nodes']]
   self.assertEqual(set(map(tuple,c['edges'])),{(i,j) for i,a in enumerate(sets) for j,b in enumerate(sets) if a<b})
   for a,b,k in c['chains']:self.assertTrue(sets[a]<sets[b]<sets[k])
   for n in c['nodes']:
    if not n['supported']:self.assertIsNone(n['height_nm'])
   self.assertEqual(d['frames'],750000 if name=='alanine' else 1868861)
   self.assertFalse(d['energy_claim'])
 def test_recorded_geometry_is_not_interpolated(self):
  for name in ['alanine','chignolin']:
   d=json.loads((DEST/(name+'-recorded.json')).read_text())
   self.assertLess(max(a['max_pair_distance_error_nm'] for a in d['anchors']),1e-6)
   for p in d['excerpts']:
    self.assertTrue(np.isfinite([f['coords_nm'] for f in p['frames']]).all())
    np.testing.assert_array_equal(np.diff([f['frame'] for f in p['frames']]),1)
   if name=='chignolin':self.assertIsNone(d['physical_frame_interval_ps'])

if __name__=='__main__':unittest.main()

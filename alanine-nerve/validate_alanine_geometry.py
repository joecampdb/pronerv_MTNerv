"""Verify atom-order/torsion consistency over every supplied alanine frame."""
import numpy as np
from MDAnalysis.lib.distances import calc_dihedrals
from robustness import ROOT
from close_limitations import write,sha
def main():
 a=np.load(ROOT/'data/alanine-dipeptide-3x250ns-heavy-atom-positions.npz');q=np.load(ROOT/'data/alanine-dipeptide-3x250ns-backbone-dihedrals.npz')
 bonds=np.array([[0,1],[1,2],[1,3],[3,4],[4,5],[4,6],[6,7],[6,8],[8,9]])
 rows=[]
 for k,j in zip(a,q):
  x=a[k].reshape(-1,10,3);phi=calc_dihedrals(x[:,1],x[:,3],x[:,4],x[:,6]);psi=calc_dihedrals(x[:,3],x[:,4],x[:,6],x[:,8]);delta=(np.column_stack([phi,psi])-q[j]+np.pi)%(2*np.pi)-np.pi
  dist=np.linalg.norm(x[:,bonds[:,0]]-x[:,bonds[:,1]],axis=2)
  rows.append(dict(coordinate_key=k,angle_key=j,frames=len(x),max_torsion_discrepancy_rad=float(abs(delta).max()),bond_range_nm=[float(dist.min()),float(dist.max())],bond_screen_failures=int(((dist<.10)|(dist>.20)).any(1).sum())))
  if abs(delta).max()>1e-4:raise ValueError('Coordinate/angle mismatch')
 write('04-alanine-chemistry.json',dict(atom_order=['ACE:CH3','ACE:C','ACE:O','ALA:N','ALA:CA','ALA:CB','ALA:C','ALA:O','NME:N','NME:CH3'],bonds=bonds.tolist(),mapping='PDB heavy-atom order; phi=(1,3,4,6), psi=(3,4,6,8), zero-based. Capped ACE-ALA-NME.',source_sha256={str(p.name):sha(p) for p in [ROOT/'data/alanine-dipeptide-3x250ns-heavy-atom-positions.npz',ROOT/'data/alanine-dipeptide-3x250ns-backbone-dihedrals.npz',ROOT/'data/alanine-dipeptide-nowater.pdb']},runs=rows,scope='All supplied frames; bond screening and torsion identity are not force-field or experimental validation. Supplied aligned coordinates lack per-frame periodic cells; no unsupported PBC reconstruction performed.'))
 print(rows)
if __name__=='__main__':main()

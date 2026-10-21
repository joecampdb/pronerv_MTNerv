"""Inspect the shortest CA neighbor spacing using its peptide omega angle."""
import json,warnings
import numpy as np
import MDAnalysis as mda
from MDAnalysis.lib.distances import calc_dihedrals
from robustness import ROOT,OUT

def main():
    warnings.filterwarnings('ignore',category=UserWarning,module='MDAnalysis')
    p=json.loads((OUT/'full-audit.json').read_text())['systems']['chignolin']['provenance']
    bounds=np.array(p['neighbor_range_nm']);record=p['timing'][int(bounds[:,0].argmin())]
    folder=ROOT/'data/chignolin-full'
    u=mda.Universe(str(folder/'topology.pdb'),str(folder/record['file']));ca=u.select_atoms('name CA')
    xyz=np.array([ca.positions.copy()*.1 for _ in u.trajectory])
    distance=np.linalg.norm(np.diff(xyz,axis=1),axis=2)
    frame,res=np.unravel_index(distance.argmin(),distance.shape);u.trajectory[frame]
    left,right=ca.residues[res],ca.residues[res+1]
    points=[left.atoms.select_atoms('name CA').positions[0],left.atoms.select_atoms('name C').positions[0],
            right.atoms.select_atoms('name N').positions[0],right.atoms.select_atoms('name CA').positions[0]]
    omega=float(np.rad2deg(calc_dihedrals(*[np.array([p]) for p in points]))[0])
    result=dict(file=record['file'],frame=int(frame),residues=[str(left.resname)+str(left.resid),str(right.resname)+str(right.resid)],
                CA_distance_nm=float(distance.min()),omega_degrees=omega,
                runs_below_old_CA_lower_bound=int((bounds[:,0]<.3).sum()),
                interpretation='Near-zero omega at shortest CA spacing is consistent with a cis peptide; a 0.3 nm lower bound is not a universal validity criterion.')
    (OUT/'geometry-outlier.json').write_text(json.dumps(result,indent=2));print(result)

if __name__=='__main__':main()

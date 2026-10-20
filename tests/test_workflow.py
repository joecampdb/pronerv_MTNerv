import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
from pilot import molecule, topology, mdp, config, verify_ff, ROOT
from analyze import unwrap_chain, metrics, committed_labels
import pytest
import pilot


def test_budget_and_formula():
    cfg=config()
    assert sum(s['replicates']*s['production_ns'] for s in cfg['systems'].values())==2000
    for repeats in [25,50]:
        m=molecule(2*repeats)
        assert m.GetNumAtoms()==6*repeats+2
        text,names=topology(m)
        assert len(set(names))==len(names)
        assert '[ pairs ]' in text
        assert len(m.GetBonds())==m.GetNumAtoms()-1


def test_mdp_production_has_no_velocity_reset_or_barostat():
    text=mdp('prod',123,200)
    assert 'nsteps = 100000000' in text
    assert 'gen-vel = no' in text
    assert 'pcoupl = no' in text
    assert 'continuation = yes' in text
    assert 'constraints = none' in mdp('em',123,200)


def test_pbc_unwrap_and_rotational_invariance():
    x=np.array([[0,0,0],[.15,.02,0],[.3,0,0],[.45,.02,0],[.6,0,0]])
    box=np.array([8.,8.,8.])
    wrapped=(x+7.8)%box
    y=unwrap_chain(wrapped,box)
    assert np.allclose(y-y[0],x-x[0])
    a=metrics(x,box); b=metrics(x[:,[1,2,0]],box)
    for key in ['rg_nm','anisotropy','contacts_per_carbon','nematic_order']:
        assert np.isclose(a[key],b[key])
    assert a['trans_fraction']==1


def test_dwell_rejects_flickers_and_ambiguous_gaps():
    times=np.arange(10)*10
    assert committed_labels([0,0,0,1,0,0,-1,1,1,1],times,20)==[(20.,0),(90.,1)]
    assert committed_labels([0,1]*5,times,20)==[]


def test_archived_forcefield_reference():
    assert 'ffbonded.itp' in verify_ff(ROOT/config()['forcefield'])


def test_topology_pairs_are_exact_graph_distance_three():
    from rdkit import Chem
    mol=molecule(8)
    text,_=topology(mol)
    pair_block=text.split('[ pairs ]')[1].split('[ angles ]')[0]
    actual={tuple(int(v)-1 for v in line.split()[:2]) for line in pair_block.strip().splitlines()}
    distances=Chem.GetDistanceMatrix(mol)
    expected={(i,j) for i in range(len(distances)) for j in range(i+1,len(distances)) if distances[i,j]==3}
    assert actual==expected


def test_recurrence_counts_both_directions_once():
    events=committed_labels([0]*4+[1]*4+[0]*4,np.arange(12)*10,20)
    assert events==[(20.,0),(60.,1),(100.,0)]


@pytest.mark.parametrize('drift,should_pass',[(0.,True),(.05,False)])
def test_equilibration_gate_rejects_density_drift(tmp_path,monkeypatch,drift,should_pass):
    def fake_call(args,cwd,log,stdin=None):
        name=args[args.index('-o')+1]
        rows=[]
        for i in range(100):
            density=1000*(1+drift*(i>=75))
            rows.append(f'{i} 300 {density}' if name.startswith('npt') else f'{i} 300')
        (tmp_path/name).write_text('\n'.join(rows))
    monkeypatch.setattr(pilot,'call',fake_call)
    if should_pass:
        pilot.check_equilibration(tmp_path,'unused')
        assert (tmp_path/'equilibration-check.json').exists()
    else:
        with pytest.raises(RuntimeError,match='density'):
            pilot.check_equilibration(tmp_path,'unused')

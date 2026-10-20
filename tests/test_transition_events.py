import numpy as np
import pytest
from transition_events import detect,classify

def test_flickers_and_undecided_do_not_make_new_events():
    t=np.arange(20)*10.
    labels=[0]*4+[-1,1,1,-1,1,1,-1]+[0]*9
    assert detect(t,labels,20)["complete_cycles"]==0

def test_complete_cycle_initial_expanded_and_right_censoring():
    labels=[1]*4+[0]*4+[1]*4+[0]*4+[1]*4
    r=detect(np.arange(20)*10.,labels,20)
    assert r["complete_cycles"]==1
    assert r["initial_committed_state"]=="E"
    assert r["unfinished_expansion"] is not None
    assert r["cycles"][0]["expanded_core_entry_ns"]==.08

def test_joint_core_and_sampling_gap():
    cfg=dict(sampling_ps=10,smoothing_ps=10,compact=dict(rg_max_nm=.65,contacts_min=1.8,hydration_max=90),
             expanded=dict(rg_min_nm=.85,contacts_max=1.4,hydration_min=95))
    rows=[dict(time_ps=i*10,rg_nm=.95,contacts_per_carbon=1.,hydration_waters=h) for i,h in enumerate([80,100,80])]
    assert classify(rows,cfg)[1].tolist()==[-1,1,-1]
    rows[-1]["time_ps"]=30
    with pytest.raises(ValueError): classify(rows,cfg)

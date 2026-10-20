import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import numpy as np
from run import memory

def test_frozen_contacts_keep_memory():
    rng=np.random.default_rng(7)
    c=np.repeat(rng.random((32,1,128))>.5,51,axis=1)
    assert all(abs(v-1)<1e-12 for v in memory(c,np.full(128,.5)).values())

def test_independent_contacts_forget():
    c=np.random.default_rng(7).random((64,51,128))>.5
    assert max(abs(v) for v in memory(c,np.full(128,.5)).values())<.03

import numpy as np

def wgn_process(n, rng=None):
    rng = rng or np.random.default_rng(1)
    return rng.standard_normal(n)

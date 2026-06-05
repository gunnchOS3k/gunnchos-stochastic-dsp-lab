from gunnchos_dsp.ofdm import ofdm_mod
import numpy as np

def test_ofdm():
    assert len(ofdm_mod(np.zeros(64))) == 64

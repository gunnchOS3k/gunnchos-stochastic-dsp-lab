from oulu_dsp.signals import tone, awgn
import numpy as np

def test_tone():
    assert len(tone(1e6, 10e3, 100)) == 100

def test_awgn():
    assert awgn((10,), 10).shape == (10,)

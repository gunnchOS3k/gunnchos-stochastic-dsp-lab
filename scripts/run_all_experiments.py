import json
from pathlib import Path
import numpy as np
from oulu_dsp.signals import tone, awgn
from oulu_dsp.matched_filter import matched_filter
from oulu_dsp.ofdm import ofdm_mod

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results'
OUT.mkdir(exist_ok=True)

fs, n = 1e6, 1024
x = tone(fs, 50e3, n)
y = awgn(x.shape, 10)
template = tone(fs, 50e3, 64)
_ = matched_filter(y[:64], template)
_ = ofdm_mod(np.random.randint(0, 2, 128))
(OUT / 'experiment_summary.md').write_text('# DSP experiments\n\nMatched filter + OFDM smoke PASS\n')
print('experiments ok')

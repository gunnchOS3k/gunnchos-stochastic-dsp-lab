from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from oulu_dsp.signals import tone, awgn

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / 'results/figures'
FIG.mkdir(parents=True, exist_ok=True)
x = tone(1e6, 100e3, 512)
y = awgn(x.shape, 5)
plt.figure(); plt.plot(np.real(x), label='tone'); plt.plot(np.real(y), alpha=0.5, label='awgn'); plt.legend(); plt.savefig(FIG/'dsp_waveforms.png'); plt.close()
print('figures ok')

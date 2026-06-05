import numpy as np

def tone(fs, f0, n):
    t = np.arange(n) / fs
    return np.exp(2j * np.pi * f0 * t)

def awgn(shape, snr_db, rng=None):
    rng = rng or np.random.default_rng(0)
    sig_pwr = 1.0
    noise_pwr = sig_pwr / (10 ** (snr_db / 10))
    return (rng.standard_normal(shape) + 1j * rng.standard_normal(shape)) * np.sqrt(noise_pwr / 2)

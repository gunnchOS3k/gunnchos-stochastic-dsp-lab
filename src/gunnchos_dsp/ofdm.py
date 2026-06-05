import numpy as np

def ofdm_mod(bits, n_sub=64):
    symbols = 2 * bits[:n_sub] - 1
    return np.fft.ifft(symbols)

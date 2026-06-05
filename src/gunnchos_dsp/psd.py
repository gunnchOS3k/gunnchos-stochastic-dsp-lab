import numpy as np

def welch_psd(x, fs, nperseg=256):
    from numpy.fft import rfft, rfftfreq
    X = rfft(x[:nperseg])
    f = rfftfreq(nperseg, 1/fs)
    return f, np.abs(X) ** 2

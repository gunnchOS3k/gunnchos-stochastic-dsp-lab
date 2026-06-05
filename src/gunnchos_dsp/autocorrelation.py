import numpy as np

def autocorr(x, max_lag=32):
    x = x - np.mean(x)
    return np.correlate(x, x, mode='full')[len(x)-1:len(x)+max_lag]

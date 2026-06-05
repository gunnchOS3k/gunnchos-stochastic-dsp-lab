import numpy as np

def moving_average(x, k=8):
    return np.convolve(x, np.ones(k)/k, mode='same')

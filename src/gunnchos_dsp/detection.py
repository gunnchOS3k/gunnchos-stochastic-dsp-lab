import numpy as np

def energy_detector(x, thresh):
    return float(np.mean(np.abs(x) ** 2) > thresh)

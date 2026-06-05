import numpy as np

def ls_estimate(rx_pilot, tx_pilot):
    return np.mean(rx_pilot / (tx_pilot + 1e-12))

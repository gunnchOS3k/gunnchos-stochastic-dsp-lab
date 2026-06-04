import numpy as np

def kalman_1d(z, q=0.01, r=0.1):
    x, p = 0.0, 1.0
    xs = []
    for zk in z:
        p = p + q
        k = p / (p + r)
        x = x + k * (zk - x)
        p = (1 - k) * p
        xs.append(x)
    return np.array(xs)

import numpy as np

def wiener_scalar(sn_obs, sn_sig=1.0):
    return sn_sig / (sn_sig + sn_obs)

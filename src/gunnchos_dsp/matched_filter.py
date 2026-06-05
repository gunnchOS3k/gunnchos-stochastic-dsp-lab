import numpy as np

def matched_filter(rx, template):
    return np.correlate(rx, template, mode='same')

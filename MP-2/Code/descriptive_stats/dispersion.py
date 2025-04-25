import numpy as np

def variance(data):
    return np.var(data, ddof=1)

def standard_deviation(data):
    return np.std(data, ddof=1)

def range_stat(data):
    return np.max(data) - np.min(data)

def iqr(data):
    q3, q1 = np.percentile(data, [75, 25])
    return q3 - q1

import numpy as np

__all__ = ['variance', 'standard_deviation', 'range_stat', 'iqr', 'iqr_outliers']

def variance(data):
    return np.var(data, ddof=1)

def standard_deviation(data):
    return np.std(data, ddof=1)

def range_stat(data):
    return np.max(data) - np.min(data)

def iqr(data):
    q3, q1 = np.percentile(data, [75, 25])
    return q3 - q1

def iqr_outliers(data, column):
    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75) 
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return data[(data[column] < lower_bound) | (data[column] > upper_bound)]

import numpy as np

def compute_mse(X, y, beta):
    '''
    Calculate the estimated y values and use these to calculate the MSE.
    '''
    n = X.shape[0]
    return 1/n * np.sum((y-X@beta)**2)
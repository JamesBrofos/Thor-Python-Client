import numpy as np


def michalewicz(x):
    xx = x.ravel()
    d = len(xx)
    m = 10
    v = np.sin(np.array([i * xx[i]**2 / np.pi for i in range(d)]))
    return np.sum(np.sin(x) * v ** (2*m))

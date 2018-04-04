import numpy as np

def eggholder(x):
    xx = x.ravel()
    x1 = xx[0]
    x2 = xx[1]
    term1 = -(x2 + 47.) * np.sin(np.sqrt(np.abs(x2 + x1 / 2. + 47.)))
    term2 = -x1 * np.sin(np.sqrt(np.abs(x1-(x2 + 47.))))
    return -(term1 + term2)


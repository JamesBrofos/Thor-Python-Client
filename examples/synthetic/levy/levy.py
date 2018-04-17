import numpy as np


def levy(xx):
    d = len(xx)
    w = np.zeros(d)
    for ii in range(d):
	    w[ii] = 1. + (xx[ii] - 1.) / 4.

    term1 = (np.sin(np.pi * w[0]))**2
    term3 = (w[d-1] - 1.)**2 * (1. + (np.sin(2*np.pi*w[d-1]))**2)
    term2 = 0.
    for ii in range(d-1):
        wi = w[ii]
        new = (wi - 1.)**2 * (1. + 10.*(np.sin(np.pi * wi + 1.))**2)
        term2 += new

    y = term1 + term2 + term3
    return -y

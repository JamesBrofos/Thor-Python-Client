import numpy as np

def shekel(x):
    xx = x.ravel()
    m = 10
    b = 0.1 * np.array([1, 2, 2, 4, 4, 6, 3, 7, 5, 5])
    C = np.array([[4.0, 1.0, 8.0, 6.0, 3.0, 2.0, 5.0, 8.0, 6.0, 7.0],
                  [4.0, 1.0, 8.0, 6.0, 7.0, 9.0, 3.0, 1.0, 2.0, 3.6],
                  [4.0, 1.0, 8.0, 6.0, 3.0, 2.0, 5.0, 8.0, 6.0, 7.0],
                  [4.0, 1.0, 8.0, 6.0, 7.0, 9.0, 3.0, 1.0, 2.0, 3.6]])
    outer = 0.
    for i in range(m):
	    bi = b[i]
	    inner = 0.
	    for j in range(4):
		    xj = xx[j]
		    Cji = C[j, i]
		    inner += (xj-Cji)**2
	    outer += 1. / (inner + bi)
    return outer


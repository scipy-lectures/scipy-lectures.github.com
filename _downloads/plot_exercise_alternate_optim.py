"""
Alternating optimization
=========================

"""
import time

import numpy as np
from scipy import optimize
import pylab as pl

np.random.seed(0)

n_dim = 100

K = np.random.normal(size=(100, 100))

def f(x):
    return np.sum((np.dot(K, x) - 1)**2) + np.sum(x**2)**2

###############################################################################
# Some pretty plotting

pl.figure(1)
pl.clf()
Z = X, Y = np.mgrid[-1.5:1.5:100j, -1.1:1.1:100j]
# Complete in the additional dimensions with zeros
Z = np.reshape(Z, (2, -1)).copy()
Z.resize((100, Z.shape[-1]))
Z = np.apply_along_axis(f, 0, Z)
Z = np.reshape(Z, X.shape)
pl.imshow(Z.T, cmap=pl.cm.gray_r, extent=[-1.5, 1.5, -1.1, 1.1],
          origin='lower')
pl.contour(X, Y, Z, cmap=pl.cm.gnuplot)

# A reference but slow solution:
x_ref = optimize.fmin_powell(f, K[0], xtol=1e-10)

t0 = time.time()
x_bfgs = optimize.fmin_bfgs(f, K[0])[0]
print 'BFGS: time %.1fs, error %.2f' % (t0 - time.time(),
    np.sum((x_bfgs - x_ref)**2))

x_l_bfgs = optimize.fmin_l_bfgs_b(f, K[0], approx_grad=1)[0]
print 'BFGS: time %.1fs, error %.2f' % (t0 - time.time(),
    np.sum((xa - x_ref)**2))


# Plot our solution
#pl.plot(x_min[0], x_min[1], 'r+', markersize=15)

pl.show()


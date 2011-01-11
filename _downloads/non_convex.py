"""
Non convex
===========

Demo non-convex problems
"""
import numpy as np

from mayavi import mlab

def f(x):
    return 1 - np.exp(-x**2) + .01*x**2

x, y = np.mgrid[-3:3:100j, -3:3:100j]

z = f(x) + f(y)

mlab.clf()
mlab.surf(x, y, z)
mlab.show()

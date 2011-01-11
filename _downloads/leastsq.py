import numpy as np
from scipy import optimize

def f(x):
    z = np.arctan(x) - np.arctan(np.linspace(0, 1, len(x)))
    return z

def g(x):
    return np.sum(f(x)**2)

x0 = np.zeros(10)

print optimize.leastsq(f, x0)
print optimize.fmin_bfgs(g, x0)

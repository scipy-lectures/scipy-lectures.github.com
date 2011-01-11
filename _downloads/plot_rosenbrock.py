"""
Demo gradient descent
"""
import numpy as np
import pylab as pl

x_min, x_max = -0.6, 1.1
y_min, y_max = -0.1, 1.1

x0, y0 = 3., 2.
epsilon = .1

for index, epsilon in enumerate((1, .01)):
    # s_x, s_y = 1.5, .01
    #def f(x, y):
    #    return -s_x*np.cos(x - x0) - s_y*np.cos(y - y0)

    #def f_prime(x, y):
    #    return s_x*np.sin(x - x0), s_y*np.sin(y - y0)

    def rosenbrock(x, y):
        return epsilon*(1 - x)**2 + (y - x**2)**2

    def rosenbrock_prime(x, y):
        return (-epsilon*2*(1 - x) - 4*x*(y - x**2),
                2*(y - x**2))

    f = rosenbrock
    f_prime = rosenbrock_prime

    x, y = np.mgrid[x_min:x_max:100j, y_min:y_max:100j]
    x = x.T
    y = y.T

    pl.figure(index, figsize=(3, 2.5))
    pl.clf()
    #pl.axes([0, 0, 1, 1])

    contours = pl.contour(f(x, y),
                        extent=[x_min, x_max, y_min, y_max],
                        cmap=pl.cm.gnuplot, origin='lower')
    pl.clabel(contours,
            inline=1,
            fmt='%1.1f',
            fontsize=14)

    x_i, y_i = 0, 0
    all_x_i = list()
    all_y_i = list()

    for i in range(10):
        all_x_i.append(x_i)
        all_y_i.append(y_i)
        dx_i, dy_i = f_prime(x_i, y_i)
        x_i += -dx_i
        y_i += -dy_i

    pl.plot(all_x_i, all_y_i, 'b-')
    pl.plot(all_x_i, all_y_i, 'k+')

    pl.plot([x0], [y0], 'rx')

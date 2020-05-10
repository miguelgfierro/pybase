from scipy.optimize import rosen
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plot


def rosenbrock(x):
    """The `Rosenbrock function <https://en.wikipedia.org/wiki/Rosenbrock_function>`_ is a non-convex function 
    used as a performance test problem for optimization algorithms. The function is defined by: 

    .. math ::

        f(x,y) = (a-x)^2 + b(y-x^2)^2
    
    The global minimum is inside a long, narrow, parabolic shaped flat valley. To find the valley is trivial. 
    To converge to the global minimum, is difficult.
    
    `See more info <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.rosen.html>`_

    Args:
        x (np.array or list): 1-D array of points at which the Rosenbrock function is to be computed.

    Returns:
        float: The value of the Rosenbrock function.

    Examples:
        >>> rosenbrock([1, 1])
        0.0
    
    """
    # return 100*(x[1] - x[0]**2)**2 + (1 - x[0])**2
    return rosen(x)


def ackley(x):
    """`Ackley function <https://en.wikipedia.org/wiki/Ackley_function>`_

    The Ackley function is a non-convex function used as a performance test problem for optimization algorithms. 

    Args:
        x (np.array or list): array of two components ``(x_0, x_1)``.

    Returns:
        float: The value of the Ackley function.
    """
    arg1 = -0.2 * np.sqrt(0.5 * (x[0] ** 2 + x[1] ** 2))
    arg2 = 0.5 * (np.cos(2.0 * np.pi * x[0]) + np.cos(2.0 * np.pi * x[1]))
    return -20.0 * np.exp(arg1) - np.exp(arg2) + 20.0 + np.e


def plot_function2D(x, y, z):
    """Plot 2D function with matplotlib
    
    Args:
        x (np.array): X value.
        y (np.array): Y value.
        z (np.array): function value.
    
    Examples::

        >> s = 0.05
        >> X = np.arange(-2, 2.+s, s)
        >> Y = np.arange(-2, 6.+s, s)
        >> X, Y = np.meshgrid(X, Y)
        >> f = rosenbrock([X, Y])
        >> plot_function2D(X, Y, f)
    """
    fig = plot.figure()
    ax = fig.gca(projection="3d")
    surf = ax.plot_surface(
        x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False
    )
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plot.show()

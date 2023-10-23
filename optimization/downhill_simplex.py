from scipy.optimize import fmin


def optimize_function(func, initial_guess, **kargs):
    """Function optimization using downhill simplex algorithm (`Nelder-Mead algorithm <https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method>`_).
    This algorithm only uses function values, not derivatives or second derivatives.
    It will usually be slower than an algorithm that uses first or second derivative information.
    In practice it can have poor performance in high-dimensional problems and is not robust to minimizing
    complicated functions. It might not successfully converge to the minimum.

    `See more info <https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin.html#scipy-optimize-fmin>`_.

    Args:
        func (callable): The objective function to be minimized. In the form ``f(x, *args)``, where x is the argument in
                         the form of a 1-D array and args is a tuple of any additional parameters.
        initial_guess (np.array): Initial guess.

    Returns:
        np.array: Result of the optimization.
        float: Value of function at minimum.

    Examples:
        >>> from .functions import rosenbrock
        >>> np.random.seed(42)
        >>> x0 = np.array([0, 0, 0, 0, 0])
        >>> xopt, fopt = optimize_function(rosenbrock, x0) # xopt = [0.9999974 , 0.99999158, 0.99998042, 0.9999658 , 0.99993196]
        >>> expected_result = np.array([1, 1, 1, 1, 1])
        >>> np.allclose(xopt, expected_result, rtol=1e-3, atol=1e-3)
        True
        >>> round(fopt, ndigits=5)
        0.0
        >>> from .functions import ackley
        >>> x0 = np.array([1, 1])
        >>> xopt, fopt = optimize_function(ackley, x0)
        >>> xopt # Real solution [0,0]
        array([0.96852082, 0.96848094])
        >>> fopt
        3.574451924990758
    """
    [xopt, fopt, iter, funcalls, warnflag, allvecs] = fmin(
        func, x0=initial_guess, full_output=True, retall=True, disp=False, **kargs
    )
    return xopt, fopt

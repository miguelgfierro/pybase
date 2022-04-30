from itertools import product

def combine_params(*values):
    """combine_params _summary_

    Args:
        values (_type_): _description_

    Returns:
        iterator: _description_

    Examples:
        >>> n = [1, 2]
        >>> l = ["a", "b"]
        >>> for vals in combine_params(n,l):
        ...     print(vals)
        (1, 'a')
        (1, 'b')
        (2, 'a')
        (2, 'b')
        >>> f = [0.1, 0.2]
        >>> for vals in combine_params(n,l,f):
        ...     print(vals)
        (1, 'a', 0.1)
        (1, 'a', 0.2)
        (1, 'b', 0.1)
        (1, 'b', 0.2)
        (2, 'a', 0.1)
        (2, 'a', 0.2)
        (2, 'b', 0.1)
        (2, 'b', 0.2)
    """
    return product(*values)
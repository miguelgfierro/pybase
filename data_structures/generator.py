from itertools import product


def combine_params(*values):
    """Create a generator that returns a combination of any arbitrary set of values.

    Args:
        values (list): An arbitrary number of lists to be combined.    

    Returns:
        iterator: A generator with the combines values.

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


def yield_data(data, batch_size, complete_batches=False):
    """Yield an array in batches.
    
    Args:
        data (np.array or list): An array or list.
        batch_size (int): The size of the data batch yielded.
        complete_batches (bool): If `True` it will return complete batches,
                                 if `False` it will return the complete list
                                 so the last batch may have a different size.
    
    Returns:
        generator (iterable): An iterator that yield the data.
    
    Examples:
        >>> data = np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(3,2,2)
        >>> for l in yield_data(data, 2, False):
        ...     print(l)
        [[[1 2]
          [3 4]]
        <BLANKLINE>
         [[5 6]
          [7 8]]]
        [[[ 9 10]
          [11 12]]]
        >>> for l in yield_data(data, 2, True):
        ...     print(l)
        [[[1 2]
          [3 4]]
        <BLANKLINE>
         [[5 6]
          [7 8]]]
        >>> py_list = [0,0,1,1,2,2,3,3,4,4]
        >>> for l in yield_data(py_list, 4, False):
        ...     print(l)
        [0, 0, 1, 1]
        [2, 2, 3, 3]
        [4, 4]

    """
    if complete_batches:
        for i in range(len(data) // batch_size):
            yield data[i * batch_size : (i + 1) * batch_size]
    else:
        for i in range(0, len(data), batch_size):
            yield data[i : i + batch_size]

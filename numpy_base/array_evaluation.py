import numpy as np


def has_same_sign(data):
    """Evaluate whether the array has all elements with the same sign.
    
    Args:
        data (np.array): An array.
    
    Returns:
        bool: Boolean with the evaluation.
    
    Examples:
        >>> data = np.array([(1,2,3),(2,3,4)])
        >>> has_same_sign(data)
        True
        >>> data = np.array([0,0])
        >>> has_same_sign(data)
        WARNING: All zeros
        True
        >>> data = np.array([(0,0),(1,2)])
        >>> has_same_sign(data)
        False
    """
    try:
        idx = next((idx for idx, val in np.ndenumerate(data) if val != 0))
    except StopIteration:
        print("WARNING: All zeros")
        return True
    return np.all(data > 0) if data[idx] > 0 else np.all(data < 0)


def has_same_sign_or_zero(data):
    """Evaluate whether the array has all elements with the same sign or zero.
    
    Args:
        data (np.array): An array.
    
    Returns:
        bool: Boolean with the evaluation.
    
    Examples:
        >>> data = np.array([(1,2,3),(2,3,4)])
        >>> has_same_sign_or_zero(data)
        True
        >>> data = np.array([0,0])
        >>> has_same_sign_or_zero(data)
        WARNING: All zeros
        True
        >>> data = np.array([(0,0),(-1,2)])
        >>> has_same_sign_or_zero(data)
        False
    """
    try:
        idx = next((idx for idx, val in np.ndenumerate(data) if val != 0))
    except StopIteration:
        print("WARNING: All zeros")
        return True
    return np.all(data >= 0) if data[idx] >= 0 else np.all(data <= 0)


def count_items(array, item):
    """Count the number of items in the array
    
    Args:
        array (np.array): An array.
        item (int, float or str): The item to count.
    
    Returns:
        int: Number of items.
    
    Examples:
        >>> data = np.array([(1,0,0,0,1,1,0)])
        >>> count_items(data, 1)
        3
    """
    return np.count_nonzero(array == item)


def array_intersection(ar1, ar2, assume_unique=False, return_indices=False):
    """Find the intersection between an array and another array or a group of arrays. Return the sorted, unique 
    values that are in of the input arrays.
    
    Args:
        ar1 (np.array or list): An array or list.
        ar2 (np.array, list, list of arrays or list of lists): Array, list or a list of the previous objects.
        assume_unique (bool): If True, the input arrays are assumed to be unique, which can speed up the calculation.
        return_indices (bool): If True, the indices which correspond to the intersection of the arrays are returned.
    
    Returns:
        tuple: tuple containing:

            np.array: Sorted 1D array of common and unique elements.
            np.array: Indices of the first occurrences of the common values in ar1. Provided if return_indices is True.
            np.array: Indices of the first occurrences of the common values in ar2. Provided if return_indices is True. 
    
    Examples: 
        >>> ar1 = [1,2,3,4,5]
        >>> ar2 = [3,4,5,6,5]
        >>> ar3 = [2,3,4,6]
        >>> arr_list = [ar2, ar3, ar2]
        >>> array_intersection(ar1, ar2)
        array([3, 4, 5])
        >>> array_intersection(ar1, arr_list)
        array([3, 4])

    """
    if any(isinstance(el, np.ndarray) for el in ar2) or any(
        isinstance(el, list) for el in ar2
    ):
        return reduce(
            lambda x, y: np.intersect1d(
                x, y, assume_unique=assume_unique, return_indices=return_indices
            ),
            (ar1, *ar2),
        )
    elif isinstance(ar2, np.ndarray) or isinstance(ar2, list):
        return np.intersect1d(
            ar1, ar2, assume_unique=assume_unique, return_indices=return_indices
        )
    else:
        raise ValueError("ar2 has a wrong type: {}".format(type(ar2)))


def array_difference(ar1, ar2, assume_unique=False):
    """Find the difference between an array and another array or a group of arrays. Return the unique 
    values in ar1 that are not in ar2..
    
    Args:
        ar1 (np.array or list): An array or list.
        ar2 (np.array, list, list of arrays or list of lists): Array, list or a list of the previous objects.
        assume_unique (bool): If True, the input arrays are assumed to be unique, which can speed up the calculation.
    
    Returns:
        np.array: values in ar1 that are not in ar2. The result is sorted when assume_unique=False, but otherwise 
        only sorted if the input is sorted.
        
    Examples: 
        >>> ar1 = [1,2,3,4,5]
        >>> ar2 = [3,4,5,6,5]
        >>> ar3 = [2,3,4,6]
        >>> arr_list = [ar2, ar3, ar2]
        >>> array_difference(ar1, ar2)
        array([1, 2])
        >>> array_difference(ar1, arr_list)
        array([1])

    """
    if any(isinstance(el, np.ndarray) for el in ar2) or any(
        isinstance(el, list) for el in ar2
    ):
        return reduce(
            lambda x, y: np.setdiff1d(x, y, assume_unique=assume_unique), (ar1, *ar2)
        )
    elif isinstance(ar2, np.ndarray) or isinstance(ar2, list):
        return np.setdiff1d(ar1, ar2, assume_unique=assume_unique)
    else:
        raise ValueError("ar2 has a wrong type: {}".format(type(ar2)))


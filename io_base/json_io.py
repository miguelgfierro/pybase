import json


def save_file(data, filename):
    """Save a dictionary as JSON format.
    Note: When saving in JSON format, the key has to be a string, it can't be a number
    
    Args:
        data (dict): A dictionary.
        filename (str): Name of the file.
    
    Examples:
        >>> data = {'name': 'Luke','surname': 'Skywalker', 1:2,'3':'4'}
        >>> save_file(data, 'file.json')
        >>> os.path.isfile('file.json')
        True
        >>> os.remove('file.json')
        >>> os.path.isfile('file.json')
        False

    """
    with open(filename, "w") as outfile:
        json.dump(data, outfile)


def read_file(filename):
    """Read a JSON file.
    
    Args:
        filename (str): Name of the file.
    
    Returns:
        dict: A dictionary.
    
    Examples:
        >>> data = read_file('share/data.json')
        >>> type(data)
        <class 'dict'>
        >>> sorted(data.items(), key=lambda t: t[0])
        [('1', 2), ('3', '4'), ('name', 'Luke'), ('surname', 'Skywalker')]

    """
    with open(filename) as json_file:
        data = json.load(json_file)
    return data

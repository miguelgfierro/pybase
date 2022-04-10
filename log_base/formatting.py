import json
from datetime import datetime, date


def format_dictionary(dct, indent=4):
    """Formats a dictionary to be printed

    Args:
        dct (dict): Dictionary.
        indent (int): Indentation value.

    Returns:
        str: Formatted dictionary ready to be printed

    Examples:
        >>> dct = {'bkey':1, 'akey':2}
        >>> print(format_dictionary(dct))
        {
            "akey": 2,
            "bkey": 1
        }
    """
    return json.dumps(dct, indent=indent, sort_keys=True)


def format_float_as_string():
    """Example of formatting a float as a string

    Examples:
        >>> format_float_as_string()
        'num=0.12'
    """
    return "num={:0.2f}".format(0.123456)


def format_date():
    """Example of formatting a datetime.

    `See more info <https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior>`_

    Examples:
        >>> format_date()
        2002-12-04
        2002-12-04T00:00:00
        Dec 04 2002 00:00:00
        04/12/02
    """
    print(date(2002, 12, 4).isoformat())
    print(datetime(2002, 12, 4).isoformat())
    print(datetime(2002, 12, 4).strftime("%b %d %Y %H:%M:%S"))
    print(datetime(2002, 12, 4).strftime("%d/%m/%y"))


def format_num_with_leading_zeros(num, leading_zeros):
    """Format a number with leading zeros.

    Args:
        num (int): A number.
        leading_zeros (int): Number of leading zeros.

    Returns:
        str: The number with leading zeros.

    Examples:
        >>> format_num_with_leading_zeros(14, 4)
        '0014'
        >>> format_num_with_leading_zeros(14, 2)
        '14'
    """
    return str(num).rjust(leading_zeros, "0")

import pandas as pd


def _get_nominal_integer_dict(nominal_vals):
    """Convert nominal values in integers, starting at 0.

    Args:
        nominal_vals (pd.Series): A series.

    Returns:
        dict: An dictionary with numeric values.

    """
    d = {}
    for val in nominal_vals:
        if val not in d:
            current_max = max(d.values()) if len(d) > 0 else -1
            d[val] = current_max + 1
    return d


def _convert_to_integer(srs, d):
    """Convert series to integer, given a dictionary.

    Args:
        srs (pd.Series): A series.
        d (dict): A dictionary mapping values to integers

    Returns:
        pd.Series: An series with numeric values.

    """
    return srs.map(lambda x: d[x])


def _convert_to_string(srs):
    """Convert series to string.

    Args:
        srs (pd.Series): A series.

    Returns:
        pd.Series: An series with string values.

    """
    return srs.map(lambda x: str(x))


def convert_cols_categorical_to_numeric(df, col_list=None):
    """Convert categorical columns to numeric and leave numeric columns
    as they are. You can force to convert a numerical column if it is
    included in ``col_list``.

    Args:
        df (pd.DataFrame): Dataframe.
        col_list (list): List of columns.

    Returns:
        pd.DataFrame: An dataframe with numeric values.

    Examples:
        >>> df = pd.DataFrame({'letters':['a','b','c'],'numbers':[1,2,3]})
        >>> df_numeric = convert_cols_categorical_to_numeric(df)
        >>> print(df_numeric)
           letters  numbers
        0        0        1
        1        1        2
        2        2        3

    """
    if col_list is None:
        col_list = []
    ret = pd.DataFrame()
    for column_name in df.columns:
        column = df[column_name]
        if column.dtype == "object" or column_name in col_list:
            col_dict = _get_nominal_integer_dict(column)
            ret[column_name] = _convert_to_integer(column, col_dict)
        else:
            ret[column_name] = column
    return ret


def convert_related_cols_categorical_to_numeric(df, col_list):
    """Convert categorical columns, that are related between each other,
    to numeric and leave numeric columns as they are.

    Args:
        df (pd.DataFrame): Dataframe.
        col_list (list): List of columns.

    Returns:
        pd.DataFrame: An dataframe with numeric values.

    Examples:
        >>> df = pd.DataFrame({'letters':['a','b','c'],'letters2':['c','d','a'],'numbers':[1,2,3]})
        >>> df_numeric = convert_related_cols_categorical_to_numeric(df, col_list=['letters','letters2'])
        >>> print(df_numeric)
           letters  letters2  numbers
        0        0         2        1
        1        1         3        2
        2        2         0        3

    """
    ret = pd.DataFrame()
    values = None
    for c in col_list:
        values = pd.concat([values, df[c]], axis=0)
        values = pd.Series(values.unique())
    col_dict = _get_nominal_integer_dict(values)
    for column_name in df.columns:
        column = df[column_name]
        if column_name in col_list:
            ret[column_name] = _convert_to_integer(column, col_dict)
        else:
            ret[column_name] = column
    return ret


def convert_cols_numeric_to_categorical(df, col_list=None):
    """Convert numerical columns to categorical and leave numeric columns as they are.

    Args:
        df (pd.DataFrame): Dataframe.
        col_list (list): List of columns.

    Returns:
        pd.DataFrame: An dataframe with categorical values.

    Examples:
        >>> df = pd.DataFrame({'letters':['a','b','c'],'numbers1':[-1,0.5,10],'numbers2':[1,2,3]})
        >>> df_cat = convert_cols_numeric_to_categorical(df, col_list=['numbers1'])
        >>> print(df_cat)
          letters numbers1  numbers2
        0       a     -1.0         1
        1       b      0.5         2
        2       c     10.0         3
        >>> print(df_cat['numbers1'].dtype)
        object
        >>> print(df_cat['numbers2'].dtype)
        int64

    """
    if col_list is None:
        col_list = df.columns
    ret = pd.DataFrame()
    for column_name in df.columns:
        column = df[column_name]
        if column_name in col_list and column.dtype != "object":
            ret[column_name] = _convert_to_string(column)
        else:
            ret[column_name] = column
    return ret


def replace_column_values(df, val_dict, col_name, new_col_name=None):
    """Replace all appearances of a value to another in a dictionary.

    Args:
        df (pd.DataFrame): Dataframe.
        val_dict (dict): Dictionary with the values to replace.
        col_name (str): Column name.
        new_col_name (str): New column name.

    Returns:
        pd.DataFrame: A dataframe with the values replaced.

    Examples:
        >>> df = pd.DataFrame({'letters':['a','a','c'], 'numbers':[1,2,3]})
        >>> df_return = replace_column_values(df, {'a':1}, 'letters')
        >>> df_return
          letters  numbers
        0       1        1
        1       1        2
        2       c        3
        >>> df_return = replace_column_values(df, {'a':1}, 'letters', 'new_column')
        >>> df_return
          letters  numbers new_column
        0       a        1          1
        1       a        2          1
        2       c        3          c

    """
    df_return = df.copy()
    if new_col_name is None:
        # NOTE: even though according to https://stackoverflow.com/a/41678874/5620182, using map
        # is 10x faster than replace, in my own benchmarks replace is 3x faster than
        # map(val_dict).fillna(df_return[col_name]) and about the same as map(val_dict), however
        # this last one will leave as NaN all values that are not in val_dict
        df_return[col_name] = df_return[col_name].replace(val_dict)
    else:
        df_return[new_col_name] = df_return[col_name].replace(val_dict)
    return df_return


def add_row(df, row):
    """Add a row to a dataframe.

    .. note::

        According to `this source <https://stackoverflow.com/questions/41888080/python-efficient-way-to-add-rows-to-dataframe/41888241#41888241>`_
        using ``loc`` is 14x faster.

    Args:
        df (pd.DataFrame): Dataframe.
        row (dict): A dictionary.

    Examples:
        >>> df = pd.DataFrame(columns=["l", "n"])
        >>> row = {"l": "a", "n": 1}
        >>> add_row(df, row)
        >>> df
           l  n
        0  a  1
        >>> row = {"l": "b", "n": 2}
        >>> add_row(df, row)
        >>> df
           l  n
        0  a  1
        1  b  2

    """
    df.loc[df.shape[0]] = row


def split_text_in_column(df, component, col_name, new_col_list):
    """Split a text in a dataframe column by a component.

    Args:
        df (pd.DataFrame): Dataframe.
        component (str): Component for splitting the text.
        col_name (str): Column name.
        new_col_list (list): List of new column names.

    Returns:
        pd.DataFrame: A dataframe with the values replaced.

    Examples:
        >>> df = pd.DataFrame({'paths':['/user/local/bin/','/user/local/share/','/user/local/doc/'], 'numbers':[1,2,3]})
        >>> df_return = split_text_in_column(df, '/', 'paths', ['a','b','c'])
        >>> df_return
           numbers     a      b      c
        0        1  user  local    bin
        1        2  user  local  share
        2        3  user  local    doc

    """
    df_exp = df[col_name].str.split(component, expand=True)
    df_exp = df_exp.loc[:, (df_exp != "").any(axis=0)]  # remove columns with no text
    df_exp.columns = new_col_list
    df = pd.concat([df, df_exp], axis=1)
    df.drop(columns=col_name, inplace=True)
    return df


def expand_list_in_rows(df, columns=None, reset_index=True):
    """expand_list_in_rows _summary_

    Args:
        df (pd.DataFrame): Dataframe.
        columns (list): List of columns to apply the expansion.

    Returns:
        pd.DataFrame: A dataframe with a row for each value in the list.

    Example:
        >>> df = pd.DataFrame({"a":[[1,2,3]], "b":[[4,5,6]]})
        >>> df
                   a          b
        0  [1, 2, 3]  [4, 5, 6]
        >>> expand_list_in_rows(df)
           a  b
        0  1  4
        1  2  5
        2  3  6
        >>> expand_list_in_rows(df, columns=["a","b"])
           a  b
        0  1  4
        1  2  5
        2  3  6
        >>> expand_list_in_rows(df, columns=["a"])
           a          b
        0  1  [4, 5, 6]
        1  2  [4, 5, 6]
        2  3  [4, 5, 6]
        >>> expand_list_in_rows(df, reset_index=False)
           a  b
        0  1  4
        0  2  5
        0  3  6
    """
    if columns is None or columns == df.columns.tolist():
        # Using apply with pd.Series.explode is 30x faster than df.explode(columns)
        df_return = df.apply(pd.Series.explode)
    else:
        df_return = df.explode(columns)
    if reset_index is True:
        return df_return.reset_index(drop=True)
    return df_return

import pandas as pd
import operator


def get_unique_values_in_column(df, col_name):
    """Get unique values in a column.
    
    Args:
        df (pd.DataFrame): Dataframe.
        col_name (str): Column name.
    
    Returns:
        np.array: Unique values.
    
    Examples:
        >>> df = pd.DataFrame({"letters":["a","a","c"], "numbers":[1,2,3]})
        >>> vals = get_unique_values_in_column(df, "letters")
        >>> print(vals)
        ['a' 'c']
    """
    return df[col_name].unique()


def get_random_fraction_of_rows(df, row_fraction=0.5, reindex=True):
    """Get a random fraction of the dataframe rows.
    
    Args:
        df (pd.DataFrame): Dataframe.
        row_fraction (float): Fraction (in percentage) of rows to retrieve.
        reindex (bool): Flag to reset the dataframe index or not.
    
    Returns:
        pd.DataFrame: Dataframe with a fraction of the original rows.
    
    Examples:
        >>> df = pd.DataFrame({"letters":["a","a","c"], "numbers":[1,2,3]})
        >>> df_return = get_random_fraction_of_rows(df, 0.3, False)
        >>> df_return.isin(df) #doctest: +ELLIPSIS
           letters  numbers
        ...   True     True
    """
    df_return = df.sample(frac=row_fraction)
    if reindex:
        df_return = df_return.reset_index(drop=True)
    return df_return


def get_random_number_of_rows(df, num_rows, reindex=True):
    """Get a random number of the dataframe rows.
    
    Args:
        df (pd.DataFrame): Dataframe.
        num_rows (int): Number of rows to retrieve.
        reindex (bool): Flag to reset the dataframe index or not.
    
    Returns:
        pd.DataFrame: Dataframe with a random number of the original rows.
    
    Examples:
        >>> df = pd.DataFrame({"letters":["a","a","c"], "numbers":[1,2,3]})
        >>> df_return = get_random_number_of_rows(df, 1, False)
        >>> df_return.isin(df) #doctest: +ELLIPSIS
           letters  numbers
        ...   True     True
    """
    df_return = df.sample(n=num_rows)
    if reindex:
        df_return = df_return.reset_index(drop=True)
    return df_return


def select_values_by_range(df, row_ini, row_end, col_ini, col_end):
    """Select a range of values in the dataframe.
    
    Args:
        df (pd.DataFrame): Dataframe.
        row_ini (int): Initial row.
        row_end (int): Final row.
        col_ini (int): Initial column.
        col_end (int): Final column.
    
    Returns:
        pd.DataFrame: Dataframe with the specific range of rows and columns.
    
    Examples:
        >>> df = pd.DataFrame({"letters":["a","a","c"], "numbers":[1,2,3]})
        >>> df_return = select_values_by_range(df, 0, 1, "letters", "numbers")
        >>> df_return
          letters  numbers
        0       a        1
        1       a        2
    """
    return df.loc[row_ini:row_end, col_ini:col_end]


def select_values_by_index(df, vector_row_pos, vector_col_pos):
    """Select values in the dataframe given specific indexes of rows and columns.
    
    Args:
        df (pd.DataFrame): Dataframe.
        vector_row_pos (array): Array of row positions.
        vector_col_pos (array): Array of column positions.
    
    Returns:
        pd.DataFrame: Dataframe with the specific values in the row and column indexes.
    
    Examples:
        >>> df = pd.DataFrame({"letters":["a","a","c"], "numbers":[1,2,3]})
        >>> df_return = select_values_by_index(df, vector_row_pos=[0,2], vector_col_pos=[0,1])
        >>> df_return
          letters  numbers
        0       a        1
        2       c        3
    """
    return df.iloc[vector_row_pos, vector_col_pos]


def select_rows_where_value_equal(df, column, value):
    """Select rows in the dataframe whose column has a specific value.
    
    Args:
        df (pd.DataFrame): Dataframe.
        column (str): Column name.
        value (int, str, float): Value to compare with.
    
    Returns:
        pd.DataFrame: Dataframe with selected rows.
    
    Examples:
        >>> df = pd.DataFrame({"letters":["a","a","c"], "numbers":[1,2,3]})
        >>> df_return = select_rows_where_value_equal(df, "letters", "a")
        >>> df_return
          letters  numbers
        0       a        1
        1       a        2
    """
    return df.loc[df[column] == value]


def select_rows_where_list_equal(df, column, items):
    """Select rows in the dataframe whose column has a list of values.
    
    Args:
        df (pd.DataFrame): Dataframe.
        column (str): Column name.
        items (list): List of items.
    
    Returns:
        pd.DataFrame: Dataframe with selected rows.
    
    Examples:
        >>> df = pd.DataFrame({"letters":["a","b","c"], "numbers":[1,2,3]})
        >>> df_return = select_rows_where_list_equal(df, "letters", ["a","b"])
        >>> df_return
          letters  numbers
        0       a        1
        1       b        2
    """
    return df.loc[df[column].isin(items)]


def select_all_columns_except_some(df, column_names):
    """Select all columns in the dataframe except those specified in ``column_list``.
    
    Args:
        df (pd.DataFrame): Dataframe.
        column_names (list): List of column names.
    
    Returns:
        pd.DataFrame: Dataframe with the columns removed.
    
    Examples:
        >>> df = pd.DataFrame({"letters":["a","b","c"], "numbers":[1,2,3], "numbers2":[4,5,6]})
        >>> df_return = select_all_columns_except_some(df, ["numbers","numbers2"])
        >>> df_return
          letters
        0       a
        1       b
        2       c
    """
    return df[df.columns.difference(column_names)]


def select_any_cols_where_operation_on_value(df, operation, value):
    """Select any columns greater, lower or equal than a value. 
    
    Args:
        df (pd.DataFrame): Dataframe.
        operation (str): Comparison operation i.e. ">", "<=", "=", etc.
        value (int, str, float): Value to compare with.

    Returns:
        pd.DataFrame: Dataframe with selected columns.

    Examples:
        >>> df = pd.DataFrame({"big_nums":[100, 200, 300], "numbers":[1,2,3]})
        >>> select_any_cols_where_operation_on_value(df, ">", 100)
           big_nums
        0       100
        1       200
        2       300
        >>> select_any_cols_where_operation_on_value(df, "<", 5)
           numbers
        0        1
        1        2
        2        3
    """
    comparison = {
        ">": operator.gt,
        "<": operator.lt,
        ">=": operator.ge,
        "<=": operator.le,
        "=": operator.eq,
    }
    # return df.loc[:,(df > value).any()]
    return df.loc[:, (comparison[operation](df, value)).any()]


def split_rows_by_condition(df, mask):
    """Split dataframe based on logical indexes (that could come from a condition).
    
    Args:
        df (pd.DataFrame): Dataframe.
        mask (pd.Series): Series with boolean indexes (could come from a condition).
    
    Returns:
        list: List of split dataframes.
    
    Examples:
        >>> df = pd.DataFrame({"letters":["a","b","c"], "numbers":[1,2,3], "numbers2":[4,5,6]})
        >>> mask = df["numbers"] > 1
        >>> df1, df2 = split_rows_by_condition(df, mask)
        >>> df1
          letters  numbers  numbers2
        1       b        2         5
        2       c        3         6
        >>> df2
          letters  numbers  numbers2
        0       a        1         4
    """
    df1 = df[mask]
    df2 = df[~mask]
    return df1, df2


def set_value_where_condition(df, value, col_val, value_cond1, col_cond1):
    """Set a value in a column where multiple conditions are fit
    
    Args:
        df (pd.DataFrame): Dataframe.
        value (int, float, str): Value to set.
        col_val (str): Column name for the set value
        value_cond1 (int, float, str): Value of the condition.
        col_cond1 (str): Column name for the condition.
    
    Returns:
        pd.DataFrame: Dataframe with the value modified.
    
    Examples:
        >>> df = pd.DataFrame({"letters":["a","b","c"], "numbers":[1,2,3], "numbers2":[4,5,6]})
        >>> df_return = set_value_where_condition(df, 10, "numbers2", "a", "letters")
        >>> df_return
          letters  numbers  numbers2
        0       a        1        10
        1       b        2         5
        2       c        3         6
    """
    df.loc[df[col_cond1] == value_cond1, col_val] = value
    return df


def set_value_where_multiple_condition(
    df, value, col_val, value_cond1, col_cond1, value_cond2, col_cond2
):
    """Set a value in a column where multiple conditions are fit
    
    Args:
        df (pd.DataFrame): Dataframe.
        value (int, float, str): Value to set.
        col_val (str): Column name for the set value
        value_cond1 (int, float, str): Value of the condition 1.
        col_cond1 (str): Column name for the condition 1.
        value_cond2 (int, float, str): Value of the condition 2.
        col_cond2 (str): Column name for the condition 2.
    
    Returns:
        pd.DataFrame: Dataframe with the value modified.
    
    Examples:
        >>> df = pd.DataFrame({"letters":["a","a","a"], "numbers":[1,2,3], "numbers2":[4,5,6]})
        >>> df_return = set_value_where_multiple_condition(df, 10, "numbers2", "a", "letters", 1, "numbers")
        >>> df_return
          letters  numbers  numbers2
        0       a        1        10
        1       a        2         5
        2       a        3         6
    """
    df.loc[
        (df[col_cond1] == value_cond1) & (df[col_cond2] == value_cond2), col_val
    ] = value
    return df


def intersection(df1, df2):
    """Intersection between two dataframes. It returns the common rows in both dataframes, without duplicates. 
    
    Args:
        df1 (pd.DataFrame): Dataframe.
        df2 (pd.DataFrame): Dataframe.
    
    Returns:
        pd.DataFrame: Intersection.

    Examples:
        >>> df1 = pd.DataFrame({"letters":["a","b","c","c"], "numbers":[1,2,3,3]})
        >>> df2 = pd.DataFrame({"letters":["b","c"], "numbers":[2,3]})
        >>> intersection(df1, df2)
          letters  numbers
        0       b        2
        1       c        3

    """
    return pd.merge(df1, df2, how="inner").drop_duplicates()


def symmetric_difference(df1, df2):
    """Symmetric difference between two dataframes. It returns the rows in either one dataframe or the other, but 
    not both.
    
    Args:
        df1 (pd.DataFrame): Dataframe.
        df2 (pd.DataFrame): Dataframe.
    
    Returns:
        pd.DataFrame, pd.DataFrame: Two dataframes with the symmetric difference. The first dataframe contains
        the rows in df1 but not in df2, and the opposite for the second dataframe.

    Examples:
        >>> df1 = pd.DataFrame({"letters": ["a", "b", "c", "c"], "numbers": [1, 2, 3, 3]})
        >>> df2 = pd.DataFrame({"letters": ["b", "c", "d"], "numbers": [2, 3, 4]})
        >>> df_left, df_right = symmetric_difference(df1, df2)
        >>> df_left
          letters  numbers
        0       a        1
        >>> df_right
          letters  numbers
        0       d        4
    """
    merge_left = pd.merge(df1, df2, how="left", indicator=True)
    merge_right = pd.merge(df1, df2, how="right", indicator=True)
    df_left = (
        merge_left[merge_left["_merge"] == "left_only"]
        .drop(["_merge"], axis=1)
        .drop_duplicates()
        .reset_index(drop=True)
    )
    df_right = (
        merge_right[merge_right["_merge"] == "right_only"]
        .drop(["_merge"], axis=1)
        .drop_duplicates()
        .reset_index(drop=True)
    )
    return df_left, df_right

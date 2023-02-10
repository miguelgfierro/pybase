# Cheatsheet: https://github.com/FavioVazquez/ds-cheatsheets/blob/master/Big_Data/pyspark_df.pdf


try:
    from pyspark.sql import functions as F
except ImportError:
    pass  # so the environment without spark doesn't break


def get_unique_values_in_column(df, col_name):
    """Get unique values in a column.
    
    Args:
        df (spark.DataFrame): Dataframe.
        col_name (str): Column name.
    
    Returns:
        spark.DataFrame: Unique values.
        
    **Examples**

        .. code-block:: python
        
            df = spark.createDataFrame([("a", 1), ("a", 2), ("c", 3)], ["letters", "numbers"])
            get_unique_values_in_column(df, "letters") 
            # [Row(letters='c'), Row(letters='a')]

    """
    return df.select(col_name).distinct().collect()


def count_unique_values_in_column(df, col_name):
    """Get unique values in a column.
    
    Args:
        df (spark.DataFrame): Dataframe.
        col_name (str): Column name.
    
    Returns:
        spark.DataFrame: Unique values.
    
    **Examples**

        .. code-block:: python
        
            df = spark.createDataFrame([("a", 1), ("a", 2), ("c", 3)], ["letters", "numbers"])
            count_unique_values_in_column(df, "letters")
            # [Row(count(DISTINCT letters)=2)]
    """
    return df.select(F.countDistinct(col_name)).collect()


def get_maximum_value_of_column(df, col_name):
    """Get the maximum value of a colum.
    
    Args:
        df (spark.DataFrame): Dataframe.
        col_name (str): Column name.

    Return:
        int, float, date: Maximum value.
        
    **Examples**

        .. code-block:: python
            from datetime import date
            df = spark.createDataFrame([(1, date(2022,1,6)), (2, date(2023,1,1))], ["numbers", "dates"])
            get_maximum_value_of_column(df, "dates")
            # 2023-01-01
    """
    return df.agg(F.max(df[col_name])).collect()[0][0]


def get_minimum_value_of_column(df, col_name):
    """Get the minimum value of a colum.
    
    Args:
        df (spark.DataFrame): Dataframe.
        col_name (str): Column name.

    Return:
        int, float, date: Maximum value.
        
    **Examples**

        .. code-block:: python
            from datetime import date
            df = spark.createDataFrame([(1, date(2022,1,6)), (2, date(2023,1,1))], ["numbers", "dates"])
            get_maximum_value_of_column(df, "dates")
            # 2023-01-01
    """
    return df.agg(F.min(df[col_name])).collect()[0][0]


def get_random_fraction_of_rows(df, row_fraction=0.5, reindex=True):
    pass


def get_random_number_of_rows(df, num_rows, reindex=True):
    pass


def select_values_by_range(df, row_ini, row_end, col_ini, col_end):
    pass


def select_values_by_index(df, vector_row_pos, vector_col_pos):
    pass


def select_rows_where_value_equal(df, column, value):
    pass


def select_rows_where_list_equal(df, column, items):
    pass


def select_all_columns_except_some(df, column_names):
    pass


def select_any_cols_where_operation_on_value(df, operation, value):
    pass


def select_all_cols_where_operation_on_value(df, operation, value):
    pass


def select_cols_with_nan(df):
    pass


def select_cols_without_nan(df):
    pass


def split_rows_by_condition(df, mask):
    pass


def set_value_where_condition(df, value, col_val, value_cond1, col_cond1):
    pass


def set_value_where_multiple_condition(
    df, value, col_val, value_cond1, col_cond1, value_cond2, col_cond2
):
    pass


def intersection(df1, df2):
    pass


def symmetric_difference(df1, df2):
    pass

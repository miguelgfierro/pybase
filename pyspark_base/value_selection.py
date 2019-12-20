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
    
    Examples:
        >>> df = spark.createDataFrame([("a", 1), ("a", 2), ("c", 3)], ["letters", "numbers"])
        >>> get_unique_values_in_column(df, "letters")
        [Row(letters='c'), Row(letters='a')]
    """
    return df.select(col_name).distinct().collect()

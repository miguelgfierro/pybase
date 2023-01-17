import pyspark.sql.functions as F


def replace_column_values(df, to_replace, value, col_name, new_col_name=None):
    """
    Replace all appearances of a value to another in a dictionary.

    Args:
        df (_type_): _description_
        val_dict (_type_): _description_
        col_name (_type_): _description_
        new_col_name (_type_, optional): _description_. Defaults to None.

    Examples:
        >>> df = spark.createDataFrame([("a", 1), ("a", 2), ("c", 3)], ["letters", "numbers"])
        >>> df_return = replace_column_values(df, "a", 1, "letters")
        >>> df_return.toPandas()
          letters  numbers
        0       1        1
        1       1        2
        2       c        3
    """
    if new_col_name is None:
        output_col = col_name
    else:
        output_col = new_col_name

    if to_replace is None:
        query = F.isnull(col_name)
    elif to_replace != to_replace: # Fastest way to check for NaN https://stackoverflow.com/a/62171968 
        query = F.isnan(col_name)
    else:
        query = F.col(col_name) == to_replace

    return df.withColumn(output_col, F.when(query, value).otherwise(F.col(output_col)))


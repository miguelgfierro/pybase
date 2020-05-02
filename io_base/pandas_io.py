import pandas as pd
from sqlalchemy import create_engine


def save_csv(dataframe, filename, **kwargs):
    """Save a dataframe as csv.
    
    Args:
        dataframe (pd.DataFrame): A dataframe
        filename (str): Name of the file.
    
    Examples:
        >>> df = pd.DataFrame({"col1":[1,2,3], "col2":[0.1,0.2,0.3]})
        >>> save_csv(df, filename="file.csv", index=False, header=False)
        >>> os.path.isfile('file.csv')
        True
        >>> os.remove('file.csv')
        >>> os.path.isfile('file.csv')
        False
    """
    dataframe.to_csv(filename, **kwargs)


def read_csv(filename, **kwargs):
    """Read a csv file with pandas.
    
    Args:
        filename (str): Name of the file.
    
    Returns:
        pd.DataFrame: A dataframe.
    
    Examples:
        >>> df = read_csv(filename="share/traj.csv", header=None,
        ...                names=["time","q1","q2"], sep=",", usecols=[0,1,2])
        >>> df
               time   q1   q2
        0  0.041667  443  205
        1  0.083333  444  206
        >>> df = read_csv(filename="share/traj_header.csv", usecols=["t","q0"])
        >>> df
                  t   q0
        0  0.041667  443
        1  0.083333  444
        >>> df.dtypes
        t     float64
        q0      int64
        dtype: object
        >>> df = read_csv(filename="share/traj_header.csv", dtype={"t": str, "q0":float})
        >>> df.dtypes
        t      object
        q0    float64
        q1      int64
        dtype: object
        >>> ff = lambda x: float(x[:5]) # NOTE: that the data is read as str, and then it can be transformed to float
        >>> df = read_csv(filename="share/traj_header.csv", converters={"t":ff})
        >>> df
               t   q0   q1
        0  0.041  443  205
        1  0.083  444  206
    """
    return pd.read_csv(filename, **kwargs)


def save_to_sqlite(dataframe, database, table_name, **kargs):
    """Save a dataframe to a SQL database.
    
    Args:
        dataframe (pd.DataFrame): A dataframe
        database (str): Database filename.
        table_name (str): Table name
    
    Examples:
        >>> df = pd.DataFrame({"col1":[1,2,3], "col2":[0.1,0.2,0.3]})
        >>> save_to_sqlite(df, "pandas.db", "table1", if_exists="replace")
        >>> import sqlite3
        >>> conn = sqlite3.connect("pandas.db")
        >>> cur = conn.cursor()
        >>> result = cur.execute("SELECT * FROM table1")
        >>> cur.fetchall()
        [(0, 1, 0.1), (1, 2, 0.2), (2, 3, 0.3)]
        >>> save_to_sqlite(df, "pandas.db", "table1", if_exists="append", index=False)
        >>> result = cur.execute("SELECT * FROM table1")
        >>> cur.fetchall()
        [(0, 1, 0.1), (1, 2, 0.2), (2, 3, 0.3), (None, 1, 0.1), (None, 2, 0.2), (None, 3, 0.3)]
    """
    connection_string = "sqlite:///" + database
    engine = create_engine(connection_string)
    dataframe.to_sql(table_name, engine, **kargs)


def read_from_sqlite(database, query, **kargs):
    """Make a query to a SQL database.
    
    Args:
        database (str): Database filename.
        query (str): Query.
    
    Returns:
        pd.DataFrame: A dataframe.
    
    Examples:
        >>> df = read_from_sqlite("share/pandas.db", "SELECT col1,col2 FROM table1;")
        >>> df
           col1  col2
        0     1   0.1
        1     2   0.2
        2     3   0.3
        3     1   0.1
        4     2   0.2
        5     3   0.3
    """
    connection_string = "sqlite:///" + database
    engine = create_engine(connection_string)
    return pd.read_sql(query, engine, **kargs)

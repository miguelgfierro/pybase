import pyodbc
import datetime


def insert_row(cursor, connector, table_name, value1, value2):
    """Insert a row of items in a table.
    
    Args:
        cursor (object): pyobdc cursor.
        connector (object): pyodbc connector.
        table_name (str): Table name.
        value1 (str or int): Value to insert.
        value2 (datetime.py): Value to insert.
    
    Examples:
        >>> conn = pyodbc.connect(connection_string) #doctest: +SKIP
        >>> cur = conn.cursor() #doctest: +SKIP
        >>> insert_row(cur, conn, tab_name, "item1", datetime.datetime.now()) #doctest: +SKIP
    """
    query = "INSERT INTO " + table_name + "( name, date ) VALUES (?,?)"
    cursor.execute(query, value1, value2)
    connector.commit()


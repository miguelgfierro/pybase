if __name__ == "__main__":
    df = spark.createDataFrame([("a", 1), ("a", 2), ("c", 3)], ["letters", "numbers"])
    print("(rows, columns)={}".format((df.count(), len(df.columns)))) # (rows, columns)=(3,2)

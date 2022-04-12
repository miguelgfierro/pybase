import os

try:
    from pyspark.sql import SparkSession
except ImportError:
    pass  # so the environment without spark doesn't break


def spark(
    app_name="App",
    url="local[*]",
    memory="16g",
    config=None,
    packages=None,
    jars=None,
    repository=None,
):
    """Start Spark if not started

    Args:
        app_name (str): Set name of the application
        url (str): URL for spark master
        memory (str): Size of memory for spark driver
        config (dict): dictionary of configuration options
        packages (list): list of packages to install
        jars (list): list of jar files to add
        repository (str): The maven repository

    Returns:
        obj: Spark context.

    **Examples**::

        >> config = {"spark.executor.cores": "8"}
        >> config.update({"spark.executor.memory": "16g"})
        >> config.update({"spark.memory.fraction": "0.9"})
        >> config.update({"spark.memory.stageFraction": "0.3"})
        >> config.update({"spark.executor.instances": 1})
        >> config.update({"spark.executor.heartbeatInterval": "36000s"})
        >> config.update({"spark.network.timeout": "10000000s"})
        >> config.update({"spark.driver.maxResultSize": "50g"})
        >> spark = spark(config=config) # doctest: +SKIP
        >> spark is not None
        True
    """

    submit_args = ""
    if packages is not None:
        submit_args = "--packages {} ".format(",".join(packages))
    if jars is not None:
        for jar in jars:
            if not os.path.isfile(jar):
                raise FileNotFoundError("{} not found".format(jar))
        submit_args += "--jars {} ".format(",".join(jars))
    if repository is not None:
        submit_args += "--repositories {}".format(repository)
    if submit_args:
        os.environ["PYSPARK_SUBMIT_ARGS"] = "{} pyspark-shell".format(submit_args)

    spark_opts = [
        'SparkSession.builder.appName("{}")'.format(app_name),
        'master("{}")'.format(url),
    ]

    if config is not None:
        for key, raw_value in config.items():
            value = (
                '"{}"'.format(raw_value) if isinstance(raw_value, str) else raw_value
            )
            spark_opts.append('config("{key}", {value})'.format(key=key, value=value))

    if config is None or "spark.driver.memory" not in config:
        spark_opts.append('config("spark.driver.memory", "{}")'.format(memory))

    spark_opts.append("getOrCreate()")
    return eval(".".join(spark_opts))

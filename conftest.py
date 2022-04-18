import os
import sys
import pytest
import numpy
import pandas
import subprocess
import glob
import json
import shutil
from collections import Counter
from collections import OrderedDict
from skimage import io
from tempfile import TemporaryDirectory


try:
    from pyspark.sql import SparkSession
except ImportError:
    pass  # so the environment without spark doesn't break


@pytest.fixture(autouse=True)
def add_libraries(doctest_namespace):
    """Definition of doctest namespace.

    See `more information <https://docs.pytest.org/en/latest/doctest.html#the-doctest-namespace-fixture>`
    """
    doctest_namespace["os"] = os
    doctest_namespace["sys"] = sys
    doctest_namespace["np"] = numpy
    doctest_namespace["pd"] = pandas
    doctest_namespace["subprocess"] = subprocess
    doctest_namespace["glob"] = glob
    doctest_namespace["json"] = json
    doctest_namespace["shutil"] = shutil
    doctest_namespace["Counter"] = Counter
    doctest_namespace["OrderedDict"] = OrderedDict
    doctest_namespace["io"] = io
    doctest_namespace["TemporaryDirectory"] = TemporaryDirectory
    try:
        spark = (
            SparkSession.builder.appName("test pybase")
            .master("local[*]")
            .config("spark.driver.memory", "4g")
            .getOrCreate()
        )
    except NameError:
        spark = None
    doctest_namespace["spark"] = spark

import os
import sys
import pytest

sys.path.append(os.path.join(".."))  # import pybase
from pybase.notebooks.notebook_utils import execute_notebook, read_notebook


def test_notebook_execution_int():
    input_notebook = os.path.join("test", "programmatic_notebook_execution.ipynb")
    execute_notebook(
        input_notebook,
        "output.ipynb",
        kernel_name="python3",
        parameters=dict(a=5),
    )

    results = read_notebook("output.ipynb")
    assert results["response1"] == 6

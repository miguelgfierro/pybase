import os
import sys
import pytest


sys.path.append(os.path.join(".."))  # import pybase
from pybase.notebooks.notebook_utils import execute_notebook, read_notebook


@pytest.fixture
def input_notebook():
    return os.path.join("test", "programmatic_notebook_execution.ipynb")


def test_notebook_execution_int(input_notebook):
    execute_notebook(
        input_notebook,
        "output.ipynb",
        kernel_name="python3",
        parameters=dict(a=5),
    )

    results = read_notebook("output.ipynb")
    assert results["response1"] == 7


def test_notebook_execution_letter(input_notebook):
    execute_notebook(
        input_notebook,
        "output.ipynb",
        kernel_name="python3",
        parameters=dict(b="M"),
    )

    results = read_notebook("output.ipynb")
    assert results["response2"] is True

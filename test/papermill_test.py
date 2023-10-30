import sys
import pytest
import papermill as pm
import scrapbook as sb


INPUT_NOTEBOOK = "test/papermill_notebook.ipynb"
OUTPUT_NOTEBOOK = "output.ipynb"


@pytest.mark.skipif(
    sys.platform == "win32", reason="got a papermill internal error in windows"
)
@pytest.mark.skipif(
    sys.version_info >= (3, 10), reason="Scrapbook does not support Python 3.10+"
)
def test_notebook_runs():
    pm.execute_notebook(
        INPUT_NOTEBOOK,
        OUTPUT_NOTEBOOK,
        kernel_name="python3",
        parameters=dict(version=sb.__version__, integer=10),
    )
    results = sb.read_notebook(OUTPUT_NOTEBOOK).scraps.dataframe.set_index("name")[
        "data"
    ]
    assert results["result"] == 15
    assert results["checked_version"] is True


def test_notebook_fails():
    with pytest.raises(Exception):
        pm.execute_notebook(
            INPUT_NOTEBOOK, OUTPUT_NOTEBOOK, parameters=dict(version="0.1", integer=10)
        )

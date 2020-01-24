[![Issues](https://img.shields.io/github/issues/miguelgfierro/pybase.svg)](https://github.com/miguelgfierro/pybase/issues)
[![Commits](https://img.shields.io/github/commit-activity/y/miguelgfierro/pybase.svg)](https://github.com/miguelgfierro/pybase/commits/master)
[![Last commit](https://img.shields.io/github/last-commit/miguelgfierro/pybase.svg)](https://github.com/miguelgfierro/pybase/commits/master)


# Python pybase

This is a codebase for basic python utilities.

## Dependencies

To install the dependencies on a conda environment named `pybase`:

    conda env create -n pybase -f conda.yaml

Make sure Java and Spark are available in the machine. Then, we need to set the environment variables `PYSPARK_PYTHON` and `PYSPARK_DRIVER_PYTHON` to point to the conda python executable.

<details>
<summary><strong><em>Press to get the instructions for installing PySpark on Linux or MacOS</em></strong></summary>



</details>

<details>
<summary><strong><em>Press to get the instructions for installing PySpark on Windows</em></strong></summary>


</details>

## Configuration

To be able to run the test in [blob_io.py](python/io_base/blob_io.py), add the correct credentials after renaming the template:

    cp share/blob_config_template.json share/blob_config.json

## Doctests

To execute the tests:

    pytest --doctest-modules --continue-on-collection-errors

To execute coverage and see the report:

    coverage run playground.py
    coverage report

To see more details on the result, the following command will generate a web where the coverage details can be examined line by line:

    coverage html

To handle variable outputs in doctest you need to add at the end of the execution line `#doctest: +ELLIPSIS` and substitude the variable output with `...`
An example can be found in the file [timer.py](python/log_base/timer.py).

Original:

    >>> "Time elapsed {}".format(t)
    'Time elapsed 0:00:1.9875734'

With ellipsis:

    >>> "Time elapsed {}".format(t) # doctest: +ELLIPSIS
    'Time elapsed 0:00:...'

To skip a test, one can also add: `# doctest: +SKIP`.

To handle [exceptions](https://docs.python.org/2.4/lib/doctest-exceptions.html), you can just add the `Traceback` info, then `...` and then the exception:

    >>> raise ValueError("Something bad happened")
    Traceback (most recent call last):
        ...
    ValueError: "Something bad happened"

To execute a context manager with doctests:

    >>> with TemporaryDirectory() as td:
    ...     print(td.name)

## Documentation

For the documentation, I'm using the [Google Style](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

To add a code block that can be rendered with sphinx: 

```
.. code-block:: python

    import sys
    print(sys.executable) 
```

This is equivalent, [having the python syntax](https://pythonhosted.org/an_example_pypi_project/sphinx.html#code):

```
Code::

    import sys
    print(sys.executable)

```

To add a note:

```
.. note::

    This is a note
```

or

```
Note:
    This is a note
```

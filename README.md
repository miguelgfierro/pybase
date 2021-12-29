[![Issues](https://img.shields.io/github/issues/miguelgfierro/pybase.svg)](https://github.com/miguelgfierro/pybase/issues)
[![Commits](https://img.shields.io/github/commit-activity/y/miguelgfierro/pybase.svg?color=success)](https://github.com/miguelgfierro/pybase/commits/master)
[![Last commit](https://img.shields.io/github/last-commit/miguelgfierro/pybase.svg)](https://github.com/miguelgfierro/pybase/commits/master)
[![Code style:black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Python 3.5+supported](https://img.shields.io/badge/python-3.5+-blue.svg)](https://www.python.org/downloads/release/python-350/)
[![Lines of code](https://tokei.rs/b1/github/miguelgfierro/pybase)](https://github.com/miguelgfierro/pybase/graphs/contributors)
[![Files](https://tokei.rs/b1/github/miguelgfierro/pybase?category=files)](https://github.com/miguelgfierro/pybase/graphs/contributors)

[![Linkedin](https://img.shields.io/badge/Linkedin-Follow%20Miguel-blue?logo=linkedin)](https://www.linkedin.com/in/miguelgfierro/)
[![Blog](https://img.shields.io/badge/Blog-Visit%20miguelgfierro.com-blue.svg)](https://miguelgfierro.com)

# Python pybase

This is a codebase for basic python utilities.

## Dependencies

To install the dependencies on a conda environment named `pybase`:

    conda env create -n pybase -f conda.yaml

For setting up PySpark, make sure Java and Spark are available in the machine. Then, we need to set the environment variables `PYSPARK_PYTHON` and `PYSPARK_DRIVER_PYTHON` to point to the conda python executable.

<details>
<summary><strong><em>Press to get the instructions for PySpark on Linux or MacOS</em></strong></summary>

To set these variables every time the environment is activated, we can follow the steps of this [guide](https://conda.io/docs/user-guide/tasks/manage-environments.html#macos-and-linux). First, get the path of the environment `pybase` is installed:

    CONDA_ENV=$(conda env list | grep pybase | awk '{print $NF}')

Then, create the file `$CONDA_ENV/etc/conda/activate.d/env_vars.sh` and add:

    #!/bin/sh
    CONDA_ENV=$(conda env list | grep pybase | awk '{print $NF}')
    export PYSPARK_PYTHON=$CONDA_ENV/bin/python
    export PYSPARK_DRIVER_PYTHON=$CONDA_ENV/bin/python
    export SPARK_HOME_BACKUP=$SPARK_HOME
    export SPARK_HOME=/home/root/installer/spark

This will export the variables every time we do `conda activate pybase`.
To unset these variables when we deactivate the environment,
create the file `$CONDA_ENV/etc/conda/deactivate.d/env_vars.sh` and add:

    #!/bin/sh
    unset PYSPARK_PYTHON
    unset PYSPARK_DRIVER_PYTHON
    export SPARK_HOME=$SPARK_HOME_BACKUP
    unset SPARK_HOME_BACKUP

</details>

<details>
<summary><strong><em>Press to get the instructions for PySpark on Windows</em></strong></summary>

To set these variables every time the environment is activated, we can follow the steps of this [guide](https://conda.io/docs/user-guide/tasks/manage-environments.html#windows). First, get the path of the environment `pybase` is installed:

    for /f "delims=" %A in ('conda env list ^| grep pybase ^| awk "{print $NF}"') do set "CONDA_ENV=%A"

Then, create the file `%CONDA_ENV%\etc\conda\activate.d\env_vars.bat` and add:
 
    @echo off
    for /f "delims=" %%A in ('conda env list ^| grep pybase ^| awk "{print $NF}"') do set "CONDA_ENV=%%A"
    set PYSPARK_PYTHON=%CONDA_ENV%\python.exe
    set PYSPARK_DRIVER_PYTHON=%CONDA_ENV%\python.exe
    set SPARK_HOME_BACKUP=%SPARK_HOME%
    set SPARK_HOME=
    set PYTHONPATH_BACKUP=%PYTHONPATH%
    set PYTHONPATH=

This will export the variables every time we do `conda activate pybase`.
To unset these variables when we deactivate the environment,
create the file `%CONDA_ENV%\etc\conda\deactivate.d\env_vars.bat` and add:

    @echo off
    set PYSPARK_PYTHON=
    set PYSPARK_DRIVER_PYTHON=
    set SPARK_HOME=%SPARK_HOME_BACKUP%
    set SPARK_HOME_BACKUP=
    set PYTHONPATH=%PYTHONPATH_BACKUP%
    set PYTHONPATH_BACKUP=

See more details on how to install PySpark on Windows [here](https://towardsdatascience.com/installing-apache-pyspark-on-windows-10-f5f0c506bea1).

</details>

<details>
<summary><strong><em>Press to get the instructions for CUDA and CuDNN on Linux or MacOS</em></strong></summary>

**TODO**

</details>


<details>
<summary><strong><em>Press to get the instructions for CUDA and CuDNN on Windows</em></strong></summary>

1. Check the capability of your GPU [here](https://developer.nvidia.com/cuda-gpus).
1. Select the version of CUDA toolkit you want to [download](https://developer.nvidia.com/cuda-toolkit-archive). The latest version can be found [here](https://developer.nvidia.com/cuda-downloads).
1. Download the corresponding CuDNN based on the CUDA version [here](https://developer.nvidia.com/rdp/cudnn-download).
1. Copy three files from the unzipped directory to CUDA X.X install location. For reference, NVIDIA team has put them in their own directory. So all you have to do is to copy file from :
    * {unzipped dir}/bin/ --> C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\vX.X\bin
    * {unzipped dir}/include/ --> C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\vX.X\include
    * {unzipped dir}/lib/ --> C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\vX.X\lib

See the full installation guide [here](https://medium.com/@akshaysin_86681/installing-cuda-and-cudnn-on-windows-10-f735585159f7).

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

[![Issues](https://img.shields.io/github/issues/miguelgfierro/pybase.svg)](https://github.com/miguelgfierro/pybase/issues)
[![Commits](https://img.shields.io/github/commit-activity/y/miguelgfierro/pybase.svg?color=success)](https://github.com/miguelgfierro/pybase/commits/master)
[![Last commit](https://img.shields.io/github/last-commit/miguelgfierro/pybase.svg)](https://github.com/miguelgfierro/pybase/commits/master)
[![Code style:black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Python 3.7+supported](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-370/)

[![Linkedin](https://img.shields.io/badge/Linkedin-Follow%20Miguel-blue?logo=linkedin)](https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=miguelgfierro)
[![Blog](https://img.shields.io/badge/Blog-Visit%20miguelgfierro.com-blue.svg)](https://miguelgfierro.com?utm_source=github&utm_medium=profile&utm_campaign=pybase)

# Python pybase

This is a codebase for basic Python utilities.

## Dependencies

We recommend using [uv](https://docs.astral.sh/uv/) for environment management (10-100x faster than pip/conda).

To install uv and set up the environment:

    # Install uv
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # Create and activate environment
    uv venv ~/.venvs/pybase --python 3.11
    source ~/.venvs/pybase/bin/activate

    # Install dependencies
    uv pip install -r requirements.txt

<details>
<summary><strong><em>Press to get the instructions for PySpark on Linux or MacOS</em></strong></summary>

For PySpark, make sure Java is installed. We recommend Temurin JDK 21:

    # Install Java (Ubuntu/Debian)
    sudo apt install -y wget apt-transport-https gpg
    wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | sudo gpg --dearmor -o /usr/share/keyrings/adoptium.gpg
    echo "deb [signed-by=/usr/share/keyrings/adoptium.gpg] https://packages.adoptium.net/artifactory/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/adoptium.list
    sudo apt update && sudo apt install -y temurin-21-jdk

Set the environment variables. Add to `~/.bashrc`:

    export JAVA_HOME=/usr/lib/jvm/temurin-21-jdk-amd64
    export PYSPARK_PYTHON=~/.venvs/pybase/bin/python
    export PYSPARK_DRIVER_PYTHON=~/.venvs/pybase/bin/python

Then reload:

    source ~/.bashrc

</details>

<details>
<summary><strong><em>Press to get the instructions for PySpark on Windows</em></strong></summary>

1. Install Java (download Temurin JDK from https://adoptium.net/)
2. Set environment variables in System Properties > Environment Variables:
   - `JAVA_HOME` = `C:\Program Files\Eclipse Adoptium\jdk-21...`
   - `PYSPARK_PYTHON` = `%USERPROFILE%\.venvs\pybase\Scripts\python.exe`
   - `PYSPARK_DRIVER_PYTHON` = `%USERPROFILE%\.venvs\pybase\Scripts\python.exe`

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

## Doctests

To execute the tests:

    pytest --doctest-modules --continue-on-collection-errors --durations 0 --disable-warnings

To execute coverage and see the report:

    coverage run playground.py
    coverage report

To see more details on the result, the following command will generate a web where the coverage details can be examined line by line:

    coverage html

To handle variable outputs in doctest you need to add at the end of the execution line `#doctest: +ELLIPSIS` and substitute the variable output with `...`
An example can be found in the file [timer.py](log_base/timer.py).

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

## Install libraries with different Python versions

In the requirements.txt file, you can specify the Python version for each library. For example:

    dask[dataframe]>=0.17.1;python_version=='3.6'
    dask>=0.17.1;python_version>='3.7'
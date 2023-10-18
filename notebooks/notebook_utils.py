import re
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from IPython.display import display


def execute_notebook(
    input_notebook, output_notebook, parameters, kernel_name="python3", timeout=600
):
    """Execute a notebook while passing parameters to it.

    .. note::

    Ensure your Jupyter Notebook is set up with parameters that can be
    modified and read. Use Markdown cells to specify parameters that need
    modification and code cells to set parameters that need to be read.

    Args:
        input_notebook (str): Path to the input notebook.
        output_notebook (str): Path to the output notebook
        parameters (dict): Dictionary of parameters to pass to the notebook.
        kernel_name (str): Kernel name.
        timeout (int): Timeout (in seconds) for each cell to execute.
    """

    # Load the Jupyter Notebook
    with open(input_notebook, "r") as notebook_file:
        notebook_content = nbformat.read(notebook_file, as_version=4)

    # Search for and replace parameter values in code cells
    for cell in notebook_content.cells:
        if (
            "tags" in cell.metadata
            and "parameters" in cell.metadata["tags"]
            and cell.cell_type == "code"
        ):
            cell_source = cell.source
            modified_cell_source = (
                cell_source  # Initialize a variable to hold the modified source
            )
            for param, new_value in parameters.items():
                # Check if the new value is a string and surround it with quotes if necessary
                if isinstance(new_value, str):
                    new_value = f'"{new_value}"'
                # Define a regular expression pattern to match parameter assignments
                pattern = re.compile(rf"\b{param}\s*=\s*([^#\n]+)(?:\n|$)")
                matches = re.findall(pattern, cell_source)
                for match in matches:
                    old_assignment = match.strip()
                    modified_cell_source = modified_cell_source.replace(
                        old_assignment, f"{new_value}"
                    )
            # Update the cell's source within notebook_content
            cell.source = modified_cell_source

    # Create an execution preprocessor
    execute_preprocessor = ExecutePreprocessor(timeout=timeout, kernel_name=kernel_name)

    # Execute the notebook
    executed_notebook, _ = execute_preprocessor.preprocess(
        notebook_content, {"metadata": {"path": "./"}}
    )

    # Save the executed notebook
    with open(output_notebook, "w", encoding="utf-8") as executed_notebook_file:
        nbformat.write(executed_notebook, executed_notebook_file)


def store_metadata(name, value):
    """Store data in the notebook's output source code.
    This function is similar to snapbook.glue().

    Args:
        name (str): Name of the data.
        value (int,float,str): Value of the data.
    """

    metadata = {"notebook_utils": {"name": name, "data": True, "display": False}}
    data_json = {
        "application/notebook_utils.json+json": {
            "name": name,
            "data": value,
            "encoder": "json",
        }
    }
    display(data_json, metadata=metadata, raw=True)


def read_notebook(path):
    """Read the metadata stored in the notebook's output source code.
    This function is similar to snapbook.read_notebook().

    Args:
        path (str): Path to the notebook.

    Returns:
        dict: Dictionary of data stored in the notebook.
    """
    # Load the Jupyter Notebook
    with open(path, "r") as notebook_file:
        notebook_content = nbformat.read(notebook_file, as_version=4)

    # Search for and replace parameter values in code cells
    results = {}
    for cell in notebook_content.cells:
        if cell.cell_type == "code" and "outputs" in cell:
            for outputs in cell.outputs:
                if "metadata" in outputs and "notebook_utils" in outputs.metadata:
                    name = outputs.data["application/notebook_utils.json+json"]["name"]
                    data = outputs.data["application/notebook_utils.json+json"]["data"]
                    results[name] = data
    return results

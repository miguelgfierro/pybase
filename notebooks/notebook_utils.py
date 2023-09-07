import re
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def execute_notebook(
    input_notebook, output_notebook, parameters, kernel_name="python3", timeout=600
):
    """Execute a notebook while passing parameters to it.

    .. note:: Ensure your Jupyter Notebook is set up with parameters that can be
    modified and read. Use Markdown cells to specify parameters that need
    modification and code cells to set parameters that need to be read.

    Args:
        input_notebook (string): Path to the input notebook.
        output_notebook (string): Path to the output notebook
        parameters (dict): Dictionary of parameters to pass to the notebook.
        kernel_name (string): Kernel name.
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

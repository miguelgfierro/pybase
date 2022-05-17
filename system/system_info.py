import os
import sys
import glob
from functools import lru_cache
import pkg_resources
import importlib
import socket
import numpy as np
from psutil import virtual_memory


def get_os():
    """Get OS name.

    .. note::

        darwin: Mac.
        linux: Linux.
        Win32: Windows.

    Returns:
        str: OS name.

    Examples:
        >>> get_os() #doctest: +ELLIPSIS
        '...'

    """
    return sys.platform


def get_machine_name():
    """Get the machine's name

    Returns:
        str: Name of the machine

    Examples:
        >>> get_machine_name() #doctest: +ELLIPSIS
        '...'

    """
    return socket.gethostname()


def get_python_version():
    """Get the system's python version.

    Returns:
        str: Python version.

    Examples:
        >>> get_python_version() #doctest: +ELLIPSIS
        '...'

    """
    return sys.version


@lru_cache()
def get_library_version(library_name):
    """Get the version of a library.

    Args:
        library_name (str): Name of the library.

    Returns:
        str: Version of the library.

    Examples:
        >>> get_library_version("pandas") #doctest: +ELLIPSIS
        '1...'

    """
    try:
        version = pkg_resources.get_distribution(library_name).version
    except Exception:
        try:
            lib = importlib.import_module(library_name)
            version = lib.__version__
        except AttributeError as e:
            version = "Could not find the version"
    return version


def get_number_processors():
    """Get the number of processors in a CPU.

    Returns:
        int: Number of processors.

    Examples:
        >>> num = get_number_processors()
        >>> num >= 2
        True

    """
    try:
        num = os.cpu_count()
    except Exception:
        import multiprocessing  # force exception in case mutiprocessing is not installed

        num = multiprocessing.cpu_count()
    return num


def get_java_version():
    """Get java version, vendor, installation files and more information

    Examples:
        >>> get_java_version() # doctest: +SKIP
        java version "1.8.0_151"
        Java(TM) SE Runtime Environment (build 1.8.0_151-b12)
        Java HotSpot(TM) 64-Bit Server VM (build 25.151-b12, mixed mode)

    """
    os.system("java -version")


def get_blas_version():
    """Shows BLAS version of MKL, OpenBLAS, ATLAS and LAPACK libraries.

    Returns:
        str: BLAS info.

    **Examples**::

        >> get_blas_version()
        openblas_info:
            library_dirs = ['/home/travis/miniconda/envs/codebase/lib']
            language = c
            define_macros = [('HAVE_CBLAS', None)]
            libraries = ['openblas', 'openblas']
        openblas_lapack_info:
            library_dirs = ['/home/travis/miniconda/envs/codebase/lib']
            language = c
            define_macros = [('HAVE_CBLAS', None)]
            libraries = ['openblas', 'openblas']
        blis_info:
            NOT AVAILABLE
        lapack_mkl_info:
            NOT AVAILABLE
        lapack_opt_info:
            library_dirs = ['/home/travis/miniconda/envs/codebase/lib']
            language = c
            define_macros = [('HAVE_CBLAS', None)]
            libraries = ['openblas', 'openblas']
        blas_opt_info:
            library_dirs = ['/home/travis/miniconda/envs/codebase/lib']
            language = c
            define_macros = [('HAVE_CBLAS', None)]
            libraries = ['openblas', 'openblas']
        blas_mkl_info:
            NOT AVAILABLE

    """
    return np.__config__.show()


def get_gpu_name():
    """Get the GPU names in the system.

    Returns:
        list: List of strings with the GPU name.

    Examples:
        >>> get_gpu_name() #doctest: +SKIP
        ['Tesla P100-PCIE-16GB']

    """
    try:
        import numba
        return [gpu.name.decode("utf-8") for gpu in numba.cuda.gpus]
    except Exception: # numba.cuda.cudadrv.error.CudaSupportError:
        return []


def get_number_gpus():
    """Get the number of GPUs in the system.

    Returns:
        int: Number of GPUs.

    Examples:
        >>> get_number_gpus() #doctest: +SKIP
        0

    """
    try:
        import torch
        return torch.cuda.device_count()
    except (ImportError, ModuleNotFoundError):
        pass
    try:
        import numba
        return len(numba.cuda.gpus)
    except Exception: # numba.cuda.cudadrv.error.CudaSupportError:
        return 0


def get_gpu_compute_capability():
    """Get the GPUs compute capability.

    Returns:
        list: List of tuples (major, minor) indicating the supported compute capability.

    Examples:
        >>> get_gpu_compute_capability() #doctest: +SKIP
        [(6, 0)]

    """
    try:
        import numba
        return [gpu.compute_capability for gpu in numba.cuda.gpus]
    except Exception: # numba.cuda.cudadrv.error.CudaSupportError:
        return []


def get_cuda_version():
    """Get CUDA version

    Returns:
        str: Version of the library.

    """
    try:
        import torch
        return torch.version.cuda
    except (ImportError, ModuleNotFoundError):
        path = ""
        if sys.platform == "win32":
            candidate = (
                "C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v*\\version.txt"
            )
            path_list = glob.glob(candidate)
            if path_list:
                path = path_list[0]
        elif sys.platform == "linux" or sys.platform == "darwin":
            path = "/usr/local/cuda/version.txt"
        else:
            raise ValueError("Not in Windows, Linux or Mac")

        if os.path.isfile(path):
            with open(path, "r") as f:
                data = f.read().replace("\n", "")
            return data
        else:
            return "Cannot find CUDA in this machine"


def get_cudnn_version():
    """Get the CuDNN version

    Returns:
        str: Version of the library.

    """

    def find_cudnn_in_headers(candiates):
        for c in candidates:
            file = glob.glob(c)
            if file:
                break
        if file:
            with open(file[0], "r") as f:
                version = ""
                for line in f:
                    if "#define CUDNN_MAJOR" in line:
                        version = line.split()[-1]
                    if "#define CUDNN_MINOR" in line:
                        version += "." + line.split()[-1]
                    if "#define CUDNN_PATCHLEVEL" in line:
                        version += "." + line.split()[-1]
            if version:
                return version
            else:
                return "Cannot find CUDNN version"
        else:
            return "Cannot find CUDNN version"
            
    try:
        import torch
        return torch.backends.cudnn.version()
    except (ImportError, ModuleNotFoundError):
        if sys.platform == "win32":
            candidates = [r"C:\NVIDIA\cuda\include\cudnn.h"]
        elif sys.platform == "linux":
            candidates = [
                "/usr/include/cudnn_version.h",
                "/usr/include/x86_64-linux-gnu/cudnn_v[0-99].h",
                "/usr/local/cuda/include/cudnn.h",
                "/usr/include/cudnn.h",
            ]
        elif sys.platform == "darwin":
            candidates = ["/usr/local/cuda/include/cudnn.h", "/usr/include/cudnn.h"]
        else:
            raise ValueError("Not in Windows, Linux or Mac")
        return find_cudnn_in_headers(candidates)


def is_cuda_available():
    """Check if the system has cuda

    Note:
        If one types `nvidia-smi`, the CUDA version appears, however, this is just indicates
        the driver CUDA version support. It does not provide any information about which
        CUDA version is installed or even whether there is CUDA installed at all.

    Returns:
        bool: True if cuda is installed, False otherwise.

    Examples:
        >>> is_cuda_available() #doctest: +SKIP
        False

    """
    try:
        import torch
        return torch.cuda.is_available()
    except (ImportError, ModuleNotFoundError):
        pass
    try:
        import numba
        return len(numba.cuda.gpus)
    except Exception: # numba.cuda.cudadrv.error.CudaSupportError:
        return False


def get_conda_environment():
    """Get the conda environment from which the script is being executed

    Returns:
        str: Environment name

    Examples:
        >>> get_conda_environment() # doctest: +ELLIPSIS
        '...'

    """
    try:
        env = os.environ["CONDA_DEFAULT_ENV"]
    except KeyError:
        env = "No conda env found"
    return env

import sys
import psutil
import subprocess
from numba import cuda
from numba.cuda.cudadrv.error import CudaSupportError


def _manage_memory_units(data_in_bytes, units):
    if units == "bytes":
        return data_in_bytes
    elif units == "Kb":
        return data_in_bytes / 1024
    elif units == "Mb":
        return data_in_bytes / 1024 / 1024
    elif units == "Gb":
        return data_in_bytes / 1024 / 1024 / 1024
    else:
        raise AttributeError("Units not correct")


def get_object_size(obj, units="Mb"):
    """Calculate the size of an object.
    Args:
        obj (obj or str or array): Object.
        units (str): Units [bytes, Kb, Mb, Gb]
    Returns:
        size (float): Size of the object.
    Examples:
        >>> get_object_size(7, "bytes")
        28
        >>> get_object_size("ABC", "bytes")
        52

    """
    s_bytes = sys.getsizeof(obj)
    return _manage_memory_units(s_bytes, units)


def get_ram_memory(units="Mb"):
    """Get the RAM memory of the current machine.
    Args:
        units (str): Units [bytes, Kb, Mb, Gb]
    Returns:
        size (float): Memory size.
    Examples:
        >>> num = get_ram_memory("Gb") 
        >>> num >= 4
        True

    """
    s_bytes = psutil.virtual_memory()[0]
    return _manage_memory_units(s_bytes, units)


def get_total_gpu_memory(units="Mb"):
    """Get the memory of the GPUs in the system
    Returns:
        result (list): List of strings with the GPU memory in Mb
    Examples:
        >>> get_total_gpu_memory()
        []

    """
    try:
        memory_list = []
        for gpu in cuda.gpus:
            with gpu:
                meminfo = cuda.current_context().get_memory_info()
                memory_list.append(_manage_memory_units(meminfo[1], units))
        return memory_list
    except CudaSupportError:
        return []


def get_free_gpu_memory(units="Mb"):
    """Get the memory of the GPUs in the system
    Returns:
        result (list): List of strings with the GPU memory in Mb
    Examples:
        >>> get_free_gpu_memory()
        []

    """
    try:
        memory_list = []
        for gpu in cuda.gpus:
            with gpu:
                meminfo = cuda.current_context().get_memory_info()
                memory_list.append(_manage_memory_units(meminfo[0], units))
        return memory_list
    except CudaSupportError:
        return []

import sys
import psutil


def _manage_memory_units(data_in_bytes, units):
    if units == "bytes":
        return data_in_bytes
    elif units == "Kb":
        return data_in_bytes / 1024
    elif units == "Mb":
        return data_in_bytes / 1048576  # 1024**2
    elif units == "Gb":
        return data_in_bytes / 1073741824  # 1024**3
    else:
        raise AttributeError("Units not correct")


def get_object_size(obj, units="Mb"):
    """Calculate the size of an object.
    
    Args:
        obj (obj or str or array): Object.
        units (str): Units [bytes, Kb, Mb, Gb]
    
    Returns:
        float: Size of the object.
    
    Examples:
        >>> get_object_size(7, "bytes")
        28
        >>> get_object_size("ABC", "bytes")
        52
    """
    s_bytes = sys.getsizeof(obj)
    return _manage_memory_units(s_bytes, units)


def get_pandas_df_size(obj, units="Mb"):
    """Calculate the size of a pandas DataFrame.

    Args:
        obj (pd.DataFrame): Dataframe.
        units (str): Units [bytes, Kb, Mb, Gb]
    
    Returns:
        float: Size of the object.
    
    Examples:
        >>> df = pd.DataFrame({"a":[1]*100, "b":[0.5]*100}) 
        >>> get_pandas_df_size(df, "Kb")
        1.6875
    """
    obj_bytes = obj.memory_usage(deep=True).sum()
    return _manage_memory_units(obj_bytes, units)


def get_ram_memory(units="Mb"):
    """Get the RAM memory of the current machine.
    
    Args:
        units (str): Units [bytes, Kb, Mb, Gb]
    
    Returns:
        float: Memory size.
    
    Examples:
        >>> num = get_ram_memory("Gb") 
        >>> num >= 2
        True
    """
    s_bytes = psutil.virtual_memory()[0]
    return _manage_memory_units(s_bytes, units)


def get_total_gpu_memory(units="Mb"):
    """Get the memory of the GPUs in the system
    
    Returns:
        list: List of strings with the GPU memory in Mb
    
    Examples:
        >>> get_total_gpu_memory() #doctest: +SKIP
        [16280.875]
    """
    try:
        import numba
        memory_list = []
        for gpu in numba.cuda.gpus:
            with gpu:
                meminfo = numba.cuda.current_context().get_memory_info()
                memory_list.append(_manage_memory_units(meminfo[1], units))
        return memory_list
    except Exception: #numba.cuda.cudadrv.error.CudaSupportError:
        return []


def get_free_gpu_memory(units="Mb"):
    """Get the memory of the GPUs in the system
    
    Returns:
        list: List of strings with the GPU memory in Mb
    
    Examples:
        >>> get_free_gpu_memory() #doctest: +SKIP
        [15987.8125]

    """
    try:
        import numba
        memory_list = []
        for gpu in numba.cuda.gpus:
            with gpu:
                meminfo = numba.cuda.current_context().get_memory_info()
                memory_list.append(_manage_memory_units(meminfo[0], units))
        return memory_list
    except Exception: # numba.cuda.cudadrv.error.CudaSupportError:
        return []


def clear_memory_all_gpus():
    """Clear memory of all GPUs.
    
    Examples:
        >>> clear_memory_all_gpus() #doctest: +SKIP
        No CUDA available

    """
    try:
        import numba
        for gpu in numba.cuda.gpus:
            with gpu:
                numba.cuda.current_context().deallocations.clear()
    except Exception: # numba.cuda.cudadrv.errorCudaSupportError:
        print("No CUDA available")


def clear_memory_gpu_id(id):
    """Clear memory of all GPUs.
    
    Args:
        id (int): GPU id.
    
    Examples:
        >>> clear_memory_gpu_id(0) #doctest: +SKIP
        No CUDA available
    """
    try:
        import numba
        for gpu in numba.cuda.gpus:
            numba.cuda.select_device(gpu.id)
            numba.cuda.close()
    except Exception: # numba.cuda.cudadrv.error.CudaSupportError:
        print("No CUDA available")
    except IndexError:
        raise ValueError("GPU id should be between 0 and {}".format(len(numba.cuda.gpus) - 1))

import sys
import os
import requests
import logging
from contextlib import contextmanager
from tempfile import TemporaryDirectory
from tqdm import tqdm


log = logging.getLogger(__name__)


def maybe_download(
    url, filename=None, work_directory=".", expected_bytes=None, force_download=False
):
    """Download a file if it is not already downloaded.
    
    Args:
        filename (str): File name.
        work_directory (str): Working directory.
        url (str): URL of the file to download.
        expected_bytes (int): Expected file size in bytes.
        force_download (bool): 

    Returns:
        str: File path of the file downloaded.

    Examples:
        >>> url = "https://raw.githubusercontent.com/miguelgfierro/pybase/master/LICENSE"
        >>> if os.path.exists("license.txt"): os.remove("license.txt")
        >>> filename = maybe_download(url, "license.txt", expected_bytes=1531)
        >>> os.path.isfile(filename)
        True
        
    """
    if filename is None:
        filename = url.split("/")[-1]
    os.makedirs(work_directory, exist_ok=True)
    filepath = os.path.join(work_directory, filename)
    if not os.path.exists(filepath):
        r = requests.get(url, stream=True)
        total_size = int(r.headers.get("content-length", 0))
        block_size = 1024
        num_iterables = math.ceil(total_size / block_size)
        with open(filepath, "wb") as file:
            for data in tqdm(
                r.iter_content(block_size),
                total=num_iterables,
                unit="KB",
                unit_scale=True,
            ):
                file.write(data)
    else:
        log.debug("File {} already downloaded".format(filepath))
    if expected_bytes is not None:
        statinfo = os.stat(filepath)
        if statinfo.st_size != expected_bytes:
            os.remove(filepath)
            raise IOError("Failed to verify {}".format(filepath))

    return filepath


@contextmanager
def download_path(path=None):
    """Return a path to download data. If `path=None`, then it yields a temporal path that is eventually deleted, 
    otherwise the real path of the input. 

    Args:
        path (str): Path to download data.

    Returns:
        str: Real path where the data is stored.

    Examples:
        >>> url = "https://raw.githubusercontent.com/miguelgfierro/pybase/master/LICENSE"
        >>> with download_path() as path:
        ...     maybe_download(url=url, work_directory=path) # doctest: +ELLIPSIS
        '...LICENSE'

    """
    if path is None:
        tmp_dir = TemporaryDirectory()
        try:
            yield tmp_dir.name
        finally:
            tmp_dir.cleanup()
    else:
        path = os.path.realpath(path)
        yield path


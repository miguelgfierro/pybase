import sys
import os
from urllib.request import urlretrieve
import logging
from contextlib import contextmanager
from tempfile import TemporaryDirectory
from tqdm import tqdm


log = logging.getLogger(__name__)


def maybe_download(url, filename=None, work_directory=".", expected_bytes=None):
    """Download a file if it is not already downloaded.
    
    Args:
        filename (str): File name.
        work_directory (str): Working directory.
        url (str): URL of the file to download.
        expected_bytes (int): Expected file size in bytes.

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
        with _TqdmUpTo(unit="B", unit_scale=True) as t:
            filepath, _ = urlretrieve(url, filepath, reporthook=t.update_to)
    else:
        log.debug("File {} already downloaded".format(filepath))
    if expected_bytes is not None:
        statinfo = os.stat(filepath)
        if statinfo.st_size != expected_bytes:
            os.remove(filepath)
            raise IOError("Failed to verify {}".format(filepath))

    return filepath


class _TqdmUpTo(tqdm):
    """Wrapper class for the progress bar tqdm to get `update_to(n)` functionality"""

    def update_to(self, b=1, bsize=1, tsize=None):
        """A progress bar showing how much is left to finish the operation
        
        Args:
            b (int): Number of blocks transferred so far.
            bsize (int): Size of each block (in tqdm units).
            tsize (int): Total size (in tqdm units). 
        """
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)  # will also set self.n = b * bsize


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


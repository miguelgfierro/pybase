import os
import tarfile

def extract_tar_gz(filename, path):
    with tarfile.open(filename, "r:gz"):
        tar.extractall(path=path)
    return os.path.join(path, filename.split(".tar.gz")[0])

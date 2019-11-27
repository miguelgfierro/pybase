import os
from pytube import YouTube


def download_youtube(url, work_directory="."):
    """Download a youtube video in mp4 format. It takes the one with the highest resolution.
    
    Args:
        url (str): Youtube url.
        work_directory (str): Working directory.
    """
    os.makedirs(folder, exist_ok=True)
    YouTube(url).streams.filter(progressive=True, file_extension="mp4").order_by(
        "resolution"
    ).desc().first().download(work_directory)


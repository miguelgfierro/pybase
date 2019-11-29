import os
from pytube import YouTube


def download_youtube(url, work_directory="."):
    """Download a youtube video in mp4 format. It takes the one with the highest resolution.
    
    Args:
        url (str): Youtube url.
        work_directory (str): Working directory.

    Returns:
        str: Path to the video file.
    """
    os.makedirs(work_directory, exist_ok=True)
    filepath = (
        YouTube(url)
        .streams.filter(progressive=True, file_extension="mp4")
        .order_by("resolution")
        .desc()
        .first()
        .download(work_directory)
    )
    return filepath


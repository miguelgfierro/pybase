import os
import cv2
from moviepy.video.io.ffmpeg_tools import (
    ffmpeg_extract_subclip,
    ffmpeg_movie_from_frames,
)


def cut_video(input_file, start_time, end_time, output_file):
    """Cut a portion of a video.

    Args:
        input_file (str): Input video file.
        start_time (int): Start time in seconds.
        end_time (int): End time in seconds
        output_file (str): Output video file.
    """
    ffmpeg_extract_subclip(input_file, start_time, end_time, output_file)


def video_from_frames_cv(filename, folder, fps=25, img_format=".jpeg"):
    """Create a video from a set of frames in a folder using OpenCV.

    Args:
        filename (str): Name of the video.
        folder (str): Folder with images.
        fps (int): Frames per second.
        img_format (str): Image format.
    """
    images = [img for img in os.listdir(folder) if img.endswith(img_format)]
    frame = cv2.imread(os.path.join(folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(
        filename, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height)
    )

    for image in images:
        video.write(cv2.imread(os.path.join(folder, image)))

    cv2.destroyAllWindows()
    video.release()


def video_to_frames_cv(filename, folder, img_format=".jpeg", leading_zeros=6):
    """Convert a video into a set of images.

    Args:
        filename (str): Name of the video.
        folder (str): Folder with images.
        img_format (str): Image format.
        leading_zeros (int): Leading zeros added to the image name.
    """
    video_path = os.path.join(folder, filename)
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Video not found at {video_path}")
    capture = cv2.VideoCapture(video_path)
    count = 0
    success, frame = capture.read()
    while success:
        image_number = str(count).rjust(leading_zeros, "0")
        image_name = filename.split(".")[0] + "_" + image_number + img_format
        cv2.imwrite(os.path.join(folder, image_name), frame)
        success, frame = capture.read()
        count += 1
    capture.release()


def video_from_frames_ffmpeg(filename, folder, fps=25, **kwargs):
    """Create a video from a set of frames in a folder using ffmpeg.

    Args:
        filename (str): Name of the video.
        folder (str): Folder with images.
        fps (int): Frames per second.

    """
    allowed_kwargs = {"digits", "bitrate"}
    for k in kwargs:
        if k not in allowed_kwargs:
            raise TypeError(
                "Unexpected keyword argument passed to optimizer: " + str(k)
            )
    ffmpeg_movie_from_frames(filename, folder, fps, kwargs)

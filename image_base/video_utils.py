from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def cut_video(input_file, start_time, end_time, output_file):
    """Cut a portion of a video.
    
    Args:
        input_file (str): Input video file.
        start_time (int): Start time in seconds.
        end_time (int): End time in seconds
        output_file (str): Output video file.
    """
    ffmpeg_extract_subclip(filename, start_time, end_time, targetname)


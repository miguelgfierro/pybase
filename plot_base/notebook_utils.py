import io
import base64
from IPython.display import HTML


def show_local_mp4_video(file_name, width=640, height=480):
    """Renders a mp4 video on a Jupyter notebook

    Args:
        file_name (str): Path to file.
        width (int): Video width.
        height (int): Video height.

    Returns:
        obj: Video render as HTML object.
    """
    video_encoded = base64.b64encode(io.open(file_name, 'rb').read())
    return HTML(data='''<video width="{0}" height="{1}" alt="test" controls>
                            <source src="data:video/mp4;base64,{2}" type="video/mp4" />
                          </video>'''.format(width, height, video_encoded.decode('ascii')))

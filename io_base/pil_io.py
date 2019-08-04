# Info: http://effbot.org/imagingbook/image.htm
from PIL import Image
import requests


def save_image(img, filename):
    """Save an image using PIL.
    
    Args:
        img (numpy array): An image.
        filename (str): Name of the file.
    
    Examples:
        >>> img = Image.open('share/Lenna.png')
        >>> save_image(img, 'file.jpg')
        >>> os.path.isfile('file.jpg')
        True
        >>> os.remove('file.jpg')
        >>> os.path.isfile('file.jpg')
        False
    """
    img.save(filename)


def read_image(filename):
    """Read an image using PIL.
    
    Args:
        filename (str): Name of the file.
    
    Returns:
        img (PIL image): An image in PIL format.
    
    Examples:
        >>> img = read_image('share/Lenna.png')
        >>> print(img.size)
        (512, 512)
        >>> print(img.mode)
        RGB
        >>> img_gray = read_image('share/Lenna_gray.png')
        >>> print(img_gray.size)
        (512, 512)
        >>> print(img_gray.mode)
        L

    """
    return Image.open(filename)


def read_image_url(url):
    """Read an image from a URL using PIL.

    Args:
        url (str): URL of the file.

    Returns:
        PIL image: An image in PIL format.

    Examples:
        >>> img = read_image_url('https://raw.githubusercontent.com/miguelgfierro/pybase/master/share/Lenna.png')
        >>> print(img.size)
        (512, 512)
        >>> print(img.mode)
        RGB
    """
    return Image.open(requests.get(url, stream=True).raw)

import cv2
import numpy as np
import urllib.request as urllib


def save_image(img, filename):
    """Save an image with OpenCV.

    Args:
        img (numpy array): An image.
        filename (str): Name of the file.

    Examples:
        >>> img = cv2.imread('share/Lenna.png')
        >>> save_image(img, 'file.jpg')
        >>> os.path.isfile('file.jpg')
        True
        >>> os.remove('file.jpg')
        >>> os.path.isfile('file.jpg')
        False

    """
    cv2.imwrite(filename, img)


def read_image(filename, flag=cv2.IMREAD_UNCHANGED):
    """Read an image with OpenCV.

    Args:
        filename (str): Name of the file.
        flag (int): If -1 (cv2.IMREAD_UNCHANGED), it loads the image as it is including
            the alpha channel. If 0 (cv2.IMREAD_GRAYSCALE), it loads in grayscale. If
            1 (cv2.IMREAD_COLOR), it loads a color image, neglecting transparencies.

    Returns:
        np.array: An image.

    Examples:
        >>> img = read_image('share/Lenna.png')
        >>> shape = np.array(img.shape)
        >>> print(shape)
        [512 512   3]
        >>> img_gray = read_image('share/Lenna.png', 0)
        >>> shape_gray = np.array(img_gray.shape)
        >>> print(shape_gray)
        [512 512]

    """
    return cv2.imread(filename, flag)


def read_image_url(url):
    """Read an image from a URL.

    Args:
        url (str): URL of the file.

    Returns:
        np.array: An image.

    Examples:
        >>> img = read_image_url('https://raw.githubusercontent.com/miguelgfierro/pybase/master/share/Lenna.png')
        >>> shape = np.array(img.shape)
        >>> print(shape)
        [512 512   3]

    """
    try:
        resp = urllib.urlopen(url)
    except urllib.HTTPError:
        raise ("Error opening url {0}".format(url))
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

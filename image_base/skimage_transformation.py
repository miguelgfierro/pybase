from skimage.util.dtype import convert
from skimage.transform import resize


def resize_image(img, new_width, new_height):
    """Resize image to a ``new_width`` and ``new_height``.
    
    Args:
        img (np.array): An image.
        new_width (int): New width.
        new_height (int): New height.
    
    Returns:
        np.array: A resized image.
    
    Examples:
        >>> img = Image.open('share/Lenna.png')
        >>> img_resized = resize_image(img, 256, 256)
        >>> img_resized.shape
        (256, 256, 3)
    """
    img_new = resize(
        img, (int(new_width), int(new_height)), anti_aliasing=True
    )  # always returns float64 type
    return convert(img_new, dtype=img.dtype)

from PIL import Image, ImageOps


def normalize_image(img):
    """Normalize image between 0 and 255.
    Parameters:
        img (PIL image): An image.
    Returns:
        img_new (PIL image): A normalized image.
    Examples:
        >>> img = Image.open('../../share/Lenna.png')
        >>> vals = img.getextrema() #gets min and max value in the three channels
        >>> vals
        ((54, 255), (3, 248), (8, 225))
        >>> img_norm = normalize_image(img)
        >>> vals = img_norm.getextrema()
        >>> vals
        ((0, 255), (0, 255), (0, 254))

    """
    return ImageOps.autocontrast(img)


def resize_image(img, new_width, new_height):
    """Resize image to a `new_width` and `new_height`.
    Parameters:
        img (PIL image): An image.
        new_width (int): New width.
        new_height (int): New height.
    Returns:
        img_new (PIL image): A resized image.
    Examples:
        >>> img = Image.open('../../share/Lenna.png')
        >>> width, height = img.size
        >>> img_resized = resize_image(img, width/2, height/2)
        >>> img_resized.size
        (256, 256)

    """
    img_new = img.resize((new_width, new_height))
    return img_new


def equalize_image(img):
    """Equalize the image histogram.
    Parameters:
        img (PIL image): An image.
    Returns:
        img_new (PIL image): A equalized image.
    Examples:
        >>> img = Image.open('../../share/Lenna.png')
        >>> img_eq = equalize_image(img)

    """
    return ImageOps.equalize(img)
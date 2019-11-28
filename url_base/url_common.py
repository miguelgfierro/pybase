def get_image_name(url):
    """Get the file name of an image url.
    
    Args:
        url (str): Image url.
    
    Returns:
        str: Image name.

    Examples:
        >>> url = "https://miguelgfierro.com/static/blog/img/hoaphumanoid.png"
        >>> get_image_name(url)
        'hoaphumanoid.png'
        >>> url = "https://miguelgfierro.com/static/blog/img/hoaphumanoid.png?itok=o-EKrRkB"
        >>> get_image_name(url)
        'hoaphumanoid.png'
        >>> url = "https://miguelgfierro.com/static/blog/img/hoaphumanoid"
        >>> get_image_name(url)
        'hoaphumanoid.jpg'

    """
    image_name = str(url[(url.rfind("/")) + 1 :])
    if "?" in image_name:
        image_name = image_name[: image_name.find("?")]
    extensions = (".jpg", ".jpeg", ".gif", ".png", ".bmp", ".svg", ".webp", ".ico")
    if not any(ext in image_name for ext in extensions):
        image_name = image_name + ".jpg"
    return image_name


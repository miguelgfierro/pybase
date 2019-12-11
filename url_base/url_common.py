def get_image_name(url, char_limit=60):
    """Get the file name of an image url.
    
    Args:
        url (str): Image url.
        char_limit (int): Maximum number of characters for the name.
    
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
        >>> url = "https://miguelgfierro.com/012345678901234567890123456789.jpg"
        >>> get_image_name(url, 20)
        '01234567890123456789.jpg'

    """
    name = str(url[(url.rfind("/")) + 1 :])
    if "?" in name:
        name = name[: name.find("?")]

    extensions = (".jpg", ".jpeg", ".gif", ".png", ".bmp", ".svg", ".webp", ".ico")
    if any(ext in name for ext in extensions):
        pos = name.rfind(".")
        ext = name[pos:]
        name = name[:pos]
    else:
        ext = ".jpg"

    if len(name) >= char_limit:
        name = name[:char_limit]

    return name + ext


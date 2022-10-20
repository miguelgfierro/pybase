from skimage import io


def plot_image(img):
    """Plot an image.
    
    Args:
        img (np.array): An image.
    
    Examples:
    
        >>> matplotlib.use("Template") # Avoids opening a window in plt.show()
        >>> img = io.imread('share/Lenna.png')
        >>> plot_image(img)
    """
    io.imshow(img)
    io.show()

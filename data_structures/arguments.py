class Example:
    """Example of class with a restriction on allowed arguments
    
    source: https://github.com/keras-team/keras/blob/master/keras/optimizers.py
    """

    def __init__(self, **kwargs):
        allowed_kwargs = {"clipnorm", "clipvalue"}
        for k in kwargs:
            if k not in allowed_kwargs:
                raise TypeError(
                    "Unexpected keyword argument passed to optimizer: " + str(k)
                )
        self.__dict__.update(kwargs)


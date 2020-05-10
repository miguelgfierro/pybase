import tensorflow as tf
import numpy as np


def derivate(func, x, val):
    """Perform autodifferentiation.

    `See more info <https://adel.ac/automatic-differentiation/>`_

    Args:
        func (callable): The objective function to be minimized. 
        x (np.array): Initial conditions.

    Returns:
        list, float: Derivative and value function.

    Examples:
        >>> x = tf.Variable([0., 0.], tf.float32)
        >>> y = tf.add(tf.pow(tf.subtract(1.0, x[0]), 2.0), tf.multiply(100.0, tf.pow(tf.subtract(x[1],tf.pow(x[0], 2.0)), 2.0)), 'y') # rosenbrock function
        >>> val = np.array([1, 1], dtype=np.float32)
        >>> xd, y = derivate(y, x, val)
        >>> xd
        array([0., 0.], dtype=float32)
        >>> y
        0.0
    """
    dx = tf.gradients(func, x)[0]
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        dvalue = sess.run(dx, {x: val})
        value = sess.run(func, {x: val})
    return dvalue, value

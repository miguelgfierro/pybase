import tensorflow as tf
import numpy as np


def derivate(func, x):
    """Perform autodifferentiation.

    `See more info <https://adel.ac/automatic-differentiation/>`_

    Args:
        func (callable): The objective function to be minimized. 
        x (list of tensors): Initial conditions.

    Returns:
        tensor, tensor, tensor: Derivative and value function.

    Examples:
        >>> y = tf.add(tf.pow(tf.subtract(1.0, x[0]), 2.0), tf.multiply(100.0, tf.pow(tf.subtract(x[1],tf.pow(x[0], 2.0)), 2.0)), 'y') # rosenbrock function
        >>> x = np.array([1.0, 1.0], dtype=np.float32)
        >>> xd, y = derivate(y, x)
        >>> xd
        [0. 0.]
        >>> y
        0.0
    """
    var = tf.Variable([0.0, 0.0], tf.float32)
    dx = tf.gradients(func, var)[0]
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        dval = sess.run(dx, {var: x})
        val = sess.run(func, {var: x})
        # print(sess.run(func, {var: x}), sess.run(dx, {var: x}))
    return dval, val

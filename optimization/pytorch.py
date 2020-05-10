import torch
from torch.autograd import Variable
from torch import FloatTensor


def optimize_function(func, x, rounds=10000, lr=0.001):
    """Minimize a pytorch function starting from initial condition x.

    Args:
        func (callable): The objective function to be minimized. 
        x (list of tensors): Initial conditions.
        rounds (int): Number of rounds.
        lr (float): Learning rate.

    Returns:
        tensor, tensor: Minimization final value and function evaluated at the minimum.

    Examples:
        >>> from .functions import rosenbrock
        >>> x = [Variable(FloatTensor([2]), requires_grad=True), Variable(FloatTensor([2]), requires_grad=True)]
        >>> x, y = optimize_function(rosenbrock, x)
        >>> x
        [tensor([1.0081], requires_grad=True), tensor([1.0162], requires_grad=True)]
        >>> y
        tensor([6.5133e-05], grad_fn=<AddBackward0>)

    """
    optimizer = torch.optim.SGD(x, lr=lr)
    # optimizer = torch.optim.Adam(x, lr=lr)
    y = func(x)
    for i in range(rounds):
        optimizer.zero_grad()
        y.backward(retain_graph=True)
        optimizer.step()
        y = func(x)
        # if (i + 1) % 1000 == 0:
        #     print(i + 1, x, y)
    return x, y


def derivate(func, x):
    """Perform autodifferentiation.

    `See more info <https://adel.ac/automatic-differentiation/>`_

    Args:
        func (callable): The objective function to be differentiated. 
        x (list of tensors): Initial conditions.

    Returns:
        tensor, tensor, tensor: Derivative and value function.

    Examples:
        >>> from .functions import rosenbrock
        >>> x = [Variable(FloatTensor([1]), requires_grad=True), Variable(FloatTensor([1]), requires_grad=True)]
        >>> xd1, xd2, y = derivate(rosenbrock, x)
        >>> xd1, xd2
        (tensor([-0.]), tensor([0.]))
        >>> y
        tensor([0.], grad_fn=<AddBackward0>)

    """
    y = func(x)
    y.backward()
    return x[0].grad, x[1].grad, y

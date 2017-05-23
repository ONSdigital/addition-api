import sys


def add(x, y):
    """
    adds two numbers
    Pass in 2 numbers, get the result of summing them
    :param x:
    :type x: int
    :param y:
    :type y: int

    :rtype: int
    """
    print("Received x={}, y={}. (Python version {}).".format(x, y, sys.version))
    return x + y

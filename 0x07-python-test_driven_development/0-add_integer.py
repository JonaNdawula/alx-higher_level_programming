#!/usr/bin/python3
"""Adds two integers"""


def add_integer(a, b=98):
    """
    Adds parameters a and b

    Any floats are converted to integer types

    Raises:
        TypeError:a must be an integer or b must be an integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)

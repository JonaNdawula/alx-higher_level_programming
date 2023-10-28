#!/usr/bin/python3
"""
Function that  prints a square with character #

"""

def print_square(size):
    """
    prints square using character #

    Args:
        size (int): square size of one side

    Raises:
        TypeError: If size is not an integer and less than 0
        valueError: If size is less than 0
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    
    for index in range(size):
        print("#" * size)

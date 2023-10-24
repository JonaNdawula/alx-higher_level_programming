#!/usr/bin/python3
"""Defines a square by: (based on 2-square.py)"""


class Square:
    """
    A Class that defines a square

    Attributes:
        size: size of a square
    """

    def __init__(self, size=0):
        """
        Creates new square instance

        Args:
            size:represents size of a square

        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Function that calculate area of a square

        Returns: Area of square
        """
        return (self.__size * self.__size)

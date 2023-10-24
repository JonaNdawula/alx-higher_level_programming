#!/usr/bin/python3
"""This class defines a square"""


class Square:
    """
    Class Square that defines a square by: (based on 3-square.py)

    Attributes:
        size: represents size on a square
    """
    def __init__(self, size=0):
        """
         Is a new instance of a square

         Args:
            size: represents size of a square side

        """
        self.__size = size

    def area(self):
        """
        Function that calculates the area of a square

        Returns: The area of a square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        Returns: the square size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        A property setter for the size

        Args:
            value (int): size of square side

        Raise:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

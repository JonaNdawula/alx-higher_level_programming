#!/usr/bin/python3
""" Class Square that defines a square by: (based on 5-square.py)  """


class Square:
    """
    A class Square that defines a square by: (based on 5-square.py)

    Attributes:
        size: represents side of a square
    """
    def __init__(self, size=0):
        """
        Creates new instance of a square

        Args:
            size: size of square side
        """
        self.__size = size

    def area(self):
        """
        method that calculates square area

        Returns: square area
        """
        return (self.__size * self.size)

    @property
    def size(self):
        """
        Returns: size of square side
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        sets the size

        Args:
            value (int): size of square size

        Raises:
            TypeError: size must be an integer
            valueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
         prints in stdout the square with the character #:
        """

        if self.__size == 0:
            print()
        for index in range(self.__size):
            print("#" * (self.__size))

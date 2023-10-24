#!/usr/bin/python3
"""A class called Square"""


class Square:
    """
    Class difining a square

    Attributes:
        size: size of side of the square
    """

    def __init__(self, size=0):
        """
        creates new square

        Args:
            size" size of side of square
        """
        self.__size = size

    def area(self):
        """
        Calculates area of square

        Returns: area of square
        """

        return (self.__size * self.__size)

    @property
    def size(self):
        """
        Return: The size of side of square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        sets

        Args:
            value (int): size of square size

        Raises:
            TypeError:  size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            ValueError("size must be >= 0")
        else:
            self.__size = value

    def __lt__(self, other):
        """
        Compares if area of one square is less than another

        Args:
            other: square to be compared to

        Returns: True  or False
        """

        return (self.__size < other.__size)

    def __le__(self, other):
        """
        Compares if area of square is less than or equal to another square
        Args:
            other: square to be compared
        """
        return (self.__size <= other.__size)

    def __eq__(self, other):
        """
        compares if area of square is equal to another

        Args:
            other: square to be compared to

        Return: True or False
        """

        return (self.__size == other.__size)

    def __ne__(self, other):
        """
        Compares if square area is not equal to another

        Args:
            Other: square to compare size too

        return: True of False
        """
        return (self.__size != other.__size)

    def __gt__(self, other):
        """
        Compares if square area is greater than another

        Args:
            Other: square to compare size

        Return: True or False
        """
        return (self.__size > other.__size)

    def __ge__(self, other):
        """
        Compares if square area is greater or equal to another

        Args:
            other: square to be compared to
        Returns: True or False
        """
        return (self.__size >= other.__size)

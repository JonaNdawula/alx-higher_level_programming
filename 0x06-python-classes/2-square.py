#!/usr/bin/python3
"""Defines a square class based on 1-square.py"""


class Square:
    """
    Is a class that defines a square based on 1-square.py


    Attributes:
        size: represents size of the square
    """
    def __init__(self, size=0):
        """
        Creates new instance of a square


        Args:
            size: represents the size of a square
        """

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

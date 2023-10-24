#!/usr/bin/python3
"""Defines a square based on 0-square.py"""


class Square:
    """
    This class defines a square based on 0-square.py

    Attributes:
        size: is a Private insatnce attribute
    """

    def __init__(self, size):

        """
        It creates a new instance of a square
        Args:
            size: represents size of the square
        """
        self.__size = size

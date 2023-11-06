#!/usr/bin/python3
"""
Class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
        creates new square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns string form of square
        """
        return ("[Square]{}/{}".format(self.__size. self.__size))

    def area(self):
        """
        Area of square
        """
        return (self.__size * self.__size)

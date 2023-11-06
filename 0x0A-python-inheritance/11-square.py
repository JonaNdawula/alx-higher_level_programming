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
        crrates new square
        """
        self.integer_validator("siz", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns strin form of square
        """
        return ("[square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """
        Area of square
        """
        return (self.__size * self.__size)

#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """
    Class defining rectangle properties

    Attributes:
    width (int): rectangle width
    height(int): rectangle height
    """
    def __init__(self, width=0, height=0):
        """
        New rectangle instance
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        gets width
        """

        return (self.__width)

    @width.setter
    def width(self, value):
        """
        sets width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width < 0
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        gets height
        """

        return (self.__height)

    @height.setter
    def height(self, value):
        """
        sets height

        Raises:
            TypeError: if height is not an integer
            ValueError: if width < 0
        """

        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Area of rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

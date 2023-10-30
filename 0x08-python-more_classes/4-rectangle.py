#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """
    Defines properties of a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        creates new rectangle instance
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        get width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        sets width

        Raises:
            TypeError: if width is not an integer
            ValueError: if value is < 0
        """
        if isinstance(value, int) is False:
            TypeError("width must be an integer")
        elif value < 0:
            ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        get height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        sets height
        Raises:
            TypeError: if height is not an integer
            ValueError: if value is < 0
        """
        if isinstance(value, int) is False:
            TypeError("height must be an integer")
        elif value < 0:
            ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Area of rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        perimeter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return (2 * (self.__height + self.__height))

    def __str__(self):
        """
        prints a rectangle with # pattern
        """
        rect = []

        if self.__height == 0 or self.__width == 0:
            return ("")

        for h in range(self.__height):
            for w in range(self.__width):
                rect.append("#")
            rect.append("\n")

        rect.pop()

        return ("".join(rect))

    def __repr__(self):
        """
        string representation of rectangle
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

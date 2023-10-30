#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """
    Defines properties of a rectangle

    Attributes:
        width (int): rectnagle width
        height (int): rectangle height
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        New rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        gets width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        sets width of rectangle

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
        sets height of triangle

        Raises:
            TypeError: if height is not an integer
            ValueError: if height < 0
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
        return (self.__height * self.__width)

    def perimeter(self):
        """
        Perimeter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """
        prints rectangle using #
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
        string representation of rectsngle
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """
        Delete rectangle intance
        """
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1

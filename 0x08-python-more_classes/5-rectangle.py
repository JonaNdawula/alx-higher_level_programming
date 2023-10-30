#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """
    Deals with properties of a rectangle

    Attributes:
        width (int): rectngle width
        height (int): rectangle height
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
            TypeError: if width not an integer
            ValueError: if width is < 0
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
            ValueError: if height is < 0
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
        Perimeter of rectangel
        """

        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """
        use # to print a rectangle
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
        String representation of rectangle
        """
        return ("Rectangle({:d}, {:d}".format(self.__width, self.__heught))

    def __del__(self):
        """
        deletes class instance
        """
        print("{:s}".format("Bye rectangle..."))

#!/usr/bin/python3
"""
A Rectangle class
"""


class Rectangle:
    """
    Defines rectangel properties

    Attributes:
        width (int): rectangle width
        height (int): Rectangle height
    """

    def __init__(self, width=0, height=0):
        """
        Creates new rectangle instance
        """
        self.height = height
        self.width = width

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
            valueError: if width < 0
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
         sets height of rectangle

         Raises:
            TypeError: if height is not an integer
            ValueError: if height is < 0
        """
        if isinstance(value, int) is False:
            TypeError("height must be an integer")
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
        perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """
        prints # in form of rectangle
        """
        rect = []

        if self.__width == 0 or self.__height == 0:
            return ("")

        for h in range(self.__height):
            for w in range(self.__width):
                rect.append("#")
            rect.append("\n")

        rect.pop()

        return ("".join(rect))

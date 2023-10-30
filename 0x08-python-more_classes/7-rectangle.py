#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """
    Defines retangle properties
    
    Attributes:
        width(int): rectangle width
        height (int): rectangle height
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        New rectangle
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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

        Returns:
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
        get height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        set height

        Returns:
            TypeError: if height is no an integer
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

    def perimenter(self):
        """
        Perimeter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """
        displays rectangle with # pattern
        """
        rect = []

        if self.__height == 0 or self.__width == 0:
            return ("")

        for h in range(self.__height):
            for w in range(self.__width):
                rect.append(str(self.print_symbol))
            rect.append("\n")

        rect.pop()

        return ("".join(rect))

    def __repr__(self):
        """
        string representation of rectangle
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__heigt))

    def __del__(self):
        """
        Deletes rectangle instance
        """
        print("{:s}", format("Bye rectangle..."))
        type(self).number_of_instances -= 1

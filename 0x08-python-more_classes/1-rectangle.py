#!/usr/bin/python3
"""
  class Rectangle- that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """
    Class defining rectngle properties

    Attributs:
        width(int): rectangle width
        height (int) rectangle height

    """
    def __init__(self, width=0, height=0):
        """
        Initialize -  3params self, width, height


        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Sets width
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter for height
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

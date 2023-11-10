#!/usr/bin/python3
"""
Class Rectangle inherits from Base class
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class with rectangle properties
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        creates new rectangle
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter for width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter for width
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        self.__height = value

    @property
    def x(self):
        """
        getter for x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        setter for x
        """
        self.__x = value

    @property
    def y(self):
        """
        getter for y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        setter for y
        """
        self.__y = value

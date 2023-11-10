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

    def __str__(self):
        """
        Rectangle string form
        """
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y,
                       self.__width, self.__height))

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

        Raises:
            TypeError: if width is not an integer
            ValeError: if width < 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
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

        Raises:
            TypeError: if height is not an integer
            ValueError: if height < 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
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

        Raises:
            TypeError: if x is not an integer
            ValueError: if x < 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
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

        Raises:
            TypeError: if y is not integer
            ValueError: if y < 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Area of Rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Prints in stdout the
        Rectangle instance with
        the character #
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

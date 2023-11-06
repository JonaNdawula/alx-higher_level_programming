#!/usr/bin/python3
"""
Class Rectangle that inherits from 
BaseGeometry (7-base_geometry.py).
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Create a new rectangle
        """

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Area of rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Gives string representation of rectangle
        """
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

#!/usr/bin/python3
"""
A class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """
    BaseGeometry (based on 6-base_geometry.py).
    """
    def area(self):
        """
        Method that raises an Exception with the
        message area() is not implemented

        Raises:
             Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Used to validate a value

        Raises:
            TypeError if the value is not an integer
            ValueError if the value is less than or equal to 0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3
""" Deines MagicClass"""
import math


class MagicClass:
    """
    Defines Properties of  MagicClass

    Attributes:
      radius: radius
    """
    def __init__(self, radius=0):
        """
        New instance of MagicClass


        Args:
            radius: radius

        Raises:
            TypeError: radius must be a number
        """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, flost):
            raise TypeError("radius must be a number")
        else:
            self._radius = radius

    def area(self):
        """
        Returns area

        Returns: area
        """
        return (math.pi * self.__radius * self.__radius)

    def circumference(self):
        """
        Returns the circumference

        Return: circumference
        """

        return (2 * math.pi * self.__radius)

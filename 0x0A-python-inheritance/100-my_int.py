#!/usr/bin/python3
"""
A class MyInt that inherits from int
"""


class MyInt(int):
    """
    Class MyInt
    """
    def __init__(self, value):
        """
        creates new class MyInt
        """
        self.__value = value

    def __eq__(self, value2):
        """
        Magic method to check if equal
        Though revere=sed to not equal
        """

        return (self.__value != value2)

    def __ne__(self, value2):
        """
        Magic method for not equal
        Though reversed to equal
        """

        return (self.__value == value2)

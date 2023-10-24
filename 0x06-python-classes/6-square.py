#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """
    Class defining square properties

    Attributes:
        size: size of square side
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Creates a new square instance

        Args:
            __size (int): size of square side
            __position (tuple): square position
        """
        self.__size = size
        self.__position = position

    def area(self):
        """
        Calculates area of a square
        Returns: area of a square
        """
        return(self.__size * self.__size)

    @property
    def size(self):
        """
        Returns the size of a square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Property that sets the size

        Args:
            value (int): size of square side

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Retuns Square position
        """
        return (self.__position)

        @position.setter
        def position(self, value):

            """
            Property setter for position

            Args:
                value (tuple): position of square

            Raises:
            TypeError: position must be a tuple of 2 positive integers
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """

        if self.__size == 0:
            print()
        else:
            for index1 in range(self.__position[1]):
                print()
            for index in range(self.__size):
                for index2 in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))

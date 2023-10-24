#!/usr/bin/python3
"""A class Square that defines a square """


class Square:
    """
    A class which defines properties of a square

    Attributes:
        size: size of square side
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        New square instance

        Args:
            __size (int): size of square side
            __ position (tuple): square's position
        """
        self.__size = size
        self.__position = position

    def area(self):
        """
        Calculates area of a square

        Returns: Area of the square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        Returns: size of square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        sets the size

        Args:
            value (int): size of square size

        Raises:
            TypeError: size must be an integer
            valueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Returns position of square
        """
        return (self.__position)

    @position.setter
    def position(self, value):

        """
        Sets position

        Args:
        value (tuple): square position

        Raises:
            TypeError: position must be a tuple of 2 positive integer
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integer")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integer")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def my_print(self):
        """
        Prints #
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                print("#" * (self.__size))

    def __str__(self):
        """
        prints square placing position with #

        Return: square
        """

        if self.__size == 0:
            return ('')
        next_line = '\n' * self.position[1]
        space = ' ' * self.position[0]
        hsh = '#' * self.size

        return (next_line + '\n'.join(space + hsh for x in range(self. size)))

#!/usr/bin/python3
"""
Class Square
"""

from models.rectangle import Rectangle
from inspect import classify_class_attrs


class Square(Rectangle):
    """
    Square class inherits from Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        creates a new square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        string representation
        of square
        """
        return ("[square] ({}) {:d}/{:d} -{:d}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """
        size getter
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        size setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns argument to
        each attribute
        """
        if args is not None and len(args) != 0:
            my_list_att = ['id', 'size', 'x', 'y']
            for index in range(len(args)):
                if my_list_att[index] == 'size':
                    setattr(self, 'width', args[index])
                    setattr(self, 'height', args[index])
                else:
                    setattr(self, my_list_att[index], args[index])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

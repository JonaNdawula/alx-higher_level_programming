#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """
    A class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Creates a new student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary
        representation of a
        Student instance
        """

        if attrs is None:
            return (self.__dict__)

        my_dict = {}
        i = 0

        while i < len(attrs):
            item = attrs[i]
            try:
                my_dict[item] = self.__dict__[item]
            except Exception:
                pass
            i += 1
        return (my_dict)

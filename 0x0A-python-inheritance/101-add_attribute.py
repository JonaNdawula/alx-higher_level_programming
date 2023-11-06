#!/usr/bin/python3
"""
A function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, name, value):
    """
    Adds  a new attribute to an object if it’s possible

    Raises:
        TypeError: can't add new attribute
    """
    dictionary = "__dict__"
    if not hasattr(obj, dictionary):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

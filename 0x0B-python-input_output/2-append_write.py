#!/usr/bin/python3

"""
Contains a function called append_write
"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end
    of a text file (UTF8) and returns the number
    of characters added
    """
    with open(filename, 'a', encoding="utf-8") as file_name:
        return (file_name.write(text))

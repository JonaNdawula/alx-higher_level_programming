#!/usr/bin/python3
"""
Contains the function write_file
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file
    (UTF8) and returns the number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as file_name:
        return (file_name.write(text))

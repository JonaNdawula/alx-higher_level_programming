#!/usr/bin/python3

"""
Contains function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    A  function that inserts a line of
    text to a file, after each line containing a specific string
    """
    with open(filename, "r") as file_name:
        line = file_name.readlines()

    with open(filename, "w") as optional_file:
        string_rep = ""

        for ln in line:
            string_rep += ln
            if search_string in ln:
                string_rep += new_string

        optional_file.write(string_rep)

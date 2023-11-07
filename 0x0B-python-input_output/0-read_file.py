#!/usr/bin/python3
"""
Contains read_file
"""


def read_file(filename=""):
    """
      Function that reads a text file
     (UTF8) and prints it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as file_name:
        scan_item = file_name.read()
        print(scan_item, end='')

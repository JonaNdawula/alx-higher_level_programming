#!/usr/bin/python3
"""
Contains the function save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A  function that writes an Object to a text file,
    using a JSON representation
    """

    with open(filename, 'w', encoding="utf-8") as file_name:
        my_json_obj = json.dumps(my_obj)

        file_name.write(my_json_obj)
        file_name.close()

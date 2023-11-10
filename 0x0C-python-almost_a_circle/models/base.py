#!/usr/bin/python3
"""
Base class
"""
import json


class Base:
    """
    Defines Properties of Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        creates new Base
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string
        representation of list_dictionaries
        """

        if list_dictionaries is None or list_dictionaries == "[]":
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

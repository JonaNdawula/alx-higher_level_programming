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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation
        of list_objs to a file
        """
        f_name = "{}.json".format(cls.__name__)
        my_dict_list = []

        if not list_objs:
            pass
        else:
            for index in range(len(list_objs)):
                my_dict_list.append(list_objs[index].to_dictionary())

        ls = cls.to_json_string(my_dict_list)

        with open(f_name, 'w') as fl:
            fl.write(ls)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string
        representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return ([])
        else:
            return (json.loads(json_string))

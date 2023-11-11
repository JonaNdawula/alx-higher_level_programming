#!/usr/bin/python3
"""
Base class
"""
import json
import os.path


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

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with
        all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy_data = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_data = cls(1)
        else:
            dummy_data.update(**dictionary)

        return (dummy_data)

    @classmethod
    def load_from_file(cls):
        """
         Returns a list of instances
        """
        f_name = "{}.json".format(cls.__name__)

        if os.path.exists(f_name) is False:
            return ([])

        with open(f_name, 'r') as fl:
            str_ls = fl.read()

        cls_list = cls.from_json_string(str_ls)
        my_list = []

        for index in range(len(cls_list)):
            my_list.append(cls.create(**cls_list[index]))

        return (my_list)

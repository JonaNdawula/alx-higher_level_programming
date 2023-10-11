#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    get_key = a_dictionary.get(key)
    if get_key is not None:
        del a_dictionary[key]
    return (a_dictionary)

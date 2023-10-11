#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_keys = list(a_dictionary.keys())

    for val_in_dict in my_keys:
        if value == a_dictionary.get(val_in_dict):
            del a_dictionary[val_in_dict]
    return (a_dictionary)

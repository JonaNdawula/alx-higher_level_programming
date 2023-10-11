#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dictionary = a_dictionary.copy()
    dictionary_key_list = list(my_dictionary.keys())

    for index in dictionary_key_list:
        my_dictionary[index] *= 2
    return (my_dictionary)

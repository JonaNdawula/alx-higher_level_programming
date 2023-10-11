#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    list_of_keys = list(a_dictionary.keys())
    for index in list_of_keys:
        count += 1
    return (count)

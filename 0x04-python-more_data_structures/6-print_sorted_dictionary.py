#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_key_list = list(a_dictionary.keys())
    ordered_key_list.sort()
    for index in ordered_key_list:
        print("{}:{}".format(index, a_dictionary.get(index)))

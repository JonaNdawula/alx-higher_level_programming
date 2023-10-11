#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mapping = map(lambda item: replace if item == search else item, my_list)
    my_new_list = list(mapping)
    return (my_new_list)

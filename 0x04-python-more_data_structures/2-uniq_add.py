#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_unique_list = set(my_list)

    integer = 0

    for index in my_unique_list:
        integer += index
    return (integer)

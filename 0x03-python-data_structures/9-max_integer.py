#!/usr/bin/python3
def max_integer(my_list=[]):
    list_length = len(my_list)
    if list_length == 0:
        return (None)
    int_big = my_list[0]
    for index in range(list_length):
        if my_list[index] > int_big:
            int_big = my_list[index]
    return (int_big)

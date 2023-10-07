#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0 or idx > (length - 1):
        return (my_list)
    cpy = [item for item in my_list]
    cpy[idx] = element
    return (cpy)

#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    list_length = len(my_list)
    if idx >= 0 and idx < list_length:
        del my_list[idx]
    return (my_list)

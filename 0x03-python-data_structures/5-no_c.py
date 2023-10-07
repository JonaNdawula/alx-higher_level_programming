#!/usr/bin/python3
def no_c(my_string):
    cpy = [item for item in my_string if item != 'c' and item != 'C']
    return ("".join(cpy))

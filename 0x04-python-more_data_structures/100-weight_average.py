#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    integer = 0
    denom = 0

    for struc in my_list:
        integer += struc[0] * struc[1]
        denom += struc[1]
    return (integer / denom)

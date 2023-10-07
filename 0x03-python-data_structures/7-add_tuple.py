#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length1 = len(tuple_a)
    length2 = len(tuple_b)
    if length1 < 2:
        if length1 == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if length2 < 2:
        if length2 == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_a[0], 0
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

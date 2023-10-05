#!/usr/bin/python3
def magic_calculation(a, b):

    from magic_calculation_102 import add, sub
    if a < b:
        add_new = add(a, b)
        for index in range(4, 6):
            add_new = add(add_new, index)
        return (add_new)
    else:
        return(sub(a, b))

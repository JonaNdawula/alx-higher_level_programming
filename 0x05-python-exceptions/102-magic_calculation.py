#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0

    for index in range(1, 3):
        try:
            if index > a:
                raise Exception('Too far')
            res += (a ** b) / index
        except Exception:
            pass
    res = a + b
    return (res)

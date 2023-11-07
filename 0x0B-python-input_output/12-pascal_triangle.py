#!/usr/bin/python3
"""
contains the function pascal_triangle
"""


def pascal_triangle(n):
    """
     A function def pascal_triangle(n):
     that returns a list of lists
     of integers representing the Pascal’s triangle of n
     """
    if n <= 0:
        return ([])
    elif n == 1:
        return([[1]])
    ps = [[1]]
    for i in range(1, n):
        curr_row = [1]
        prev_row = ps[i - 1]

        for j in range(1, i):
            if j < len(prev_row):
                curr_row.append(prev_row[j - 1] + prev_row[j])
            else:
                break

        curr_row.append(1)
        ps.append(curr_row)

    return (ps)

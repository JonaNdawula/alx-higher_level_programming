#!/usr/bin/python3
"""Divides all elements of matrix"""
def matrix_divided(matrix, div):
    """
    A function that divides all elements of a matrix

    Args:
        matrix (list): A list of lists of integers or floats
        div (int or float): divisor

        Raises:
            TypeError: non number values in matrix
            TypeError: rows have different sizes
            TypeError: div not int or float
            ZeroDivisionError: div is 0
    """
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    my_matrix = []
    for row in matrix:
        my_row = []
        for num in row:
            my_row.append(round(num / div, 2))
        my_matrix.append(my_row)

    return (my_matrix)

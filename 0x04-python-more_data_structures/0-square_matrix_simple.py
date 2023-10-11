#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = matrix.copy()

    for index in range(len(matrix)):
        my_matrix[index] = list(map(lambda item: item**2, matrix[index]))
    return (my_matrix)

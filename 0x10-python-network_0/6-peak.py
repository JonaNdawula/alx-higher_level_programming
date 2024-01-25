#!/usr/bin/python3
"""
Finds peak in a list of integers
"""


def find_peak(list_of_integers):
    """
    Finds peak in list of integers
    """
    if list_of_integers:
        left_index = 0
        right_index = len(list_of_integers) - 1
        while left_index < right_index:
            middle_index = (left_index + right_index) // 2
            if list_of_integers[middle_index] > list_of_integers[middle_index + 1]:
                right_index = middle_index
            else:
                left_index = middle_index + 1
        return list_of_integers[left_index]

#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_presence = set_1 ^ set_2
    return (unique_presence)

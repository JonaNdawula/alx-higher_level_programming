#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_length = len(my_list)

    items_in_list = []

    for index in range(list_length):
        if my_list[index] % 2 == 0:
            items_in_list.append(True)
        else:
            items_in_list.append(False)

    return (items_in_list)

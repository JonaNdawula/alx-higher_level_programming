#!/usr/bin/python3
"""
A class called Mylist that inherits from
a base class called list
"""


class MyList(list):
    """
    Mylist inherits from
    base class list
    """
    def print_sorted(self):
        """
        prints sorted list in ascending
        order
        """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)

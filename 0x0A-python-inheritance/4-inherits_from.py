#!/usr/bin/python3
"""
A function that returns True
if the object is an instance of a class that
inherited (directly or indirectly) from the
specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a
    class that inherited (directly or indirectly)
    from the specified class ; otherwise False.

    Returns:
        True or False
    """
    check = type(obj)
    if check is a_class:
        return (False)
    return issubclass(check, a_class)

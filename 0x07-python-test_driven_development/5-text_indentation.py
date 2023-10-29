#!/usr/bin/python3
"""
Prints a text with 2 new lines after: '.', '?' and ':'

Attributes:
        text_indentation: a function that prints a text with 2 new lines after each of these characters: ., ? and :

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after specific characters

    Args:
        text (str): The string to be checked

    Raise:
        TypeError: text must be a string

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for character in ":.?":
        text = (character + "\n\n").join([sentence.strip(" ")
            for sentence in text.split(character)])

    print(text, end="")

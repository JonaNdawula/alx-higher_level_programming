#!/usr/bin/python3
for ascii_letter in range(97, 123):
    if (chr(ascii_letter) != 'q') and (chr(ascii_letter) != 'e'):
        print("{}".format(chr(ascii_letter)), end="")

#!/usr/bin/python3
x = 0
for alph_char in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(alph_char - x)), end="")
    if x == 0:
        x = 32
    else:
        x = 0

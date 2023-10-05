#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    item = len(sys.argv) - 1
    if item == 0:
        print("0 arguments.")
    elif item == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(item))
    for index in range(item):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))

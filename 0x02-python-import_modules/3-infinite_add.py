#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    sum_of_args = 0

    for index in range(len(sys.argv) - 1):
        sum_of_args += int(sys.argv[index + 1])
    print("{}".format(sum_of_args))

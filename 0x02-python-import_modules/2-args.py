#!/usr/bin/python3
#  Prints the number of and the list of its arguments
if __name__ == "__main__":
    import sys

    args = sys.argv
    l_size = len(args) - 1

    if l_size > 1:
        print("{} arguments:".format(l_size))
        for y in range(1, l_size + 1):
            print("{}: {}".format(y, args[y]))

    elif l_size == 0:
        print("{} arguments.".format(l_size))

    else:
        print("{} arguments:".format(l_size))
        print("{}: {}".format(l_size, args[1]))

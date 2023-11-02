#!/usr/bin/python3
def add_arg(argv):
    y = len(argv) - 1
    if y == 0:
        print("{:d}".format(y))
        return
    else:
        z = 1
        total = 0
        while z <= y:
            total += int(argv[z])
            z += 1
        print("{:d}".format(total))

if __name__ == "__main__":
    import sys, math
    add_arg(sys.argv)

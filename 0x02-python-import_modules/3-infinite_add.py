#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    arguments = sys.argv[1:]
    y = 0
    for arg in arguments:
        y += int(arg)
        print((y))

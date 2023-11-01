#!/usr/bin/python3
for y in range(122, 96, -1):
    if y % 2:
        y = y - 32
    print("{:c}".format(y), end="")

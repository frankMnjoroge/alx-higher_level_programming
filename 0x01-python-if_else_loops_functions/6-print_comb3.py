#!/usr/bin/python3
for char in range(9):
    for y in range(char + 1, 10):
        if char * 10 + y < 89:
            print("{:d}{:d}".format(char, y), end=", ")
print("{:d}".format(89))

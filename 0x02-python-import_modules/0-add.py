#!/usr/bin/python3
# Import the add function from the add_0 module
#if __name__ == "__main__":
#    from add_0 import add
#    a = 1
#    b = 2
#    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
a = 1
b = 2
add = __import__('add_0').add

result = add(a, b)

print("{} + {} = {}".format(a, b, result))

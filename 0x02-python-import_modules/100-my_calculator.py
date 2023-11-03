#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv[1:]
    argv_count = len(argv)
    operators = ["+", "-", "*", "/"]
    if argv_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        y = int(sys.argv[1])
        z = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{:d} + {:d} = {:d}".format(y, z, add(y, z)))
        elif sys.argv[2] == "-":
            print("{:d} - {:d} = {:d}".format(y, z, sub(y, z)))
        elif sys.argv[2] == "*":
            print("{:d} * {:d} = {:d}".format(y, z, mul(y, z)))
        elif sys.argv[2] == "/":
            print("{:d} / {:d} = {:d}".format(y, z, div(y, z)))

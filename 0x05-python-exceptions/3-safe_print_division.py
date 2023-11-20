#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divsn = a / b
    except (ZeroDivisionError):
        divsn = None
    finally:
        print("Inside result: {}".format(divsn))
        return divsn

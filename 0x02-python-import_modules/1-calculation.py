#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
# Assign the value 10 to a variable called a
    a = 10
# Assign the value 5 to a variable called b
    b = 5
# Call each of the imported functions and store the results in variables
    add_result = add(a, b)
    sub_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)
# Print the results
    print(f"{a} + {b} = {add_result}")
    print(f"{a} - {b} = {sub_result}")
    print(f"{a} * {b} = {mul_result}")
    print(f"{a} / {b} = {div_result}")

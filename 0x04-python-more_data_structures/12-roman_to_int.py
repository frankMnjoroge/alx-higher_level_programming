#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    data_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [data_value[y] for y in roman_string] + [0]
    result = 0

    for n in range(len(numbers) - 1):
        if numbers[n] >= numbers[n+1]:
            result += numbers[n]
        else:
            result -= numbers[n]

    return result

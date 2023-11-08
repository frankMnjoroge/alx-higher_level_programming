#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temporaly = a_dictionary.copy()
    for y, p in temporaly.items():
        if value == p:
            a_dictionary.pop(y)
    return a_dictionary

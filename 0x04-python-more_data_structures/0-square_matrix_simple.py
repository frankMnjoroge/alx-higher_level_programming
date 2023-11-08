#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for row in matrix:
        squared.append([value**2 for value in row])
    return squared

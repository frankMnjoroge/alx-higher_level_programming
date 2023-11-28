#!/usr/bin/python3
"""Module for matrix_divided method."""
def matrix_divided(matrix, div):
    """divide all elements of matrix by div.
    Args:
        matrix: lists containing int or float
        div: number to divide matrix by
    Returns:
        list: lists representing divided matrix.
    Raises:
        TypeError: If matrix is not list of lists containing int or float.
        TypeError: If sublists are not all same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for rw in matrix:
        if not isinstance(rw, list) or len(rw) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(rw) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for y in rw:
            if not isinstance(y, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(y / div, 2) for y in rw] for rw in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")

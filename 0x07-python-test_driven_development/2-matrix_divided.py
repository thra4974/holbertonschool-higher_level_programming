#!/usr/bin/python3
"""
Module to divide a matrix
"""


def matrix_divided(matrix, div):
    """
    return matrix with divided elements
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    matrix_size = 0
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for data in row:
            if not isinstance(data, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if matrix_size == 0:
            matrix_size = len(row)
        elif matrix_size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    mat_div = [[(data / div) for data in row] for row in matrix]
    return mat_div

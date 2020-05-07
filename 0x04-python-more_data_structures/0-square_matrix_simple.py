#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    matr = []
    for n in matrix:
        matr.append(list(map(lambda x: x * x, n)))
    return matr

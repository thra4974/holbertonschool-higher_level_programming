#!/usr/bin/python3
"""contains pascal_triangle function"""


def pascal_triangle(n):
    """ returns list of lists of integers representing pascals triangle"""
    matr = [[]]
    if n <= 0:
        return matr
    

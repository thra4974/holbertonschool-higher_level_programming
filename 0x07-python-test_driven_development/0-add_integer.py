#!/usr/bin/python3
"""
Add_integer module:
func: add_integrs(a, b)
"""

def add_integer(a, b=98):
    """
    return sum of two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    return a + b

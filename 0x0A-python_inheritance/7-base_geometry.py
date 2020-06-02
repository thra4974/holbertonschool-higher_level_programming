#!/usr/bin/python3
""" Class: BaseGeometry"""


class BaseGeometry:
    """defines class BaseGeometry"""
    def area():
        """
        Raise exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

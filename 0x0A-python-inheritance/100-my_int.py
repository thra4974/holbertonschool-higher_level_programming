#!/usr/bin/python3
"""defines class MyInt"""


class MyInt(int):
    """define MyInt, inherits from int"""

    def __eq__(self, inv):
        """ MyInt inverts =="""
        return int.__ne__(self, inv)

    def __ne__(self, inv):
        """ MyInt inverts !="""
        return int.__eq__(self, inv)

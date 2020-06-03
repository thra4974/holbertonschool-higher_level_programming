#!/usr/bin/python3
"""contains number_of_lines func"""


def number_of_lines(filename=""):
    """ returns number of lines of text file"""
    with open(filename, encoding='utf-8') as f:
        count = len(f.readlines())
        return count

#!/usr/bin/python3
""" contains function write_file"""


def write_file(filename="", text=""):
    """ writes strinf to a text file and returns number of ch written"""
    with open(filename, 'w+', encoding='utf-8') as f:
        return f.write(text)

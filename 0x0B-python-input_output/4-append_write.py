#!/usr/bin/python3
""" contains function append_write"""


def append_write(filename="", text=""):
    """appends text to end of file"""
    with open(filename, 'a+', encoding='utf-8') as f:
        return f.write(text)

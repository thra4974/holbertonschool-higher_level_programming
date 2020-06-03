#!/usr/bin/python3
"""contains append_after function"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r+', encoding='utf-8') as f:
        buf = []
        for readline in f:
            buf.append(readline)
            if search_string in readline:
                """look for search string and append new string if found"""
                buf.append(new_string)
            """reset ref point to beginning of file"""
            f.seek(0)
            for readline in buf:
                f.write(readline)

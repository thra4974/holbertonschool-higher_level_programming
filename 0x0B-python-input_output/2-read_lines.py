#!/usr/bin/python3
""" contains read_lines function"""


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file and prints to stdout"""
    with open(filename, encoding='utf-8') as f:
        lines = f.readline()
        size = len(f.readlines())
        f.seek(0)
        if nb_lines > 0 and nb_lines < size:
            for n in range(nb_lines):
                print(lines, end="")
                n += 1
        else:
            for line in f:
                print(line, end="")

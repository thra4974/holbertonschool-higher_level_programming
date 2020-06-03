#!/usr/bin/python3
""" Contains read_file function"""


def read_file(filename=""):
    """ reads text file (UTF8) and prints to stdout"""
    with open(filename, 'r') as f:
        print(f.read())

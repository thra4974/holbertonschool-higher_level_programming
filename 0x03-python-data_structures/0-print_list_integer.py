#!/usr/bin/python3


def print_list_integer(my_list=[]):

    li = ''.join(str(n) for n in my_list)
    for n in li:
        print(str.format(n))

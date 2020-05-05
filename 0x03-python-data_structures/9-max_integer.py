#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        for n in range(0, len(my_list)):
            if my_list[n] > my_list[0]:
                return (my_list[n])

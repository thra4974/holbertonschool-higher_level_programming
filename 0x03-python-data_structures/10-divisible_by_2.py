#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    divlist = []
    for n in my_list:
        if n % 2 == 0:
            divlist.append(True)
        else:
            divlist.append(False)
    return divlist

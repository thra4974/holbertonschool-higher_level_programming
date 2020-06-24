#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        maxn = my_list[0]
        if len(my_list) == 0:
            return None
        else:
            for n in range(0, len(my_list)):
                if my_list[n] > maxn:
                    maxn = my_list[n]
            return maxn

#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = dict()
    for key, values in a_dictionary.items():
        new_dict[key] = 2 * values
    return new_dict

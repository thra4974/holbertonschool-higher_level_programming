#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_items = list(a_dictionary.items())
    if a_dictionary is not None:
        for key, values in dict_items:
            if values == value:
                del a_dictionary[key]
    return a_dictionary

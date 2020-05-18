#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        new_list = my_list[:x]
        str1 = ''.join(str(n) for n in new_list)
        print("{}".format(str1))
        for n in str1:
            count += 1
        return (count)
    except:
        print("Failed to print list")

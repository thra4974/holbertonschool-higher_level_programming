#!/usr/bin/python3
def uppercase(str):

    res = ''
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            res += chr(ord(c) - 32)
        else:
            res += chr(ord(c))
    print("{}".format(res))

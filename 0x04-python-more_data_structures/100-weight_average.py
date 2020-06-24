#!/usr/bin/python3
def weight_average(my_list=[]):
    pt = 0
    ttl = 0
    if my_list:
        con = ()
        for con in my_list:
            pt += (con[0] * con[1])
            ttl += con[1]
        return pt / ttl
    else:
            return 0

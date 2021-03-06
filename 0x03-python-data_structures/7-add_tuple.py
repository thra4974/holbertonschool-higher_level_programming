#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        return tuple_b
    elif len(tuple_b) == 0:
        return tuple_a
    elif len(tuple_a) > 2 and len(tuple_b) < 2:
        return tuple_a[1]
    else:
        return tuple(map(lambda x, y: x + y, tuple_a, tuple_b))

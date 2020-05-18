#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        res = str(a / b)
    except (ZeroDivisionError, TypeError, ValueError):
        res = None
    finally:
        print("Inside result: {}".format(res))
    return res

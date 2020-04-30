#!/usr/bin/python3
import sys


def main():
    args = sys.argv[1:]
    length = len(args)
    res = 0
    for arg in args:
        res += int(arg)
    print("{:d}".format(res))

if __name__ == "__main__":

    main()

#!/usr/bin/python3
import sys


def main():
    argv = sys.argv
    args = argv[1:]
    length = len(args)
    if length == 0:
        print("{:d} arguments.".format(length))
    elif length == 1:
        for arg in args:
            print("{:d} argument:".format(length))
            print("{:d}: {}".format(argv.index(arg), arg))
    elif length > 1:
        print("{:d} arguments:".format(length))
        for arg in args:
            print("{:d}: {}".format(argv.index(arg), arg))

if __name__ == "__main__":

    main()

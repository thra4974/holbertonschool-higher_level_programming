#!/usr/bin/python3
import hidden_4


def main():
    names = dir(hidden_4)
    for arg in names:
        if arg[0] == '_':
            pass
        else:
            print("{}".format(arg))

if __name__ == "__main__":

    main()

#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    args = len(argv)

    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    res = 0

    if operator == "+":
        res = add(a, b)

    elif operator == "-":
        res = sub(a, b)

    elif operator == "*":
        res = mul(a, b)

    elif operator == "/":
        div(a, b)

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {} {:d} = {:d}".format(a, operator, b, res))

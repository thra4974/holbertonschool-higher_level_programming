#!/usr/bin/python3
for n in range(ord('z'), ord('`'), -1):
    if n % 2 == 0:
        n = chr(n).lower()
    else:
        n = chr(n).upper()
    print("{}".format(n), end='')

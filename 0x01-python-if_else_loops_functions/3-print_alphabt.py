#!/usr/bin/python3
for letter in range(ord('a'), ord('z')):
    if chr(letter) is 'q' or chr(letter) is 'e':
        pass
    else:
        print("{}".format(chr(letter)), end='')

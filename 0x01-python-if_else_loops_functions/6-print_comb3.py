#!/usr/bin/python3
for n in range(1, 100):
    if n // 10 == n % 10:
        pass
    elif (n - ((n%10)*(10)) + (n//10))%3 == 0 and (n - ((n%10)*(10)) + (n//10)) > 0:
        print("nope")
    else:
        print("{0:0=2d}, ".format((n)), end='')

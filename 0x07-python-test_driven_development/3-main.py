#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Tristan", "Thrasher")
say_my_name("Elena", "Khoury")
say_my_name("Noon")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

#!/usr/bin/python3
"""script with add_args func"""
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


f = "add_item.json"
try:
    my_list= load_from_json_file(f)
except:
    my_list=[]
for arg in argv[1:]:
    my_list.append(arg)
save_to_json_file(my_list, f)

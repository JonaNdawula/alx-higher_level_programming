#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file
"""
from sys import argv

save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file
i = 1

try:
    new_json_list = load_file('add_item.json')
except (ValueError, FileNotFoundError):
    new_json_list = []

while i < len(argv):
    new_json_list.append(argv[i])
    i += 1

save_file(new_json_list, 'add_item.json')

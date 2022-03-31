#!/usr/bin/python3
"""
Script that updates a list with json representation
"""

from sys import argv
save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    list_arg = load_json(filename)
except:
    list_arg = []

with open(filename, 'w', encoding="utf-8") as f:
    for arg in argv[1:]:
        list_arg.append(arg)
        save_json(list_arg, filename)

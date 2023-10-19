#!/usr/bin/python3
"""creates an Object from a “JSON file”"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file = "add_item.json"
args = sys.argv

with open(file, "a+", encoding="utf-8") as f:
    my_list = []
    my_list = args[1:]
    save_to_json_file(my_list, file)
    load_from_json_file(file)

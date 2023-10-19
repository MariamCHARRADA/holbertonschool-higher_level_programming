#!/usr/bin/python3
"""creates an Object from a “JSON file”"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file = "add_item.json"
args = sys.argv

mylist = args[1:]
save_to_json_file(mylist, file)
load_from_json_file(file)

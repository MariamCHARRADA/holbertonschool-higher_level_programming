#!/usr/bin/python3
"""creates an Object from a “JSON file”"""
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
args = sys.argv

try:
    my_list = load_from_json_file(filename)
except:
    my_list = []

for i in range(1, len(args)):
    my_list.append(args[i])

save_to_json_file(my_list, filename)

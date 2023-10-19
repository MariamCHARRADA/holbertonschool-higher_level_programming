#!/usr/bin/python3
"""creates an Object from a “JSON file”"""
import sys
from os.path import isfile

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
args = sys.argv

if isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []
    
my_list.append(args[1:])
save_to_json_file(my_list, filename)
print(my_list)

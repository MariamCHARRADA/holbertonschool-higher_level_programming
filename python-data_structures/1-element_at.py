#!/usr/bin/python3
def element_at(my_list, idx):
    if idx in range(len(my_list)) and idx > 0:
        return my_list[idx]
    else:
        return None

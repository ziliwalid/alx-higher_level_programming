#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    x = len(my_list)
    list_cpy = my_list.copy()
    if idx < 0:
        return list_cpy
    elif idx > x - 1:
        return list_cpy
    else:
        list_cpy[idx] = element
        return list_cpy

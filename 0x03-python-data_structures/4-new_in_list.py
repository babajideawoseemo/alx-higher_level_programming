#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    jide_list = my_list[:]
    if 0 <= idx < len(my_list):
        jide_list[idx] = element
        return(jide_list)
    return(my_list)

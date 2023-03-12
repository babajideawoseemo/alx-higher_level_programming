#!/usr/bin/python3
def replace_in_list(jide_list, ide, element):
    if ide < 0 or ide > len(jide_list) - 1:
        return jide_list
    else:
        jide_list[ide] = element
        return jide_list

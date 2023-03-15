#!/usr/bin/python3

def search_replace(my_list, search, replace):
    jidecopy = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            jidecopy.append(replace)
        else:
            jidecopy.append(my_list[i])
    return jidecopy

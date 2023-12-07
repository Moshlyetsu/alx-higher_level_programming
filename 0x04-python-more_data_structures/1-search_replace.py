#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_list = list(my_list)
    for x in range(len(nw_list)):
        if nw_list[x] == search:
            nw_list[x] = replace
    return nw_list

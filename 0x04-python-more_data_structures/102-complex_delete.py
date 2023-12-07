#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for srchd_key in list(a_dictionary):
        if a_dictionary[srchd_key] == value:
            del a_dictionary[srchd_key]
    return a_dictionary

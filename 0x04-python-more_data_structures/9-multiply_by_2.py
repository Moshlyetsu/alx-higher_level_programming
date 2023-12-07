#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictnry = {}
    for x in a_dictionary:
        new_dictnry[x] = a_dictionary[x] * 2
    return new_dictnry

#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lst_nmbr = (-number % 10)
    elif number >= 0:
        lst_nmbr = number % 10
    print("{}".format(lst_nmbr), end="")
    return lst_nmbr

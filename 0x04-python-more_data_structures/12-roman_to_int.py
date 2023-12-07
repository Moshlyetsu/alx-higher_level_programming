#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    roman_dffntion = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_nw = 0

    for r in range(len(roman_string)):
        if r > 0 and roman_dffntion[roman_string[r]] > roman_dffntion[roman_string[r - 1]]:
            roman_nw += roman_dffntion[roman_string[r]] - 2 * \
                        roman_dffntion[roman_string[r - 1]]
        else:
            roman_nw += roman_dffntion[roman_string[r]]
    return roman_nw

#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return (0)
    if not roman_string:
        return (0)

    rom_di = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_dict_keys = list(rom_di.keys())

    integer = 0
    last_r_num = 0
    number_list = [0]

    for char in roman_string:
        for roman in roman_dict_keys:
            if roman == char:
                if rom_di.get(char) <= last_r_num:
                    integer += subtract(number_list)
                    number_list = [rom_di.get(char)]
                else:
                    number_list.append(rom_di.get(char))

                last_r_num = rom_di.get(char)
    integer += subtract(number_list)

    return (integer)


def subtract(number_list):
    sub = 0
    max_list = max(number_list)

    for integer in number_list:
        if max_list > integer:
            sub += integer
    return (max_list - sub)

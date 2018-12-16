#!/usr/bin/python3
def roman_to_int(roman_string):
    index = 0
    result = 0
    if isinstance(roman_string, str):
        rdict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
        for index in range(len(roman_string)):
            k = roman_string[index]
            if k in rdict:
                if index < len(roman_string) - 1:
                    p = roman_string[index + 1]
                    if rdict[k] < rdict[p]:
                        result -= rdict[k]
                    else:
                        result += rdict[k]
                else:
                    result += rdict[k]
    return result

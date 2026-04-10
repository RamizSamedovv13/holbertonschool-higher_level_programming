#!/usr/bin/python3
def roman_to_int(roman_string):
    RomanChar = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    if not roman_string:
        return 0
    prev_value = 0
    total = 0
    for char in reversed(roman_string):
        value = RomanChar.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value
    return total

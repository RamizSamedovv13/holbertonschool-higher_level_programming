#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_numbers = []

    for num in my_list:
        if num not in unique_numbers:
            unique_numbers.append(num)

    total = 0
    for num in unique_numbers:
        total += num

    return total

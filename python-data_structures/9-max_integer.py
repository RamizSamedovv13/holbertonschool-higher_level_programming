#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_value = my_list[0]

    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value


if __name__ == "__main__":
    print(max_integer([3, 10, 2, 7]))
    print(max_integer([-5, -2, -10]))
    print(max_integer([]))

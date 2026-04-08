#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []

    for num in my_list:
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list


if __name__ == "__main__":
    print(divisible_by_2([0, 1, 2, 3, 4, 5, 6]))
    print(divisible_by_2([]))

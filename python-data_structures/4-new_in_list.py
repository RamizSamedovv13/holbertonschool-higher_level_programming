#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = my_list[:]  

    if idx < 0 or idx >= len(my_list):
        return new_list

    new_list[idx] = element
    return new_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    new_list = new_in_list(my_list, 2, 99)

    print("Original list:", my_list)
    print("New list:", new_list)

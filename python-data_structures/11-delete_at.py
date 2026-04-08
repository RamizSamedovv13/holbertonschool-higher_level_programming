#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]
    return my_list


if __name__ == "__main__":
    my_list = [10, 20, 30, 40, 50]

    print(delete_at(my_list, 2))
    print(delete_at(my_list, 10))
    print(delete_at(my_list, -1))

#!/usr/bin/python3
def uppercase(str):

    new_str = ""

    for char in str:
        if ord(char) >= 97 or ord(char) > 122:
            new_str += chr(ord(char) - 32)
        else:
            new_str += char

    print("{}".format(new_str))

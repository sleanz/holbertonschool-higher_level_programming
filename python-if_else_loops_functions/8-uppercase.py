#!/usr/bin/python3
def uppercase(str):
    """
    Function that prints a string in uppercase followed by a new line
    """
    result = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
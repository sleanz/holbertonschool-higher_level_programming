#!/usr/bin/python3
def islower(c):
    """
    Function that checks if a character is lowercase
    Returns True if c is lowercase, False otherwise
    """
    # ASCII values for lowercase letters a-z are 97-122
    return ord('a') <= ord(c) <= ord('z')
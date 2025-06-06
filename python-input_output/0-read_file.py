#!/usr/bin/python3
"""
Module containing the read_file function
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout
    
    Args:
        filename (str): The name of the file to read (default: empty string)
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')


#!/usr/bin/python3
"""
This module contains a function to get all attributes and methods of an object
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    
    Args:
        obj: Any Python object
        
    Returns:
        list: A list of strings containing all available attributes and methods
    """
    return dir(obj)

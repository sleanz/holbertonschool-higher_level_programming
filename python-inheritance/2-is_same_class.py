#!/usr/bin/python3
"""
This module contains a function to check if an object is exactly 
an instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.
    
    Args:
        obj: Any Python object
        a_class: A class to check against
        
    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise
    """
    return type(obj) is a_class

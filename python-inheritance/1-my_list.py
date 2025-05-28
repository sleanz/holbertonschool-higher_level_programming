#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list
"""


class MyList(list):
    """
    A class that inherits from list with additional functionality
    """
    
    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        Does not modify the original list
        """
        print(sorted(self))

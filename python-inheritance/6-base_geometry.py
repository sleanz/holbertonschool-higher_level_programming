#!/usr/bin/python3
"""
Module that defines the BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class with area method
    """
    
    def area(self):
        """
        Public instance method that raises an Exception
        
        Raises:
            Exception: Always raises with message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

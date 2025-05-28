#!/usr/bin/python3
"""
Module that defines the BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class with area method and integer validator
    """
    
    def area(self):
        """
        Public instance method that raises an Exception
        
        Raises:
            Exception: Always raises with message "area() is not implemented"
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0
        
        Args:
            name (str): The name of the parameter being validated
            value: The value to validate
            
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

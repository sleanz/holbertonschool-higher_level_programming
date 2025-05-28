#!/usr/bin/python3
"""
Module that defines the Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """
    
    def __init__(self, size):
        """
        Initialize Square with size
        
        Args:
            size (int): Size of the square (must be positive integer)
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    
    def __str__(self):
        """
        Return string representation of the square
        
        Returns:
            str: Square description in format [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

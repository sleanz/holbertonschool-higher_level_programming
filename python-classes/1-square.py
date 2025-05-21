#!/usr/bin/python3
"""Square module for defining a square class"""


class Square:
    """Class that defines a square

    Attributes:
        __size (int): Private instance attribute for the size of the square
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: Size of the square (no type/value verification)
        """
        self.__size = size

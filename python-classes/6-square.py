#!/usr/bin/python3
"""Square module for defining a square class"""


class Square:
    """Class that defines a square

    Attributes:
        __size (int): Private instance attribute for the size of the square
        __position (tuple): Private instance attribute for the position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int, optional): Size of the square. Defaults to 0.
            position (tuple, optional): Position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square.

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size for the square

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square.

        Returns:
            tuple: The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position for the square

        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square (size squared)
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters.

        If size is 0, prints an empty line.
        Position is used to determine the starting position of the square:
        - position[0] determines the horizontal offset (spaces before each row)
        - position[1] determines the vertical offset (new lines before the square)
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print the square with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

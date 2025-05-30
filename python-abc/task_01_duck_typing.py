#!/usr/bin/env python3
"""
Module that defines abstract Shape class and its concrete implementations.

This module demonstrates the use of abstract base classes and duck typing
for geometric shapes with area and perimeter calculations.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    
    This class defines the interface that all shape subclasses must implement.
    All shapes must be able to calculate their area and perimeter.
    """
    
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        
        Returns:
            float: The area of the shape.
        """
        pass
    
    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        
        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape.
    
    Represents a circle with a given radius and implements
    area and perimeter calculations.
    """
    
    def __init__(self, radius):
        """
        Initialize a Circle with the given radius.
        
        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π * r²).
        """
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.
        
        Returns:
            float: The perimeter of the circle (2 * π * r).
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.
    
    Represents a rectangle with given width and height and implements
    area and perimeter calculations.
    """
    
    def __init__(self, width, height):
        """
        Initialize a Rectangle with the given width and height.
        
        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (width * height).
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        
        Returns:
            float: The perimeter of the rectangle (2 * (width + height)).
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print information about a shape using duck typing.
    
    This function relies on duck typing - it assumes the passed object
    has area() and perimeter() methods without explicitly checking its type.
    
    Args:
        shape: Any object that implements area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# Testing the implementation
if __name__ == "__main__":
    # Create instances of Circle and Rectangle
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    
    print("Circle with radius 5:")
    shape_info(circle)
    
    print("\nRectangle with width 4 and height 6:")
    shape_info(rectangle)

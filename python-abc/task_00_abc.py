#!/usr/bin/env python3
"""
Module that defines abstract Animal class and its concrete subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.
    
    This class defines the interface that all animal subclasses must implement.
    """
    
    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        
        Returns:
            str: The sound that the animal makes.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.
    
    Implements the sound method to return the sound a dog makes.
    """
    
    def sound(self):
        """
        Return the sound a dog makes.
        
        Returns:
            str: "Bark" - the sound of a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.
    
    Implements the sound method to return the sound a cat makes.
    """
    
    def sound(self):
        """
        Return the sound a cat makes.
        
        Returns:
            str: "Meow" - the sound of a cat.
        """
        return "Meow"

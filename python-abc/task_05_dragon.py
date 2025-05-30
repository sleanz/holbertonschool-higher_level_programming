#!/usr/bin/env python3
"""
Module that demonstrates the use of mixins for composable behavior.

This module defines mixin classes that provide specific behaviors
and shows how they can be combined to create complex objects
without deep inheritance hierarchies.
"""


class SwimMixin:
    """
    Mixin class that provides swimming behavior.
    
    This mixin can be combined with other classes to give them
    the ability to swim.
    """
    
    def swim(self):
        """
        Method that makes the creature swim.
        
        Prints a message indicating that the creature is swimming.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying behavior.
    
    This mixin can be combined with other classes to give them
    the ability to fly.
    """
    
    def fly(self):
        """
        Method that makes the creature fly.
        
        Prints a message indicating that the creature is flying.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits from both SwimMixin and FlyMixin.
    
    This class demonstrates multiple inheritance using mixins,
    combining swimming and flying abilities with dragon-specific behavior.
    """
    
    def roar(self):
        """
        Method specific to dragons that makes them roar.
        
        Prints a message indicating that the dragon is roaring.
        """
        print("The dragon roars!")


# Testing the implementation
if __name__ == "__main__":
    # Create an instance of Dragon
    draco = Dragon()
    
    # Demonstrate the dragon's abilities from mixins
    print("Testing Dragon abilities:")
    draco.swim()  # From SwimMixin
    draco.fly()   # From FlyMixin
    draco.roar()  # Dragon-specific method

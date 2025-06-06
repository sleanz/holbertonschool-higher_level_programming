#!/usr/bin/env python3
"""
Custom object serialization module using pickle.
"""

import pickle


class CustomObject:
    """
    A custom class to demonstrate serialization and deserialization using pickle.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.
        
        Args:
            name (str): The name of the person
            age (int): The age of the person
            is_student (bool): Whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of the object and save it to a file.
        
        Args:
            filename (str): The filename to save the serialized object to
        
        Returns:
            None if an error occurs during serialization
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return an instance of CustomObject from a file.
        
        Args:
            filename (str): The filename to load the serialized object from
        
        Returns:
            CustomObject: The deserialized object, or None if an error occurs
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError, Exception):
            return None

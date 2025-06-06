#!/usr/bin/python3

class Student:
    """
    Student class that defines a student with serialization/deserialization capabilities.
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age.
        
        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        
        Args:
            attrs (list): List of attribute names to retrieve. If None, all attributes are retrieved.
        
        Returns:
            dict: Dictionary containing specified attributes of the Student instance
        """
        if attrs is None:
            return self.__dict__
        
        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        
        return result

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        
        Args:
            json (dict): Dictionary containing attribute names as keys and their values
        """
        for key, value in json.items():
            setattr(self, key, value)

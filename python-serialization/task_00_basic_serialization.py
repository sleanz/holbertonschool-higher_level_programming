#!/usr/bin/env python3
"""
Basic serialization module for Python dictionaries to JSON files.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    
    Args:
        data (dict): A Python Dictionary with data to serialize
        filename (str): The filename of the output JSON file
                       If the file exists, it will be replaced
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file to recreate a Python Dictionary.
    
    Args:
        filename (str): The filename of the input JSON file
    
    Returns:
        dict: Python Dictionary with the deserialized JSON data from the file
    """
    with open(filename, 'r') as file:
        return json.load(file)

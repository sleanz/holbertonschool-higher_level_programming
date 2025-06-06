#!/usr/bin/python3

import json

def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".
    
    Args:
        filename (str): The name of the JSON file to read from
    
    Returns:
        object: Python data structure loaded from the JSON file
    """
    with open(filename, 'r') as file:
        return json.load(file)

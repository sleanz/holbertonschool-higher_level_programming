#!/usr/bin/env python3
"""
CSV to JSON conversion module using serialization techniques.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert data from a CSV file to JSON format and save it to 'data.json'.
    
    Args:
        csv_filename (str): The name of the CSV file to convert
    
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        data_list = []
        
        with open(csv_filename, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            for row in csv_reader:
                data_list.append(row)
        
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)
        
        return True
        
    except FileNotFoundError:
        return False
    except Exception:
        return False

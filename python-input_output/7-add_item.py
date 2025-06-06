#!/usr/bin/python3

import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Try to load existing list from file, if it doesn't exist, start with empty list
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

# Add all command line arguments to the list (excluding script name)
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)

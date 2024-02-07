#!/usr/bin/python3

"""
A script that adds all arguments to a Python list and then saves them to a JSON file.
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def update_json_file(args, json_file: str = "add_item.json") -> None:
    """
    Adds command-line arguments to a Python list and then saves them to a JSON file.

    Args:
        args (list): A list of command-line arguments.
        json_file (str): The name of the JSON file to write to. Defaults to "add_item.json".
    """
    # Initialize an empty Python list
    py_list = []

    # Attempt to load existing data from the JSON file
    try:
        py_list = load_from_json_file(json_file)
    except FileNotFoundError:
        pass  ''' File doesn't exist yet, so we'll create it later'''

    '''Add command-line arguments to the Python list'''
    py_list.extend(args)

    ''' Save the updated Python list to the JSON file'''
    save_to_json_file(py_list, json_file)

if __name__ == "__main__":
    update_json_file(sys.argv[1:])


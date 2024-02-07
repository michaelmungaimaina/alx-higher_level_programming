#!/usr/bin/python3

def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a JSON file.

    Args:
        my_obj (any): The Python object to save.
        filename (str): The name of the file to save to.

    Returns:
        None
    """
    import json
    with open(filename, mode="w", encoding="utf-8") as fd:
        json.dump(my_obj, fd)


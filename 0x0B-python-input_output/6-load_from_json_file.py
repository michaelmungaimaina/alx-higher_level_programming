#!/usr/bin/python3

def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        any: The Python object loaded from the JSON file.
    """
    import json
    with open(filename, encoding="utf-8") as fd:
        return json.load(fd)

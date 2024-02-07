#!/usr/bin/python3
import json


def load_from_json_file(filename: str) -> object:
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        any: The Python object loaded from the JSON file.
    """

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

#!/usr/bin/python3

def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        any: The Python object represented by the JSON string.
    """
    import json
    return json.loads(my_str)


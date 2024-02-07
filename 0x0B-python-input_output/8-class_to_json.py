#!/usr/bin/python3

def class_to_json(obj):
    """
    Converts a class instance to a dictionary representation.

    Args:
        obj (object): The object to convert.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    return obj.__dict__


#!/usr/bin/python3

def add_attribute(obj, a, v):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj (object): The object to which the attribute will be added.
        a (str): The name of the attribute to add.
        v (any): The value of the attribute to add.

    Raises:
        TypeError: If the object already has a '__dict__' attribute,
                   indicating it's not possible to add new attributes.

    Returns:
        None
    """
    if hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, a, v)


#!/usr/bin/python3
def best_score(my_dict):
    """
    A function that returns a key with the biggest integer value.
    """
    return max(my_dict, key=my_dict.get) if my_dict else None

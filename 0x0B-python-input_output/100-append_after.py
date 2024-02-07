#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Appends a new string after each occurrence of a search string in a file.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in the file.
        new_string (str): The string to append after each occurrence of the search string.

    Returns:
        None
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        new_lines = []

        for line in lines:
            new_lines.append(line)

            if search_string in line:
                new_lines.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as nf:
        for line in new_lines:
            nf.write(line)


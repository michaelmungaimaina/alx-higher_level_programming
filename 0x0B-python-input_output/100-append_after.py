#!/usr/bin/python3

"""
A module with a function to append text to a file after each line containing a
specific string.
"""


def append_after(
    filename: str = "", search_string: str = "", new_string: str = ""
) -> None:
    """
    Appends a line of text to a file after each line containing a specific
    string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to append after each line containing the
        search string.

    Returns:
        None
    """
    with open(filename, "r+", encoding="utf-8") as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            if search_string in line:
                lines[i] += new_string

        file.seek(0)
        file.writelines(lines)

#!/usr/bin/python3


def read_file(filename: str = "") -> None:
    """
    Reads and prints the content of a file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """

    with open(filename, "r", encoding="utf-8") as fd:
        for line in fd:
            print(line, end="")

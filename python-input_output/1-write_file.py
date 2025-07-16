#!/usr/bin/python3
"""
This module provides a function to write a string to a text file (UTF8)\
        and returns the number of characters written.

Function:
    write_file(filename="", text=""): Writes the specified text to \
            the specified file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of \
            characters written.

    Args:
        filename (str): The name of the file to write to. Default is an empty\
                string.
        text (str): The text to write to the file. Default is an empty string.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)

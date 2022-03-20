#!/usr/bin/python3
"""Module for write_file function."""


def write_file(filename="", text=""):
    """This function writes a string to a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        written = f.write(text)
        """Write return the total number of characters inserts in the file."""
        return written

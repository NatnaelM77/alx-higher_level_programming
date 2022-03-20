#!/usr/bin/python3
"""Module for append_write function."""


def append_write(filename="", text=""):
    """This function appends a strings at the end of a text file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

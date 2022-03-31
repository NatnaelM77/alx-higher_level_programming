#!/usr/bin/python3
"""
Module 0-read_file.py
"""


def read_file(filename=""):
    """This function reads a text file(UTF-8) and prints to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")

#!/usr/bin/python3
"""
This module contains a function to read and print a UTF-8 text file.
"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

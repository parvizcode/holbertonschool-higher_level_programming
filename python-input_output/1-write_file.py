#!/usr/bin/python3
"""Module for writing to files."""

def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns num of chars written.
    
    Args:
        filename (str): Name of file to write to
        text (str): Text to write to the file
    
    Returns:
        int: Number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

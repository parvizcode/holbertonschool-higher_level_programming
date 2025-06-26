#!/usr/bin/python3
"""This module provides a function to list
an object's attributes and methods."""


def lookup(obj):
    """Returns the list of available attributes
    and methods of an object.

    Args:
        obj: The object to inspect

    Returns:
        list: A list of strings representing
        the object's attributes and methods
    """
    return dir(obj)

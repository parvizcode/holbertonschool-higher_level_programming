#!/usr/bin/python3
"""A module for checking exact class instances

This module provides a function to determine if an object
is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """Check if object is exactly an instance of the specified class

    Args:
        obj: Any Python object to check
        a_class: The class to compare against

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise

    Examples:
        >>> is_same_class(1, int)
        True
        >>> is_same_class(1, object)
        False
    """
    return type(obj) is a_class

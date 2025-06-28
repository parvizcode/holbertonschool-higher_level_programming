#!/usr/bin/python3
"""Module for checking object class type"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of or inherited from
    the specified class

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        bool: True if obj is an instance of a_class or
        its subclass, False otherwise
    """
    return isinstance(obj, a_class)

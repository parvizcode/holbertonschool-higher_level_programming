#!/usr/bin/python3
"""
This module defines a function to add attributes to objects
if possible, raising a TypeError otherwise.
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible.

    Raises:
        TypeError: If the object cannot have new attributes added.
    """
    if hasattr(obj, '__slots__'):
        if attr_name not in obj.__slots__:
            raise TypeError("can't add new attribute")
    elif not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)

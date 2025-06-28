#!/usr/bin/python3
"""Module for adding attributes to objects if possible."""

def add_attribute(obj, name, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to add an attribute to
        name (str): Name of the new attribute
        value: Value of the new attribute

    Raises:
        TypeError: If the object can't have new attributes
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    elif hasattr(type(obj), '__slots__') and name not in type(obj).__slots__:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)

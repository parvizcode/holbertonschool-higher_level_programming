#!/usr/bin/python3
"""
This module defines a function that adds a new attribute to an object
if it is possible. Raises a TypeError if the attribute cannot be added.
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute should be added.
        attr_name: The name of the attribute to add.
        attr_value: The value of the attribute to add.

    Raises:
        TypeError: If the object does not support adding new attributes.
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)

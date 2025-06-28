#!/usr/bin/python3
"""
This module defines a function that adds a new attribute to an object if possible.
"""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute should be added.
        attr_name: The name of the attribute.
        attr_value: The value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")

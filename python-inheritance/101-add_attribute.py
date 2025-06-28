#!/usr/bin/python3
def add_attribute(obj, name, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to add an attribute to
        name: Name of the new attribute
        value: Value of the new attribute

    Raises:
        TypeError: If the object can't have new attributes
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)

#!/usr/bin/python3

"""
This module defines is_kind_of_class.
It checks if an object is an instance of a class or a class that inherited from it.
"""

def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance or inherits from a_class; otherwise False."""
    return isinstance(obj, a_class)

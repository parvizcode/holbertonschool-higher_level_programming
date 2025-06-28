#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def __dir__(self):
        """Custom dir() implementation that excludes
        __init_subclass__ attribute.
        """
        attributes = dir(type(self))
        return [attr for attr in attributes 
                if attr != '__init_subclass__']

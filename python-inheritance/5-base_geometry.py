#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def __dir__(self):
        """Customize dir() output by excluding __init_subclass__"""
        return [attr for attr in dir(type(self)) if attr != '__init_subclass__']

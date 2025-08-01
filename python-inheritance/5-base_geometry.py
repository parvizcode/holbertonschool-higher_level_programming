#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def __dir__(self):
        """Customize dir() output to include all default attributes"""
        return sorted(dir(type(self)))

#!/usr/bin/python3
"""
This module defines MyInt class that inherits from int and
inverts == and != operators.
"""


class MyInt(int):
    """MyInt is a rebel, inverts == and !=."""

    def __eq__(self, other):
        """Invert equality: return True if not equal."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert inequality: return True if equal."""
        return super().__eq__(other)

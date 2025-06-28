#!/usr/bin/python3
"""Module that defines MyList class inheriting from list."""

class MyList(list):
    """A custom list that can print itself sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying the original list."""
        print(sorted(self))

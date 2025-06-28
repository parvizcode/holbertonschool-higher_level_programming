#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list.
"""


class MyList(list):
    """
    MyList class that inherits from list and adds a print_sorted method.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        print(sorted(self))

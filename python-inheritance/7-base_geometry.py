#!/usr/bin/python3
"""Module containing BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with area and integer_validator methods"""
    
    def area(self):
        """Raises an Exception indicating area() is not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates that value is a positive integer
        
        Args:
            name (str): name of the value being validated
            value (int): value to validate
            
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

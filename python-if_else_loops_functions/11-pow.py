#!/usr/bin/python3
def pow(a, b):
    """Return a to the power of b"""
    result = 1
    if b >= 0:
        for _ in range(b):
            result *= a
    else:
        for _ in range(-b):
            result /= a
    return result

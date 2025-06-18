#!/usr/bin/python3
def pow(a, b):
    """Compute a to the power of b with precise results"""
    if b == 0:
        return 1
    if b < 0:
        return 1 / pow(a, -b)
    result = 1
    for _ in range(b):
        result *= a
    return result

#!/usr/bin/python3
def pow(a, b):
    """Return a to the power of b with precise floating point"""
    result = 1.0  # Use float for precise division
    if b == 0:
        return 1
    abs_b = abs(b)
    for _ in range(abs_b):
        result *= a
    return 1 / result if b < 0 else result

#!/usr/bin/python3
output = "".join(chr(c) for c in range(97, 123) if c not in [101, 113])
print("{0}".format(output), end="")

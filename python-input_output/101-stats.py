#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:
- Total file size
- Count of status codes
"""

import sys

def print_stats(total_size, status_codes):
    """Prints the accumulated metrics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

total_size = 0
status_codes = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()

        # Extract file size
        if len(parts) >= 2:
            try:
                size = int(parts[-1])
                total_size += size
            except ValueError:
                pass

        # Extract status code
        if len(parts) >= 2:
            code = parts[-2]
            if code in valid_codes:
                if code not in status_codes:
                    status_codes[code] = 0
                status_codes[code] += 1

        # Print every 10 lines
        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise

# Final print after stdin ends
print_stats(total_size, status_codes)

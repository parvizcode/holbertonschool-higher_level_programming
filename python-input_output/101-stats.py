#!/usr/bin/python3
"""
This module reads from standard input line by line
and computes metrics about the file size and
number of occurrences for specific status codes.
"""

import sys


def print_stats(total_size, status_codes):
    """
    Prints the accumulated metrics:
    - File size
    - Status code counts in ascending order
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


def main():
    """
    Main processing loop:
    Reads stdin lines, updates counters,
    prints stats every 10 lines and on keyboard interrupt.
    """
    total_size = 0
    status_counts = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.strip().split()

            if len(parts) >= 2:
                # Handle file size
                try:
                    total_size += int(parts[-1])
                except (ValueError, IndexError):
                    pass

                # Handle status code
                code = parts[-2]
                if code in valid_codes:
                    if code not in status_counts:
                        status_counts[code] = 0
                    status_counts[code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()

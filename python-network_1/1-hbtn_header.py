#!/usr/bin/env python3
"""Fetches the X-Request-Id header from a URL response"""

import sys
from urllib.request import urlopen, Request

if __name__ == "__main__":
    url = sys.argv[1]

    req = Request(url)
    with urlopen(req) as response:
        headers = response.info()
        print(headers.get("X-Request-Id"))

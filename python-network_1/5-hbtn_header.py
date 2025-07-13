#!/usr/bin/python3
"""Fetches and displays the value of X-Request-Id in the response header of a given URL"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))

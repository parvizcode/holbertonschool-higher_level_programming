#!/usr/bin/python3
"""Sends a POST request with email as parameter and displays response body"""
import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = parse.urlencode({'email': email}).encode('utf-8')

    # Create the request object
    req = request.Request(url, data=data)

    # Perform the request and print response
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))

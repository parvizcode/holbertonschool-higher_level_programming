#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the URL
with the email as a parameter, then displays the response body.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)

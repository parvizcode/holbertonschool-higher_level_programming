#!/usr/bin/env python3
""" Fetches https://intranet.hbtn.io/status using urllib """

from urllib.request import urlopen

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

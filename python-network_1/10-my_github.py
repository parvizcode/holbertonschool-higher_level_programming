#!/usr/bin/python3
"""Displays the GitHub user id using Basic Authentication"""

import sys
import requests


def main():
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        data = response.json()
        print(data.get("id"))
    else:
        print("None")


if __name__ == "__main__":
    main()

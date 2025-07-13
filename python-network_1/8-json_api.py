#!/usr/bin/python3
"""Sends POST request to search_user API and processes the JSON response"""


import sys
import requests


def main():
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    try:
        response = requests.post(
            "http://0.0.0.0:5000/search_user", data={"q": q}
        )
        response.raise_for_status()  # HTTP errors

        try:
            data = response.json()
            if data:
                print("[{}] {}".format(data.get("id"), data.get("name")))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")

    except requests.RequestException:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()

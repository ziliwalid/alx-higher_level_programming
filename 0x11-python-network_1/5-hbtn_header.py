#!/usr/bin/python3
"""displays stuff
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))

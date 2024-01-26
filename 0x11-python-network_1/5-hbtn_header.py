#!/usr/bin/python3
"""
A Python script that takes in a URL,
sends a request to the URL and displays
the value of the variable X-Request-Id
in the response headeri
"""
import sys
import requests


if __name__ == "__main__":
    myurl = sys.argv[1]
    result = requests.get(myurl)
    print(result.headers.get("X-Request-Id"))

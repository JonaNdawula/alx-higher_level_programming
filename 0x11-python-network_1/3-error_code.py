#!/usr/bin/python3
"""
A Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""
import sys
import urllib.request


if __name__ == "__main__":
    try:
        myurl = sys.argv[1]
        with urllib.request.urlopen(myurl) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))

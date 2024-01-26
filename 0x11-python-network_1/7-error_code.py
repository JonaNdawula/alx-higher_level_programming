#!/usr/bin/python3
"""
 Python script that takes in a URL,
 sends a request to the URL and displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    myurl = sys.argv[1]
    result = requests.get(myurl)

    if (result.status_code >= 400):
        print("Error code: {}".format(result.status_code))
    else:
        print(result.text)


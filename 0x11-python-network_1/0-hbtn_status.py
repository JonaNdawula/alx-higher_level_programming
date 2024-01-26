#!/usr/bin/python3
"""
A Python script that
fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    myurl = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(myurl) as url_response:
        response = url_response.read()

        print("Body response:")
        print(f"\t- type: {type(response)}")
        print(f"\t- content: {response}")
        print(f"\t- utf8 content: {response.decode('utf8')}")

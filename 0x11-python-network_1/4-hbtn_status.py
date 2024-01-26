#!/usr/bin/python3
"""
A Python script that fetches
https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    given_url = "https://alx-intranet.hbtn.io/status"
    resp = requests.get(given_url)
    result = resp.text
    print("Body response:")
    print(f"\t- type:{type(result)}")
    print(f"\t- content: {result}")

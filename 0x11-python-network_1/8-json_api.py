#!/usr/bin/python3
"""
A Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":
    myurl = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = ""
    params = {"q": query}
    result = requests.post(myurl, data=params)

    try:
        json_res = result.json()
        if not json_res:
            print("No result")
        else:
            myId = json_res.get("id")
            myName = json_res.get("name")
            print(f"[{myId}] {myName}")
    except ValueError:
        print("Not a valid JSON")

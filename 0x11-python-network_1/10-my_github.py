#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials
(username and password) and uses the GitHub
API to display your id
"""
import sys
from requests.auth import HTTPBasicAuth
import requests

if __name__ == "__main__":
    myurl = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    res = requests.get(myurl, auth=HTTPBasicAuth(username, password))
    json_res = res.json()
    myjson = json_res.get("id")
    print(f"{myjson}")

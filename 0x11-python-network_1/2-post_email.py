#!/usr/bin/python3
"""
 ython script that takes in a URL and an email,
 sends a POST request
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    myurl = sys.argv[1]
    email = sys.argv[2]
    params = {"email": email}

    given_string = urllib.parse.urlencode(params)
    data = given_string.encode("utf-8")
    rqst = urllib.request.Request(myurl, data)

    with urllib.request.urlopen(rqst) as resp:
        resp_txt = resp.read().decode("utf-8")
        print(resp_text)

#!/usr/bin/python3
"""
A Python script that takes in a URL and an email address,
sends a POST request to the
passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    myurl = sys.argv[1]
    myemail = sys.argv[2]
    params = {"email": myemail}
    result = requests.post(myurl, data=params)
    print(result.text)

#!/usr/bin/python3

"""
takes a URL, sends a request to the URL
and displays the body of the response.
"""

import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(argv[1])
    if req.status_code < 400:
        print(req.text)
    else:
        print(f'Error code: {req.status_code}')

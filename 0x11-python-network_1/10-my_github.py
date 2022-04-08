#!/usr/bin/python3

"""
takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""

import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    auth = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get('https://api.github.com/user', auth=auth)
    print(req.json().get('id'))

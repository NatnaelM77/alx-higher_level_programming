#!/usr/bin/python3

"""
takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""

import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(f'https://api.github.com/repos/{argv[1]}/{argv[2]}'
                       f'/commits')
    data = req.json()
    for i in range(10):
        print(f'{data[i].get("name")}', end=':  ')
        print(f'{data[i].get("commit").get("author").get("name")}')

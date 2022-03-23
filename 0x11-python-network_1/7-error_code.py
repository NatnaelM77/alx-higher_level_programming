#!/usr/bin/python3

'''
takes a URL, sends a request to the URL
and displays the body of the response.
'''

import requests
from sys import argv

if __name__ == '__main__':
    try:
        req = requests.get(argv[1])
        print(req.content)
    except error.HTTPError as err:
        print(f'Error Code: {err.code}')

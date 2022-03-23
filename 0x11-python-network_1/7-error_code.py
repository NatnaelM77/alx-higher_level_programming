#!/usr/bin/python3

'''
takes a URL, sends a request to the URL
and displays the body of the response.
'''

import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(argv[1])
    try:
        if req.status_code < 400:
            print(req.text)
    except req.status_code as err_code:
        print(f'Error Code: {err_code}')

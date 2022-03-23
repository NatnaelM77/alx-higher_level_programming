#!/usr/bin/python3

'''
fetches https://alx-intranet.hbtn.io/status
'''

import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(argv[1])
    print('Body response:')
    print(f'\t- type: {type(req.content)}')
    print(f'\t- content: {req.content}')

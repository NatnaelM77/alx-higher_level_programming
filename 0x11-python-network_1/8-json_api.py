#!/usr/bin/python3

'''
takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
'''

import requests
from sys import argv

if __name__ == '__main__':
    query = {'q': '' if len(argv) == 1 else argv[1]}
    req = requests.post('http://0.0.0.0:5000/search_user', data=query)
    try:
        dct = req.json()
        id = dct.get('id')
        name = dct.get('name')
        if len(dct) == 0 or not id or not name:
            print("No result")
        else:
            print(f'[{dct.get("id")}] {dct.get("name")}')
    except:
        print('Not a valid JSON')

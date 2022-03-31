#!/usr/bin/python3

'''
 takes 2 arguments in order to solve this challenge.
'''

import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(f'https://api.github.com/repos/{argv[1]}/{argv[2]}'
                       f'/commits')
    data = req.json()
    for i in range(10):
        print(f'{data[i].get("sha")}', end=': ')
        print(f'{data[i].get("commit").get("author").get("name")}')

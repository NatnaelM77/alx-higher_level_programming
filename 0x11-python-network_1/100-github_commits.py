#!/usr/bin/python3

'''
 takes 2 arguments in order to solve this challenge.
'''

import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(f'https://api.github.com/repos/{argv[2]}/{argv[1]}'
                       f'/commits')
    commits = req.json()
    for i in range(10):
        print(f"{commits[i]['sha']}: {commits[i]['commit']['author']['name']}")

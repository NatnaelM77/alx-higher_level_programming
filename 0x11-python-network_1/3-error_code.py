#!/usr/bin/python3

'''
takes a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
'''

from sys import argv
import urllib.error
import urllib.request

if __name__ == '__main__':
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print(f'Error code: {err.code}')

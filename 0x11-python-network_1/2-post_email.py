#!/usr/bin/python3

"""
takes URL and an email, sends a POST request to the passed
and displays the body of the response decoded in utf-8.
"""

from sys import argv
import urllib.parse
import urllib.request

if __name__ == '__main__':
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(f'{response.read().decode("utf-8")}')

#!/usr/bin/python3

'''
 takes a URL and an email, sends a POST request to the passed URL with
 the email as a parameter, and displays the body of the response
 decoded in utf-8.
'''

from sys import argv
import urllib.parse
import urllib.request

if __name__ == '__main__':
    data = urllib.parse.urlencode(argv[2])
    data = data.encode('ascii')
    url = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(argv[1]) as response:
        print(f'{response.read().decode("utf-8")}')

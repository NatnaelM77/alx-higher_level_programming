#!/usr/bin/python3
import sys

if __name__ == '__main__':
    index = 1
    total = 0
    arg = sys.argv
    length = len(sys.argv)

    if length > 1:
        while (index < length):
            total += int(arg[index])
            index += 1
        print(total)
    else:
        print(0)

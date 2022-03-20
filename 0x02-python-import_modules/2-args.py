#!/usr/bin/python3
import sys

if __name__ == '__main__':
    index = 1
    arg = sys.argv
    length = len(sys.argv)

    length -= 1

    if length > 0:
        if (length == 1):
            print(f"{length:d} argument:")
        else:
            print(f"{length:d} arguments:")
        while (index <= length):
            print(f"{index:d}: {sys.argv[index]:s}")
            index += 1
    else:
        print(f"{length:d} arguments.")

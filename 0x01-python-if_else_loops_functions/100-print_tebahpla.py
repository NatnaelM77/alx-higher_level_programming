#!/usr/bin/python3
i = 122
while (i >= 97):
    if i % 2 != 0:
        print("{:c}".format(i - 32), end="")
    else:
        print("{:c}".format(i), end="")
    i -= 1

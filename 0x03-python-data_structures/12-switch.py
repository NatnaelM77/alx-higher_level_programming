#!/usr/bin/python3
a = 89
b = 10
a, b = b, a + (b - b)
print("a={:d} - b={:d}".format(a, b))

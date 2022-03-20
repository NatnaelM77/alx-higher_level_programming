#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    arg = sys.argv
    length = len(arg)
    operators = ['+', '-', '*', '/']

    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(arg[1])
        op = arg[2]
        b = int(arg[3])

        if op in operators:
            if (op == '+'):
                print(f"{a:d} {op:s} {b:d} = {add(a, b):d}")
            elif (op == '-'):
                print(f"{a:d} {op:s} {b:d} = {sub(a, b):d}")
            elif (op == '*'):
                print(f"{a:d} {op:s} {b:d} = {mul(a, b):d}")
            else:
                print(f"{a:d} {op:s} {b:d} = {div(a, b):d}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

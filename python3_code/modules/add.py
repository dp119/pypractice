#!/usr/bin/env python3

def get_input():
    import sys

    x = sys.argv[1]
    y = sys.argv[2]

    x , y = int(x), int(y)
    return x, y

def do_add(a, b):
    print("Addition", a + b)

def do_mul(a , b):
    print("Multiply", a * b)

# Main starts from here
if __name__ == "__main__":
    p,q = get_input()
    print("Inside if")
    do_add(p, q)
    do_mul(p, q)


#!/usr/bin/python3
"""
    Program to add two numbers
"""

def add(a, b):
    print("Sum of {} and {} is {}".format(a, b, a+b))
    # Below line works only in 3.6+
    print(f"Sum of {a} and {b} is {a+b}")

def main():
    x = 10
    y = 20
    add(x, y)

# Main starts from here
main()

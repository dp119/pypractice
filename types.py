#!/usr/bin/python
""" A simple program to print the type of variables
"""

def approximate(num):
    """ This function takes a float number
        It returns the integer equivalent of this number
    """
    intnum = int(num)
    return intnum

def print_and_type(val):
    """ This function takes a variable as input
        It prints the variable and its type
    """
    print val, type(val)

# Main starts from below
name = "Sunil"
age = 20
weight = 65.9
approx_weight = approximate(weight)
value = 99 ** 8
agree = True

print_and_type(name)
print_and_type(age)
print_and_type(weight)
print_and_type(approx_weight)
print_and_type(value)
print_and_type(agree)

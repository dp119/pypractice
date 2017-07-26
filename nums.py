#!/usr/bin/python
""" A program to get a number from the user
    It prints the number and its 3 consecutive numbers
"""

def get_number():
    """ A function to fetch a number from the user
        It return an integer value
    """
    num = raw_input("Please enter a number : ")
    num = int(num)
    return num

def print_cons_nums(number):
    """ This function takes an integer number as input
        It prints the number and its 3 consecutive numbers
    """
    print "The number you entered is : ", number
    print "The 3 consecutive numbers following", number, "are :",
    print number + 1, number + 2, number + 3

# Main starts from here
xxx = get_number()
print_cons_nums(xxx)

#!/usr/bin/python
""" A program to print the temperatures in celsius and farhenite
    for a given set of numbers

    If input is 100, expected out is :
    82.0
    87.5555555556
    93.1111111111
    98.6666666667
    104.222222222
    109.777777778
"""

def get_celsius():
    val = raw_input("Enter the temperature in celsius : ")
    # TODO : Fix the code so that this functions returns
    # the temperature in celsius

def get_surround_cels(temp):
    return temp-10, temp, temp+10

def get_farh(cel):
    # TODO : The formula for converting temperature in celsius
    # to farenhite is
    # F = 32 + (C * 5/9 )
    # Implement this function so that 
    #   it takes the input temperature in celsius and 
    #   returns the equivalent temperature in farhenhite

# Main starts from here
cel = get_celsius()
cel1, cel2, cel3 = get_surround_cels(cel)

print get_farh(cel1)
# TODO : Fix the below 2 lines of code
print get_farh()
print get_farh()

cel += 30
all_cels = get_surround_cels(cel)

# TODO : Fix the below 3 lines of code so that we use
# temperatures present in all_cels variable
print get_farh()
print get_farh()
print get_farh()

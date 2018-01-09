#!/usr/bin/python3
"""
    This program calculates the area of a circle
"""

def get_float(msg):
    inp = input(msg)
    return float(inp)

def calculate_area(rrr):
    area = (22/7) * (rrr ** 2)
    print("Area of circle with radius {} is {}".format(rrr, area))
    # Below line works only in Python version 3.6 and above
    print(f"Area of circle with radius {rrr} is {area}")

def main():
    radius = get_float("What is the radius of the circle ? ")
    calculate_area(radius)

# Main starts from here
main()

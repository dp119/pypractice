#!/usr/bin/python3
"""
    This program prints all the squares starting from the given number
    But it prints only two digit square numbers
"""

def get_num():
    inp = input("Enter a two digit number : ")
    return int(inp)

def roll_on(val):
    if val < 10 or val > 99:
        print("Wrong input")
        return

    sqr = val ** 2

    while sqr < 900:
        if val < 0:
            print("No negatives please")
            val = get_num()
            sqr = val ** 2
            continue

        print(sqr, end=" ")
        val += 1
        sqr = val ** 2

    else:
        print()
        print("All squares less than 900 printed")

    print("We are done")


def main():
    start = get_num()
    roll_on(start)

# Main starts from here
main()

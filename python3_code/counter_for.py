#!/usr/bin/python3
"""
    A program to print the numbers from start to end
"""

def get_num(msg="Enter a number : "):
    inp = input(msg)
    try :
        inp = int(inp)
    except ValueError:
        inp = get_num(msg)

    return inp

def print_newline(val):
    if val % 10 == 0:
        print()

    return val + 1

def count(begin, finish):
    if begin < finish:
        first, last, step = begin, finish + 1, 1
    else:
        first, last, step = begin, finish - 1, -1

    nums = 1
    for itr in range(first, last, step):
        print(itr, end=' ')
        nums = print_newline(nums)
    else:
        print()

def main():
    start = get_num("Where do you want to start from ? ")
    end = get_num("Where do you want me to stop at ? ")
    count(start, end)

# Main starts from here
main()

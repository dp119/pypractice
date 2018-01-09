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

def count(begin, finish):
    if begin > finish:
        nums = 0
        itr = finish
        while itr >= begin:
            print(itr, end=' ')
            itr -= 1
            nums += 1
            if nums % 10 == 0:
                print()
        else:
            print()
    else:
        nums = 0
        itr = begin
        while itr <= finish:
            print(itr, end=' ')
            itr += 1
            nums += 1
            if nums % 10 == 0:
                print()
        else:
            print()

def main():
    start = get_num("Where do you want to start from ? ")
    end = get_num("Where do you want me to stop at ? ")
    count(start, end)

# Main starts from here
main()

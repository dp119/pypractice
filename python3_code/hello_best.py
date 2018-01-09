#!/usr/bin/python
""" This is my first Python program
    This prompts the user to enter his name and then
    welcomes the user by printing "Hello" followed by his name
"""

def wish_user(user):
    print("Hello", user, "!!!")

def get_name():
    name = input("Enter your name : ")
    return name

def main():
    user_name = get_name()
    wish_user(user_name)

# Main starts from here
main()

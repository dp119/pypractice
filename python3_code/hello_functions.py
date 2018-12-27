# A simple program to understand about functions

# The order of defining the functions does not matter
def say_bye():
    print("Good bye")
    
def say_hello():
    print("Hello", "World")


def say_something(msg):
    """ 
        A function that takes a single value as input
    """
    print(msg)

def add_runs(inp1, inp2):
    """ 
        A function that takes two numbers as input
        and returns their sum
    """
    res = inp1 + inp2
    return res

# Main
a = 10
print(a)

# The program output is dependent on the order in which we invoke the functions
say_hello()
say_bye()

# functions can take a value as input
say_something("Good night")
say_something(29)

sachin = 99
dhoni = 120
# Always have a variable to store the value returned by a function
total = add_runs(sachin, dhoni)
print("Total runs", total)

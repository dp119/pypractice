#!/usr/bin/env python3

print("Printing Hello World 5 time")
for counter in range(0, 5):
    print("Hello World")
else:
    print() # To add a separator line in the output

# The above code can also be written for any range of 5 numbers
# The counter variable in this "for" loop is basically never used
# And rendered useless
print("Hello world using a range of 5 numbers")
for counter in range(12, 17):
    print("Hello World")
else:
    print() # To add a separator line in the output

# Below is a generic way of writing the same loop as above
# It iterates over a range of any 5 numbers
print("Hello world using a generic range of 5 numbers")
start = 23
end = start + 5

for counter in range(start, end):
    print("Hello World")
else:
    print() # To add a separator line in the output

# If one insists on writing a "for" loop for this,
# Then the Pythonic way of writing it is to use
# an _ variable to indicate that this variable
# is not used in the "for" loop
print("Hello world using _")
for _ in range(start, end):
    print("Hello World")
else:
    print() # To add a separator line in the output

# A more cleaner and preferred way for such loops is to use a "while" loop.
# The use of "counter" variable makes it easy to understand what is 
# intended in this code
print("Hello World using a while loop")
counter = 0
while counter < 5:
    print("Hello World")
    counter += 1
else:
    print() # To add a separator line in the output

# The preferred scenario for using a "for" loop is when iterating over a list
print("Wishing Hello to my friends")
friends = [ 'Ajay', 'Chethan', 'Girish', 'Amardeep']
for name in friends:
    print("Hello", name)
else:
    print() # To add a separator line in the output

# Iterating over a list using "while" loop is also possible
# But it is not the most Pythonic way of doing it
# Using a "for" loop in this case is more Pythonic
print("Wishing Hello to my friends using a while loop")
idx = 0
while idx < len(friends):
    print("Hello", friends[idx])
    idx += 1
else:
    print() # To add a separator line in the output

#!/usr/bin/python

"""
    This program insert's some text in any given line of a file.
    Input : 
            Filename is taken as argument to the program
            The user is prompted for the line where the text 
             is to be inserted
    Output :
            The same file is updated with some new text
"""

import sys

def get_linenumber(num):
    """
        Prompt the user for the line number where he wants to insert the text
        Input :
                The max number of lines in the existing file
        Output :
                A number that is less than the max number of lines in file

    """
    ans = num + 10 # Initialise ans to a number larger than number of lines
    while ans >= num:
        prompt = "Please enter the line number where you want to insert the text[max: " + str(num) + " ]"
        ans = raw_input (prompt)
        ans = int(ans)

    return ans

def print_file(FH):
    """
        Print the contents of the file on the output screen
        Input : 
                file handle
        Return : 
                The number of lines in the file
    """
    all_text = FH.read()
    all_lines = all_text.split('\n')
    for line in all_lines:
        print line

    return len(all_lines)

# Main : This is where the program starts
# First check if the mandatory argument is given to the program
if len(sys.argv) < 2:
    print "No filename provided as argument to program"
    print "Usage :", sys.argv[0], "<filename>"
    quit()

fname = sys.argv[1]
text = "This line is added by my program"

FH = open(fname)

print "Printing the contents of file", fname
num_of_lines = print_file(FH)
line_number = get_linenumber(num_of_lines)
print "The user wants the text to be inserted in line number :", line_number


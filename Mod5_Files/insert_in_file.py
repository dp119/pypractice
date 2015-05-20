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

def print_file(FH):
    """
        Print the contents of the file on the output screen
        Input : 
                file handle
        Return : 
                None
    """
    all_text = FH.read()
    all_lines = all_text.split('\n')
    for line in all_lines:
        print line

# Main : This is where the program starts
# First check if the mandatory argument is given to the program
if len(sys.argv) < 2:
    print "No filename provided as argument to program"
    print "Usage :", sys.argv[0], "<filename>"
    quit()

fname = sys.argv[1]

FH = open(fname)

print "Printing the contents of file", fname
print_file(FH)


""" Takes a filename as argument 
    Creates a new file with the name
    "shuffle" appended to the original filename.
    The lines in the input are shuffled 
    and written into the new file
"""

from fileops import *

def shuffler(lines):
    """ Shuffle a list of strings Input : list of strings
    Return : a new list with original strings shuffled
    """

# Main starts here
# Get filename from command line 
FH, lines = get_lines(file) 
FH.close()

shuffled_lines = shuffler(lines)

new_name = file + "shuffle" 
write_lines(new_name, shuffled_lines)

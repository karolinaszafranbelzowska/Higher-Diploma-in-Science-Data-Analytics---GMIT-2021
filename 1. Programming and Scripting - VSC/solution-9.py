# solution to problem number 9
# Karolina Szafran Belzowska, 2019/03/27
# Command Line arguments

# Taken from: https://www.youtube.com/watch?v=qjdeQ83T9sQ and this stack overflow question https://stackoverflow.com/a/42040147

import sys

filename = "my_text.txt"
f = open(filename, "r+")

# with open(sys.argv[1]) as f: # with keyword automatically closes file when the program ends.

   
lines = f.readlines() # Using .readlines() method to access individual lines 
                      # It creates a list with each line as a separate item on the list

for l in lines:
    if l == '\n':
        lines.remove(l) # removes the blanks

for i in range(0, len(lines), 2): # for loop - range starts at 0, ends with the number of lines in the text and does it in increments of 2.
                                  # i represets the index of each line in lines and every second one should print to console
    print (lines[i])



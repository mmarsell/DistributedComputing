#!/usr/bin/python2.7
# reducer.py
import sys
valid_ID = None
num_votes = 0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip().strip("|")    # Remove trailing characters
    titleID, value = line.split("|", 1)
    if value[0] != 'n':
        valid_ID = titleID
        num_votes = int(value)

    elif titleID == valid_ID:
        print(str(num_votes) + "|" + titleID + "|" + str(value))
#!/usr/bin/python2.7
# combiner.py
import sys
valid_ID = None

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    titleID, value = line.split("|", 1)
    if value != '\\N':
        if value == "":
            valid_ID = titleID

        elif titleID == valid_ID:
            print(value)

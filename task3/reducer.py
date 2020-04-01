#!/usr/bin/python2.7
# reducer.py
import sys
valid_ID = None
past_val = 0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    titleID, value1, value2, value3 = line.split("|", 3)
    if value2 == "":
        valid_ID = titleID
        past_val = float(value1)

    elif titleID == valid_ID:
        print(str(value1) + "|" + str(value3) + "|" + str(past_val) + "|" + value2)
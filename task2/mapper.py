#!/usr/bin/python2.7
# mapper.py
import sys


def map_function(title):

    fields = title.strip().split('\t')
    titleID = fields[0]

    # filter fields sent to reducer
    if len(fields) == 9 and fields[1] != '\\N' and fields[5] != '\\N' and fields[2] != '\\N':
        if fields[1] == "movie" and 1990 <= int(fields[5]) <= 2018:
            yield titleID, fields[2]

    if len(fields) == 3 and float(fields[1]) >= 7.5 and int(fields[2]) >= 500000:
        yield titleID, ""               # ensures easily accessible sorting

for line in sys.stdin:
    # Call map_function for each line in the input
    for key, value in map_function(line):
        # Emit key-value pairs using '|' as a delimiter
        print(key + "|" + str(value))
#!/usr/bin/python2.7
# mapper.py
import sys


def map_function(title):

    fields = title.strip().split('\t')
    titleID = fields[0]

    # Filter fields to restrict data sent to reducer
    if len(fields) == 9 and fields[1] != '\\N' and fields[2] != '\\N' and fields[5] != '\\N':
        if fields[1] == "movie" and 1900 <= int(fields[5]) <= 1999:
            genres = fields[8]
            if genres != '\\N':
                for types in genres.strip().split(','):
                    yield titleID, types, fields[2], fields[5]

    if len(fields) == 3:
        yield titleID, fields[1], "", ""

for line in sys.stdin:
    # Call map_function for each line in the input
    for key, value1, value2, value3 in map_function(line):
        # Emit key-value pairs using '|' as a delimiter
        print(key + "|" + str(value1) + "|" + str(value2) + "|" + str(value3))
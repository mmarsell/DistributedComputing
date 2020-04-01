#!/usr/bin/python2.7
# mapper.py
import sys

def map_function(title):
    fields = title.strip().split('\t')
    titleID = fields[0]

    if len(fields) == 3 and fields[2] != '\\N':
        if(fields[2][0] == 'n'):                    # check which file is being read
            allWriters = fields[2]
            for writer in allWriters.strip().split(','):
                yield titleID, writer
        else:
            yield titleID, fields[2]


for line in sys.stdin:
    # Call map_function for each line in the input
    for key, value1 in map_function(line):
        # Emit key-value pairs using '|' as a delimiter
        print(key + "|" + str(value1))


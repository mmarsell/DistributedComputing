#!/usr/bin/python2.7
# mapper.py
import sys


def map_function(title):
    if "|" in title.strip().strip("|"):
        votes, titleID, writer = title.strip().split("|", 2)
        yield writer, titleID, votes                        # if reading output from reducer1
    else:
        fields = title.strip().split('\t')
        if fields[1] != '\\N' and fields[5] != '\\N':
            for title in fields[5].strip().split(','):
                yield fields[0], title, fields[1]           # if reading from name.basics.tsv

for line in sys.stdin:
    # Call map_function for each line in the input
    for key, value1, value2 in map_function(line):
        # Emit key-value pairs using '|' as a delimiter
        print(key + "|" + str(value1) + "|" + str(value2))
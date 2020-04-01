#!/usr/bin/python2.7
# mapper.py
import sys

def map_function(title):
    fields = title.strip().split('\t')
    genres = fields[8]                              # grab necessary fields
    runtimeMinutes = fields[7]
    if genres != '\\N' and runtimeMinutes != '\\N':
        for types in genres.strip().split(','):     # split by genre
            yield types, runtimeMinutes

for line in sys.stdin:
    for key, value in map_function(line):
        print(key + "|" + str(value))               # send genre|runtime
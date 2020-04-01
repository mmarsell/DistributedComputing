#!/usr/bin/python2.7
# mapper2.py
import sys

def map_function(title):
    genre, year, rating, title = title.strip().split('|', 3)
    yield genre, year, rating, title

for line in sys.stdin:
    # Call map_function for each line in the input
    for key, year, rating, title in map_function(line):
        # Emit key-value pairs using '|' as a delimiter
        print(key + "|" + str(year) + "|" + str(rating) + "|" + title)
#!/usr/bin/python2.7
# reducer2.py
import sys
from collections import defaultdict

lastID = None
lastTitle = None
votes = 0
writer = None
counter = 0
isNum = False
current_writers = defaultdict(int)      # bounded to size 10

global_min = float("inf")

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip().strip("|")         # Remove trailing characters
    nameID, titleID, value1 = line.split("|", 2)
    try:
        value1 = int(value1)
        isNum = True
    except:
        isNum = False

    if isNum:
        lastID = nameID
        lastTitle = titleID
        votes = value1

    # load dictionary of writers until 10 have been loaded
    elif lastID == nameID and lastTitle == titleID and counter < 10:
        writer = value1
        writer_seen = current_writers.get(writer)

        # if we have not encountered writer before
        if writer_seen == None:
            current_writers[writer] = votes;
            counter = counter + 1

        # if the writer already has been seen
        elif writer_seen != None:
            if current_writers[writer] < votes:
                current_writers[writer] = votes
        if votes < global_min:
            global_min = votes

    # Once there are 10 writers, replace the lowest one in the dictionary if the current votes are higher
    elif lastID == nameID and lastTitle == titleID and counter == 10 and votes > global_min:
        writer = value1

        # If the replacement is not currently a writer
        if current_writers.get(writer) == None:
            temp_min = min(current_writers, key=current_writers.get)
            current_writers.pop(temp_min, None)
            current_writers[writer] = votes
            global_min = current_writers[min(current_writers.keys(), key=(lambda person: current_writers[person]))]

        # If replacement already exists, just update their botes
        elif current_writers[writer] < votes:
            current_writers[writer] = votes
            global_min = current_writers[min(current_writers.keys(), key=(lambda person: current_writers[person]))]

# Convert dictionary to sorted list and print
result = []
for writers in current_writers:
    result.append((current_writers[writers], writers))
result.sort()
result.reverse()
for value in result:
    print(str(value[0]) + "|" + value[1])

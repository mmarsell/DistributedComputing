#!/usr/bin/python2.7
# combiner.py
import sys

prev_genre = None
total_runtime = 0.0
global_min = float("inf")
global_max = 0
counter = 1

for line in sys.stdin:
    line = line.strip().strip("|")
    genre, runtime = line.split("|", 1)
    if genre != '\\N' and runtime != '\\N':
        runtime = int(runtime)

        if prev_genre == genre:
            counter = counter + 1
            total_runtime += float(runtime)     # keep adding runtime until genre changes
        else:
            if prev_genre != None:
                print(prev_genre + "|" + str(total_runtime) + "|" + str(global_max) + "|" + str(global_min) + "|" + str(counter))
                global_min = float("inf")
                global_max = 0
                counter = 1

            total_runtime = runtime
            prev_genre = genre

        if runtime <= global_min:
            global_min = runtime
        if runtime >= global_max:
            global_max = runtime

# To print last line
if prev_genre == genre:
    print(prev_genre + "|" + str(total_runtime) + "|" + str(global_max) + "|" + str(global_min) + "|" + str(counter))

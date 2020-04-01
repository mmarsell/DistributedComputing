#!/usr/bin/python2.7
# memory-efficient_reducer.py
import sys

prev_genre = None
prev_count = 0
total_runtime = 0.0
global_min = float("inf")
global_max = 0
counter = 1
max_count = 0
ran_combiner = True

for line in sys.stdin:
    line = line.strip().strip("|")
    try:
        genre, average, max_time, min_time, count = line.split("|", 4)
    except:
        ran_combiner = False

    # if the combiner was executed split into 5 fields
    if ran_combiner:
        average = float(average)
        max_time = int(max_time)
        min_time = int(min_time)
        count = int(count)


        if prev_genre == genre:
            max_count += count
            total_runtime += average
        else:
            if prev_genre != None:
                total_runtime = float(total_runtime / max_count)
                print(str(round(total_runtime, 2)) + "|" + str(global_max) + "|" + str(global_min) + "|" + prev_genre)
                global_min = float("inf")
                global_max = 0
                max_count = 0
            total_runtime = average
            prev_genre = genre
            max_count = count

        if min_time <= global_min:
            global_min = min_time
        if max_time >= global_max:
            global_max = max_time
        counter = max_count

    # if the combiner didn't run handle mapper output format
    if not ran_combiner:
        genre, runtime = line.split("|", 1)
        if genre != '\\N' and runtime != '\\N':
            runtime = int(runtime)

            if prev_genre == genre:
                counter = counter + 1
                total_runtime += float(runtime)
            else:
                total_runtime = float(total_runtime / counter)
                if prev_genre != None:
                    print(str(round(total_runtime, 2)) + "|" + str(global_max) + "|" + str(global_min) + "|" + prev_genre)
                    global_min = float("inf")
                    global_max = 0
                    counter = 1

                total_runtime = runtime
                prev_genre = genre

            if runtime <= global_min:
                global_min = runtime
            if runtime >= global_max:
                global_max = runtime

if prev_genre == genre:
    total_runtime = float(total_runtime / counter)
    print(str(round(total_runtime, 2)) + "|" + str(global_max) + "|" + str(global_min) + "|" + prev_genre)
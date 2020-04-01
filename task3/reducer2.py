#!/usr/bin/python2.7
# reducer2.py
import sys

prev_genre = None
best_title = None
prev_decade = 0
global_max = 0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    genre, year, rating, title = line.split("|", 3)
    year = int(year)/10 % 10        # calculate decade number
    rating = float(rating)

    if genre == prev_genre:
        if prev_decade != year:
            print(str(prev_decade) + "|" + genre + "|" + best_title)
            prev_decade = year
            global_max = rating
            best_title = title

    else:
        if prev_genre != None:
            print(str(prev_decade) + "|" + prev_genre + "|" + best_title)

        best_title = title
        global_max = rating
        prev_decade = year
        prev_genre = genre

    # Update global max rating for genre
    if rating >= global_max:
        if rating == global_max:
            best_title = title if title < best_title else best_title
        else:
            best_title = title
        global_max = rating

if prev_genre == genre and prev_decade == year:  # Don't forget the last key/value pair
    print(str(prev_decade) + "|" + prev_genre + "|" + best_title)
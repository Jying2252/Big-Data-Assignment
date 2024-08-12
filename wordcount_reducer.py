#!/usr/bin/env python3
import sys

# Initialize variables to track the current word and its cumulative count
current_word = None
current_count = 0
word = None

# Read input from standard input line by line
for line in sys.stdin:
     # Split the line into word and count based on the tab delimiter
    line = line.strip()
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue
     # If the word matches the current word being tracked, accumulate the count
    if current_word == word:
        current_count += count
    else:
        # If the word has changed, output the count for the previous word
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# output the count for the last word
if current_word == word:
    print(f"{current_word}\t{current_count}")


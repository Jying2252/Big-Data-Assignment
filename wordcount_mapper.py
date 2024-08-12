#!/usr/bin/env python3
import sys

# Iterate over each line of input from standard input
for line in sys.stdin:
    # Split the line into fields using tab as the delimiter
    fields = line.strip().split('\t')
    # Check if the line has at least 3 fields
    if len(fields) >= 3:  
        review_text = fields[2]
        words = review_text.split()
        for word in words:
            # Print each word followed by a tab and the number 1
            print(f"{word}\t1")

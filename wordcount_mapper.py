#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split('\t')
    if len(fields) >= 3:  
        review_text = fields[2]
        words = review_text.split()
        for word in words:
            print(f"{word}\t1")

# wordcount_mapper.py
#!/usr/bin/env python3
import sys

for line in sys.stdin:
    fields = line.strip().split('\t')
    if len(fields) >= 3:  # Assuming the text is the third field
        review_text = fields[2]
        words = review_text.split()
        for word in words:
            print(f"{word}\t1")


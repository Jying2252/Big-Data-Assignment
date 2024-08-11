#!/usr/bin/env python3

import sys

current_title = None
current_total_score = 0
current_count = 0
sentiment_label = None

books = []

for line in sys.stdin:
    try:
        title, score, sentiment = line.strip().split('\t')
        score = float(score)
    except ValueError:
        # If there is an error in splitting or converting the score, skip this line
        print(f"Error processing line: {line.strip()}", file=sys.stderr)
        continue

    if current_title == title:
        current_total_score += score
        current_count += 1
    else:
        if current_title:
            average_score = current_total_score / current_count
            books.append((current_title, average_score, sentiment_label))
        current_title = title
        current_total_score = score
        current_count = 1
        sentiment_label = sentiment

# Add the last book
if current_title:
    average_score = current_total_score / current_count
    books.append((current_title, average_score, sentiment_label))

# Sort books by average score and print top 10
books_sorted = sorted(books, key=lambda x: x[1], reverse=True)
for book in books_sorted[:10]:
    print(f"{book[0]}\t{book[1]}\t{book[2]}")

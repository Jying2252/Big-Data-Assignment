#!/usr/bin/env python3

import sys
import re
import string

# Load VADER lexicon from file
def load_vader_lexicon(file_path):
    vader_lexicon = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split(':')
            if len(parts) == 2:
                word, score = parts
                vader_lexicon[word.strip()] = float(score)
    return vader_lexicon

# Normalize sentiment score to 0 to 1 range
def normalize_score(score):
    # Assuming VADER scores range from -4 to 4 based on typical usage
    return (score + 4) / 8

# Calculate sentiment score using the VADER lexicon
def calculate_sentiment(text, lexicon):
    # Remove punctuation from text
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    sentiment_score = 0
    words_in_lexicon = 0
    for word in words:
        word_lower = word.lower()
        if word_lower in lexicon:
            sentiment_score += lexicon[word_lower]
            words_in_lexicon += 1
    if words_in_lexicon == 0:
        print("No words from review matched the lexicon.", file=sys.stderr)
        return 0.5  # Return neutral score if no match
    normalized_score = normalize_score(sentiment_score / words_in_lexicon)
    return normalized_score

# Load the VADER lexicon
vader_lexicon = load_vader_lexicon('vader_lexicon.txt')
print(f"Loaded VADER lexicon: {len(vader_lexicon)} words loaded", file=sys.stderr)

# Skip the header if present
header_skipped = False

# Process each line of input
for line in sys.stdin:
    line = line.strip()
    print(f"Raw line: {line}", file=sys.stderr)  # Print the raw line for debugging

    # Skip header
    if not header_skipped:
        header_skipped = True
        continue

    # Split the line on multiple spaces or tabs
    fields = re.split(r'\s{2,}|\t+', line)

    # Check if the line has at least three fields
    if len(fields) >= 3:
        title = fields[1]
        review_text = fields[2]
        sentiment_score = calculate_sentiment(review_text, vader_lexicon)

        # Adjust sentiment classification thresholds
        if sentiment_score > 0.6:
            sentiment_label = 'positive'
        elif sentiment_score < 0.4:
            sentiment_label = 'negative'
        else:
            sentiment_label = 'neutral'

        print(f"{title}\t{sentiment_score}\t{sentiment_label}")
    else:
        print(f"Error processing line (fields length: {len(fields)}): {line}", file=sys.stderr)


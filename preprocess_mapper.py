#!/usr/bin/env python3
import sys
import re

# Load stopwords from the stopwords.txt file
with open('stopwords.txt', 'r') as file:
    stopwords = set(file.read().split())

def tokenize(text):
    """Tokenize the text into words."""
    return text.split()

def remove_punctuation(text):
    """Remove punctuation from the text."""
    return re.sub(r'[^\w\s]', '', text)

def remove_stopwords(tokens):
    """Remove stopwords from the token list."""
    return [word for word in tokens if word.lower() not in stopwords]

for line in sys.stdin:
    fields = line.strip().split(',')
    if len(fields) >= 10:
        review_text = fields[9]

        # Remove punctuation
        review_text = remove_punctuation(review_text)
        
        # Tokenize the text
        tokens = tokenize(review_text)

        # Remove stopwords
        filtered_tokens = remove_stopwords(tokens)

        # Print the processed output
        print(f"{fields[0]}\t{fields[1]}\t{' '.join(filtered_tokens)}")

import nltk
from nltk.corpus import stopwords
import re
import string

# Get English stopwords
stop_words = set(stopwords.words('english'))

# Function to tokenize text into words
def tokenize(text):
    """Tokenize the text into words."""
    return text.split()

# Function to remove punctuation from text
def remove_punctuation(text):
    """Remove punctuation from the text."""
    return re.sub(r'[^\w\s]', '', text)

# Function to remove stopwords from a list of tokens
def remove_stopwords(tokens):
    """Remove stopwords from the token list."""
    return [word for word in tokens if word.lower() not in stop_words]

# Function to process a single review text
def preprocess_review_text(review_text):
    # Remove punctuation
    review_text = remove_punctuation(review_text)
    
    # Tokenize the text
    tokens = tokenize(review_text)
    
    # Remove stopwords
    filtered_tokens = remove_stopwords(tokens)
    
    return filtered_tokens


# Wordcount #

from collections import Counter

# Path to the dataset
file_path = "/Users/minyee/Downloads/Amazon Books Review/Books_rating.csv"

# Counter to store word frequencies
word_counter = Counter()

# Function to read and process each line in the datset
def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        next(file)  # Skip the header if present
        for line in file:
            fields = line.strip().split(',')
            if len(fields) >= 10:  # Adjust the index if the review text is not in the 10th column
                review_text = fields[9]
                # Preprocess the review text
                tokens = preprocess_review_text(review_text)
                # Update word counter with the tokens
                word_counter.update(tokens)
    
    return word_counter

# Get the word counts from the file
word_counter = count_words_in_file(file_path)

# Get the top 20 most common words
top_20_words = word_counter.most_common(20)

# Display the top 20 words with their counts
print("Top 20 words with highest word count:")
for word, count in top_20_words:
    print(f"{word}: {count}")

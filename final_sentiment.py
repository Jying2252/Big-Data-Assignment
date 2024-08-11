import nltk
from nltk.corpus import stopwords
import re
from collections import defaultdict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Download the stopwords 
nltk.download('stopwords')

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
    """Process the review text by removing punctuation, tokenizing, and removing stopwords."""
    # Remove punctuation
    review_text = remove_punctuation(review_text)
    
    # Tokenize the text
    tokens = tokenize(review_text)
    
    # Remove stopwords
    filtered_tokens = remove_stopwords(tokens)
    
    return filtered_tokens

# Sentiment Analysis #

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Access the vaderSentiment lexicon
vader_lexicon = sia.lexicon

# Export the lexicon to a file
with open('vader_lexicon.txt', 'w') as file:
    for word, score in vader_lexicon.items():
        file.write(f"{word}: {score}\n")

# Function to load the VADER lexicon from a text file
def load_vader_lexicon(file_path):
    vader_lexicon = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split(':')
            if len(parts) == 2:
                word, score = parts
                vader_lexicon[word.strip()] = float(score)
    return vader_lexicon

# Function to calculate sentiment score using the loaded VADER lexicon
def calculate_sentiment(text, lexicon):
    """Calculate the sentiment score using the custom VADER lexicon."""
    # Remove punctuation from text
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    sentiment_score = 0
    words_in_lexicon = 0
    for word in words:
        word_lower = word.lower()
        if word_lower in lexicon:
            sentiment_score += lexicon[word_lower]
            words_in_lexicon += 1
    if words_in_lexicon == 0:
        return 0  # Return 0 if no match, instead of None
    # Average the sentiment score and normalize it
    normalized_score = normalize_score(sentiment_score / words_in_lexicon)
    return normalized_score

# Normalize sentiment score to 0 to 1 range
def normalize_score(score):
    # Assuming VADER scores range from -4 to 4 based on typical usage
    return (score + 4) / 8

# Function to process and calculate sentiment for each review
def process_reviews_with_sentiment(file_path, lexicon):
    book_scores = defaultdict(list)

    with open(file_path, 'r') as file:
        next(file)  # Skip the header if present
        for line in file:
            fields = line.strip().split(',')
            if len(fields) >= 10:  
                title = fields[1].strip() 
                review_text = fields[9].strip()

                # Preprocess the review text using the correct preprocessing method
                tokens = preprocess_review_text(review_text)
                
                if tokens:  
                    filtered_review = ' '.join(tokens)

                    # Calculate sentiment score
                    sentiment_score = calculate_sentiment(filtered_review, lexicon)

                    # Include scores of 0
                    if sentiment_score is not None:  # Ensure valid sentiment score
                        
                        # Store the score under the respective book title
                        book_scores[title].append(sentiment_score)

    # Calculate average sentiment score for each book
    book_avg_scores = [(title, sum(scores) / len(scores)) for title, scores in book_scores.items()]

    # Sort books by average sentiment score in descending order
    books_sorted = sorted(book_avg_scores, key=lambda x: x[1], reverse=True)

    return books_sorted

# Load the VADER lexicon from the file
vader_lexicon = load_vader_lexicon('vader_lexicon.txt')

# Replace this with the path to your input file
file_path = 'E:/big data/Books_rating.csv'

# Get the books with their normalized sentiment scores
books_with_sentiment = process_reviews_with_sentiment(file_path, vader_lexicon)

# Display the top 10 books with highest sentiment scores
print("\nTop 10 books with highest sentiment scores:")
print(f"{'Title':<60} {'Sentiment Score':<20}")
print("-" * 80)
for book in books_with_sentiment[:10]:
    print(f"{book[0]:<60} {book[1]:<20.4f}")

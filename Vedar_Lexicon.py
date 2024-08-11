from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Access the vaderSentiment lexicon
vader_lexicon = sia.lexicon

# Export the lexicon to a file
with open('vader_lexicon.txt', 'w') as file:
    for word, score in vader_lexicon.items():
        file.write(f"{word}: {score}\n")

vader_lexicon_list = list(vader_lexicon.items())
vader_lexicon_words = list(vader_lexicon.keys())
vader_lexicon_dict = dict(vader_lexicon)
print(vader_lexicon_list[:10])

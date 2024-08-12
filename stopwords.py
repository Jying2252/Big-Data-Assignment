import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')

# Get English stopwords
stop_words = stopwords.words('english')

# Save stopwords to a text file
with open("stopwords.txt", "w") as f:
    for word in stop_words:
        f.write(word + "\n")

print("Stopwords saved to stopwords.txt")

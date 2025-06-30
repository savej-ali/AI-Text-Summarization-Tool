import nltk
import heapq
import re

# Download NLTK resources
nltk.download("punkt")
nltk.download("stopwords")

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

def extract_summary(input_data, summary_length=3):
    # Text normalization
    refined_text = re.sub(r'\[[0-9]*\]', '', input_data)
    refined_text = re.sub(r'\s+', ' ', refined_text)

    # Sentence breakdown
    sentence_collection = sent_tokenize(refined_text)

    # Stopword list
    ignored_words = set(stopwords.words('english'))

    # Calculate word frequency
    token_frequencies = {}
    for token in word_tokenize(refined_text.lower()):
        if token.isalnum() and token not in ignored_words:
            token_frequencies[token] = token_frequencies.get(token, 0) + 1

    # Normalize word weights
    highest = max(token_frequencies.values(), default=1)
    token_frequencies = {word: val / highest for word, val in token_frequencies.items()}

    # Assign scores to sentences
    sentence_weight = {}
    for line in sentence_collection:
        words = word_tokenize(line.lower())
        if len(line.split()) <= 30:
            for w in words:
                if w in token_frequencies:
                    sentence_weight[line] = sentence_weight.get(line, 0) + token_frequencies[w]

    # Fetch most relevant lines
    selected = heapq.nlargest(summary_length, sentence_weight, key=sentence_weight.get)
    return ' '.join(selected)

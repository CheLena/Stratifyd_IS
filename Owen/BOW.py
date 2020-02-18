"""
Exploratory analysis of Virginia VS Purdue 2019 game closed captions.

@author: owenbezick
"""

# read in .txt file
f = open("VirginiaVSPurdue.txt", "r")

# read file object as closedCaptions
closedCaptions = f.read()

# remove punctuation 
import string # for string.puncutation
table = str.maketrans('','', string.punctuation)
stripped = closedCaptions.translate(table)

# tokenize
from nltk.tokenize import word_tokenize
tokens = word_tokenize(stripped)

# lowercase 
lower_tokens = [t.lower() for t in tokens]

# Get list of english stop words
from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))

# Filter the stopwords out
filtered_tokens = []
for t in lower_tokens:
    if t not in stopWords:
        filtered_tokens.append(t)

from nltk.stem import WordNetLemmatizer
# Instantiate the WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# Lemmatize all tokens into a new list: lemmatized
lemmatized_tokens = [wordnet_lemmatizer.lemmatize(t) for t in filtered_tokens]

from collections import Counter
bow = Counter(lemmatized_tokens)

print(bow.most_common(100))
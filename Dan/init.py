"""
EDA with the Virginia vs. Purdue game from 2019 March Madness

@author Dan Murphy
@date Monday, February 17th, 2019
"""
import pandas
import numpy
from matplotlib import pyplot as plt
import string

# open the file
f = open("/Users/danielmurphy/Desktop/Stratifyd_IS/datasets/VirginiaVSPurdue2019CC.txt", "r")
readFile = f.read()
# verify proper reading of file
# print(readFile)

"""
Part One: word and sentence tokenization. 
First, I will remove punctuation from the textual data. 
Then, I will tokenize the cleaned data into words and sentences
"""
tab = str.maketrans('', '', string.punctuation)  # removes nothing except for punctuation
removePunctuation = readFile.translate(tab)

#tokenize sentences
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk

words = word_tokenize(removePunctuation) # word tokenization
phrases = sent_tokenize(removePunctuation) # sentence tokenization
lower_words = [t.lower() for t in words]
lower_sentences = (t.lower() for t in phrases)

"""
Part Two: Modify our cleaned data to now remove stop words
"""
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
new_words = word_tokenize(removePunctuation)
filtered_words = []

for word in new_words:
    if word not in stop_words:
        filtered_words.append(word)
print(len(new_words))
print(len(filtered_words))
print(len(new_words) - len(filtered_words))

# filtered words are now stored in filtered_words array
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
words_without_punctuation = word_tokenize(removePunctuation)
filtered_words = []

for word in words_without_punctuation:
    if word not in stop_words: #remove stop words
        if word not in filtered_words: #remove repeats. filtered_words is the same as words_Without_punctuation except it does not contain repeats
            filtered_words.append(word)
print(len(words_without_punctuation))
print(len(filtered_words))
print(len(words_without_punctuation) - len(filtered_words))
# filtered words are now stored in filtered_words array

"""
Part Three: Stemming words using nltk.stem -> PorterStemmer
"""
from nltk.stem import PorterStemmer

porter_stemmer = PorterStemmer()

for word in filtered_words:
    print(word + ": " + porter_stemmer.stem(word))


count_applause =0
count_music = 0 
for word in words:
    if word == "Applause":
        count_applause += 1
    elif word == "Music":
        count_music += 1

non_conversational_data = count_applause + count_music

"""
Part Four: Graphing histogram of number of applauses and number of music segments

Work in Progress
"""
import streamlit 
import matplotlib.pyplot as plt

plt.hist([count_applause, count_music])
plt.show()
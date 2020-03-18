#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 12:20:47 2020

@author: malcolmmccabe
"""
import os
import nltk
from collections import Counter 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

'''This code analyzes the most common words in a text file'''

#Open and read file
#Democratic Debate File
'''
file = open("/Users/malcolmmccabe/Desktop/Python File/Democratic_Debate_NH.txt", 'r')
myfile = file.read()
'''

file = open("/Users/malcolmmccabe/Desktop/Python File/VirginiaVSPurdue.txt", 'r')
myfile = file.read()

#Split file into words
tokens = nltk.word_tokenize(myfile)

#Normalize words by lowercasing all
lower_tokens = [w.lower() for w in tokens]

#Eliminate non-alpha tokens
alpha_only = [t for t in lower_tokens if t.isalpha()]

#Eliminate stop words 
no_stops = [t for t in alpha_only if t not in stopwords.words('english')]

#Instantiate WordNetLemmatizer
wnl = WordNetLemmatizer()

#Lemmatize tokens
lemmatized = [wnl.lemmatize(t) for t in no_stops]

#Count tokens 
bow = Counter(lemmatized)

#Print 10 most common 
print(bow.most_common(50))

'''
#Eliminates punctuation
words = [word for word in tokens if word.isalpha()]

#Eliminates stop words 
stop_words = stopwords.words('english')
words = [w for w in words if w not in stop_words]

#Prints most common words in Debate Transcript 
bow_simple = Counter(words)
print(bow_simple.most_common(10))
'''
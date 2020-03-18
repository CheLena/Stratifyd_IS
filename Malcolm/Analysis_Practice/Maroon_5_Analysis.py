#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 11:45:27 2020

@author: malcolmmccabe
"""

import os
import nltk
from collections import Counter 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import spacy


file = open("/Users/malcolmmccabe/Desktop/Python File/Text Files/Maroon 5 Text/Lost Stars.txt", 'r')
lyrics = file.read()
#print(lyrics)

tokens = nltk.word_tokenize(lyrics)
#print(tokens)

lower_tokens = [w.lower() for w in tokens]
#print(lower_tokens)

alpha_only = [t for t in lower_tokens if t.isalpha()]
#print(alpha_only)

no_stops = [t for t in alpha_only if t not in stopwords.words('english')]
#print(no_stops)

wnl = WordNetLemmatizer()

lemmatized = [wnl.lemmatize(t) for t in no_stops]

bow = Counter(lemmatized)
#print(bow.most_common(20))

nlp = spacy.load('en_core_web_sm', tagger=False, parser=False, matcher=False)

#Create new document
doc = nlp(lyrics)

for ent in doc.ents:
    print(ent.label_, ent.text)
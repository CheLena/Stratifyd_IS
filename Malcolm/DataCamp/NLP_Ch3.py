#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:16:36 2020

@author: malcolmmccabe
"""

"""
Name Entity Recognition (NER):
    - identity people, places, etc.
    - used for topic identification
"""

import nltk
from scrapy import Selector
import requests 
from collections import defaultdict
import matplotlib.pyplot as plt

sentence = "In New York, I like to ride the Metro to visit Moma\
            and some restaurants rated well by Ruth Reichl."
#Tokenize sentence
tokenized_sent = nltk.word_tokenize(sentence)

#Tags tokens
tagged_sent = nltk.pos_tag(tokenized_sent)

#Displays first three words and its corresponding tag
#print(tagged_sent[:3])

#Exercise

url = 'https://www.investopedia.com/articles/personal-finance/111015/story-uber.asp'
html = requests.get(url).content

sel = Selector(text = html)

article = str(sel.xpath('//*[@class="comp mntl-sc-block finance-sc-block-html'\
                              ' mntl-sc-block-html"]//text()').extract())
#Tokenize article into sentences
sentences = nltk.sent_tokenize(article)

#print(sentences)

#Tokenize each sentence into words
token_sentences = [nltk.word_tokenize(sent) for sent in sentences]
#print(token_sentences)

#Tag each tokenized sentence into parts of speech
pos_sentences = [nltk.pos_tag(sent) for sent in token_sentences]
#print(pos_sentences)

#Creates named entity chunks
chunked_sentences = nltk.ne_chunk_sents(pos_sentences, binary=True)

#print(chunked_sentences)

#Test if named entity chunk has label = 'NN'
'''
for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, 'label') and chunk.label() == 'NE':
            print(chunk)
'''

#Creates defaultdict
ner_categories = defaultdict(int)

#Create nested for loop
for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, 'label'):
            ner_categories[chunk.label()] += 1
 
#Create list from dictionary keys for chart labels           
labels = list(ner_categories.keys())

#Create list of values
values = [ner_categories.get(v) for v in labels]

#Create Pie Chart 
#plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)

#Show Pie Chart 
#plt.show()

'''
Intro to Spacy
'''

import spacy 

#Instantiate English model
nlp = spacy.load('en_core_web_sm', tagger=False, parser=False, matcher=False)

#Create new document
doc = nlp(article)

#Print all found entities and their labels
#for ent in doc.ents:
 #   print(ent.label_, ent.text)

'''
Intro to Polyglot
* Supports many languages
*** I HAD PROBLEMS DOWNLOADING POLYGLOT MODULE
''' 
import polyglot
from polyglot.text import Text

text = 'El presidente de la Generalitat de Cataluña,\
        Carles Puigdemont, ha afirmado hoy a la alcaldesa\
        de Madrid, Manuela Carmena, que en su etapa de\
        alcalde de Girona (de julio de 2011 a enero de 2016)\
        hizo una gran promoción de Madrid.'
        
poly_txt = Text(text)

for ent in poly_txt.entities:
    print(ent)
    



            

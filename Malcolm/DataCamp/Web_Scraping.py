#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:35:05 2020

@author: malcolmmccabe
"""

"""
Web Scraping Practice
"""

from scrapy import Selector 
import requests
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

url = 'https://www.investopedia.com/articles/personal-finance/111015/story-uber.asp'
html = requests.get(url).content

sel = Selector(text = html)

article = str(sel.xpath('//*[@class="comp mntl-sc-block finance-sc-block-html'\
                              ' mntl-sc-block-html"]//text()').extract())

#Tokenize article 
tokens = word_tokenize(article)

#Lowercase tokens 
lower_tokens = [t.lower() for t in tokens]

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
print(bow.most_common(10))





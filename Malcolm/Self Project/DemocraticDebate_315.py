#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updated on Mon Apr 27 15:23:07 2020

@author: Malcolm McCabe
"""

"""
Democratic Debate Analysis 3/15
"""



#Web Scraping Packages
from scrapy import Selector 
import requests

#Preproessing Packages
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

#Text Summarization Packages
import heapq

#Sentiment Analysis Packages
from textblob import TextBlob

#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#Data Visualizaiton Packages
from wordcloud import WordCloud
import matplotlib.pyplot as plt



'''
#Pt. 1 - Web Scraping
'''

url = ('https://www.rev.com/blog/transcripts/march-democratic-debate-'
       'transcript-joe-biden-bernie-sanders')

html = requests.get(url).content

sel = Selector(text = html)

article = str(sel.xpath('//*[@class="fl-callout-text"]//text()').extract())


'''
#Pt. 2 - Preprocessing
'''

#Tokenize article by words
tokens = word_tokenize(article)

sentences = sent_tokenize(article)

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

#Print most common 
print(bow.most_common(10))

print()


'''
#Pt. 3 - Text Summarization
'''

#Find weighted occurence frequency (similar to bow) 
word_frequencies = {}
for word in no_stops: 
    if word not in word_frequencies.keys():
        word_frequencies[word] = 1 
    else:
        word_frequencies[word] += 1
        
#To find word frequency, word_frequency/max_frequency
max_frequency = max(word_frequencies.values())
for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/max_frequency)

#Now calculate sentence score frequency
sentence_scores = {}
for sent in sentences:
    if sent not in sentence_scores.keys():
        sentence_scores[sent] = word_frequencies[word]
    else:
        sentence_scores[sent] += word_frequencies[word]

#Generating summary       
summary_sentences = heapq.nlargest(10, sentence_scores, 
                                   key=sentence_scores.get)
summary = ' '.join(summary_sentences)
print("Text Summary: " + summary)

print()


'''
#Pt. 4 - Sentiment Analysis
'''

blob = TextBlob(article)
sas = blob.sentiment
print(sas)

print()


'''
#Pt. 5 - Data Visualization
'''

#5.1 - Graphing word clouds -- shows most common words 

#Generate word cloud
wordcloud = WordCloud(width=600, height=600, background_color='white', 
                      min_font_size=10).generate_from_frequencies(bow)

#Plot word cloud 
plt.figure(figsize = (6,6), facecolor = None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad = 0)

plt.show()


#5.2 - Graphing who spoke the most

#Web scrape for timestamps
timestamps = list(sel.xpath('//*[@class="fl-callout-text"]//p//a/text()')\
                 .extract())

#Convert timestamps from MM:SS to seconds 
seconds_list = []
for ts in timestamps:
    seconds_list.append(sum(int(x) * 60  ** i  for i,x in enumerate
                        (reversed(ts.split(':')))))

#Web scrape for names that are tied to timestamps     
names = list(sel.xpath('//*[@class="fl-callout-text"]//p//text()')\
             .extract())

#Filter for names 
filtered_names = []
for name in names:
    if 'Jake Tapper: (' in name:
        filtered_names.append(name[:-3])
    if 'Dana Bash: (' in name:
        filtered_names.append(name[:-3])
    if 'Ilia Calderón: (' in name:
        filtered_names.append(name[:-3])
    if 'Joe Biden: (' in name:
        filtered_names.append(name[:-3])
    if 'Bernie Sanders: (' in name:
        filtered_names.append(name[:-3])
    if 'Dr. Sanjay Gupta: (' in name:
        filtered_names.append(name[:-3])
    if 'Amy Langenfeld: (' in name:
        filtered_names.append(name[:-3])
        
       
#Combine lists -- name_time_lst format (filtered_name, seconds_list)
name_time_lst = [list(a) for a in zip(filtered_names, seconds_list)]

#Create dictionary with format {names : number of seconds spoken}
#There were three parts to the debate, restarting the timestamps. That is 
#why I include the first if statement. 

name_time_dict = {}

for n in range(0, len(name_time_lst)-1):
    if (name_time_lst[n+1][1]) > (name_time_lst[n][1]):
        if name_time_lst[n][0] not in name_time_dict:
            name_time_dict[name_time_lst[n][0]] = name_time_lst[n+1][1]-\
            name_time_lst[n][1]
        else:
            name_time_dict[name_time_lst[n][0]] += name_time_lst[n+1][1]-\
            name_time_lst[n][1]


#Plotting graph         
names = name_time_dict.keys()
num_seconds = name_time_dict.values()

plt.bar(names, num_seconds)
plt.xlabel('Person')
plt.xticks(rotation=90)
plt.ylabel('Number of Seconds Spoken')
plt.title('Who Spoke the Most?')
plt.show()    


#5.3 - Dispersion Plot -- illustrates speaking tradeoff between two candidates

fig = plt.subplots(figsize=(10,8))
nltk.draw.dispersion_plot(lemmatized, ['biden', 'sander'])



'''
Section 5 - Bigram Analysis
'''

#Use lemmatized pre-processed text to find bigrams
bigram = list(nltk.bigrams(no_stops))

#Convert tuples to string and create bigram strings
bigram_string = []

for pair in bigram:
    combine = ' '.join(pair)
    bigram_string.append(combine)


#Find most common bigrams
pair_counter = {}

for pair in bigram_string:
     if pair in pair_counter:
         pair_counter[pair] += 1
     else:
         pair_counter[pair] = 1

popular_pairs = sorted(pair_counter, key=pair_counter.get, reverse=True)
most_popular= popular_pairs[:5]
print(most_popular)

#Generate and plot word cloud  
wordcloud = WordCloud(width=600, height=600, background_color='white', 
                      min_font_size=10).generate_from_frequencies(pair_counter)

plt.figure(figsize = (6,6), facecolor = None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad = 0)

plt.show()


'''
Section 6 - Trigrams
'''

#Define trigrams
trigrams = list(nltk.trigrams(no_stops))

#Convert "tri-elements" to trigram strings
trigram_string = []

for triple in trigrams:
    combine = ' '.join(triple)
    trigram_string.append(combine)

#Find most common trigrams
tri_counter = {}

for triple in trigram_string:
    if triple in tri_counter:
        tri_counter[triple] += 1
    else:
        tri_counter[triple] = 1
        
popular_triples = sorted(tri_counter, key=tri_counter.get, reverse=True)
tri_most_popular = popular_triples[:20]
print(tri_most_popular)
    

    
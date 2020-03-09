#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:37:55 2020

@author: malcolmmccabe
"""

"""
Purdue v. Virginia Data Analysis
"""

import pandas as pd 
import matplotlib.pyplot as plt
import os
import nltk
from collections import Counter 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#Read in CSV as dataframe. Remove first column
df = pd.read_csv('PurdueData.csv')

#Remove last column 
df = df[:-1]

'''
column_list1 = ['PTS']
df[column_list1].plot(kind='bar')
plt.show()
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
#print(bow.most_common(50))

#problems with doing this: sometimes first and last name is said at same time,
#so we are double counting. 
#closed captions don't always spell players' names correclty 

names_dict = {}
 
for k,v in bow.items():
    if k == 'edward' or k == 'carson':
        names_dict['Carsen Edwards'] = bow.get('edward') + bow.get('carson')
            
    if k == 'ryan' or k == 'klein':
        names_dict['Ryan Cline'] = bow.get('ryan') + bow.get('klein')
       
    if k == 'matt' or k == 'harm':
        names_dict['Matt Haarms'] = bow.get('matt') + bow.get('harm')
    
    #this one was tough - no jail, no jelly 
    if k == 'eastern':
        names_dict['Nojel Eastern'] = bow.get('eastern')
        
    if k == 'grady' or k == 'eyford':
        names_dict['Grady Eifert'] = bow.get('grady') + bow.get('eyford')
        
    if k == 'aaron' or k == 'wheeler':
        names_dict['Aaron Wheeler'] = bow.get('aaron') + bow.get('wheeler')
    
    if k == 'treyvion' or k == 'williams':
        names_dict['Trevion Williams'] = bow.get('treyvion') + bow.get('williams')
    
    #problems with this one is there is another hunter
    if k == 'eric' or k == 'hunter': 
        names_dict['Eric Hunter Jr.'] = bow.get('eric') + bow.get('hunter')
    
    if k == 'sasha' or k == 'stefanovic':
        names_dict['Sasha Stefanovic'] = bow.get('sasha') + bow.get('stefanovic')
        

print(names_dict)

#Maps dictionary values with players in dataframe
df['Times_Name_Said'] = df['Starters'].map(names_dict)

print(df)

#Bar Graph with axis set equal to Times Name Said and Minutes Played
bar_graph = plt.figure()

ax = bar_graph.add_subplot(111)
ax2 = ax.twinx()

width = 0.3

df.MP.plot(kind='bar', color='red', ax=ax, width=width, position=1)
df.Times_Name_Said.plot(kind='bar', color='blue', ax=ax2, width=width, position=0)

ax.set_ylabel('Minutes Played')
ax2.set_ylabel('Times Name Said')
ax.set_xticklabels(df['Starters'])

plt.show()

team_dict = {}

for k,v in bow.items():
    if k == 'virginia':
        team_dict['Virginia'] = bow.get('virginia')
    
    if k == 'perdue' or k == 'purdue':
        team_dict['Purdue'] = bow.get('perdue') + bow.get('perdue')

print(team_dict)


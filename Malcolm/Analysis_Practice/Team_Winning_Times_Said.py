#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:06:52 2020

@author: malcolmmccabe
"""

import os
import nltk
from collections import Counter 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


file = open("/Users/malcolmmccabe/Desktop/Python File/Text Files/VirginiaVSPurdue.txt", 'r')
file1 = open("/Users/malcolmmccabe/Desktop/Python File/Text Files/DukeVsUCF.txt", 'r')
file2 = open("/Users/malcolmmccabe/Desktop/Python File/Text Files/MichiganVsHouston.txt",'r')
file3 = open("/Users/malcolmmccabe/Desktop/Python File/Text Files/KentuckyVsHouston.txt",'r')
file4 = open("/Users/malcolmmccabe/Desktop/Python File/Text Files/VirginiaVsAuburn.txt",'r')

 
list_of_files = [file, file1, file2, file3, file4]

for file in list_of_files:
    
    read_file = file.read()
    
    #Split file into words
    tokens = nltk.word_tokenize(read_file)
    
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
    #print()
    
    team_dict = {}
    
    for k,v in bow.items():
        if 'virginia' in bow:
            team_dict['Virginia'] = bow['virginia']
            
        if 'ucf' in bow:
            team_dict['UCF'] = bow['ucf']
            
        if 'perdue' or 'purdue' in bow:
            team_dict['Purdue'] = bow['perdue'] + bow['purdue']
            
        if 'duke' in bow:
            team_dict['Duke'] = bow['duke']
        
        if 'auburn' in bow:
            team_dict['Auburn'] = bow['auburn']
            
        if 'houston' in bow:
            team_dict['Houston'] = bow['houston']
            
        if 'michigan' in bow:
            team_dict['Michigan'] = bow['michigan']
            
        if 'kentucky' in bow:
            team_dict['Kentucky'] = bow['kentucky']
    
            
    print(team_dict)
    print()
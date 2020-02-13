#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:53:35 2020

@author: malcolmmccabe

Intro to NLP - Ch. 2 Notes
"""

from nltk.tokenize import word_tokenize
from collections import Counter

#Counter allows to see each token and its frequency
Counter(word_tokenize("The cat is in the box. The cat likes the box.\
                      The box is over the cat."))

#Returns the 3 most frequent tokens 
#Counter.most_common(3)

article = "The terms 'bug' and 'debugging' are attributed to Admiral Grace \
\n Hopper in the 1940s.[1] While she was working on a Mark II computer at \
\n Harvard University, her associates discovered a moth stuck in a relay and \
\n thereby impeding operation, whereupon she remarked that they were \
\n'debugging' the system. However, the term 'bug', in the sense of 'technical \
\n error', dates back at least to 1878 and Thomas Edison (see software bug \
\n for a full discussion). Similarly, the term 'debugging' seems to have been \
\n used as a term in aeronautics before entering the world of computers. \
\n Indeed, in an interview Grace Hopper remarked that she was not coining the\
\n term. The moth fit the already existing terminology, so it was saved. A \
\n letter from J. Robert Oppenheimer (director of the WWII atomic bomb \
\n Manhattan' project at Los Alamos, NM) used the term in a letter to Dr. \
\n Ernest Lawrence at UC Berkeley, dated October 27, 1944,[2] regarding the \
\n recruitment of additional technical staff. The Oxford English Dictionary \
\n entry for 'debug' quotes the term 'debugging' used in reference to \
\n airplaneengine testing in a 1945 article in the Journal of the Royal \
\n Aeronautical Society. An article in 'Airforce'(June 1945 p. 50) also \
\n refers to debugging, this time of aircraft cameras. Hopper's bug was \
\n found on September 9, 1947. Computer programmers did not adopt the term \
\n until the early 1950s. The seminal article by Gill[3] in 1951 is the \
\n earliest in-depth discussion of programming errors, but it does not use \
\n the term 'bug' or 'debugging'. In the ACM's digital library, the term \
\n 'debugging' is first used in three papers from 1952 ACM National \
\n Meetings. Two of the three use the term in quotation marks. By 1963 \
\n 'debugging' was a common-enough term to be mentioned in passing without \
\n explanation on page 1 of the CTSS manual. Kidwell's article Stalking \
\n the Elusive Computer Bug[8] discusses the etymology of 'bug' and 'debug' \
\n in greater detail."

#tokenize article by words
tokens = word_tokenize(article)

#Standardize tokens by converting all to lowercase
lower_tokens = [t.lower() for t in tokens]

#Create Counter of lowercase tokens
bow_simple = Counter(lower_tokens)

#Prints the 10 most frequent tokens
print(bow_simple.most_common(10))

'''
Text Preprocessing and Removing Stopwords
'''

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#WordNetLemmatizer function returns base of word
wnl = WordNetLemmatizer()
print(wnl.lemmatize('dogs')) #Prints dog
print(wnl.lemmatize('wolves')) #Prints wolf 

#Eliminates non-alpha characters
alpha_only = [t for t in lower_tokens if t.isalpha()]

#Creates variable of english stopwords
english_stops = stopwords.words('english')

#Removes stop words 
no_stops = [t for t in alpha_only if t not in english_stops]


#Instantiate WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

#Lemmatize tokens into new list: lemmatized
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

#Creates bag of words: bow
bow = Counter(lemmatized)

#Prints 10 most frequent tokens
print(bow.most_common(10))

'''
Gensim Introduction

Used for building document/word vectors and perform topic identification
'''

from gensim.corpora.dictionary import Dictionary 

#Dataset I am working with in this section
movie_reviews = ['The movie was about a spaceship and aliens.',
                 'I really liked the movie!',
                 'Awesome action scenes, but boring characters.',
                 'The movie was awful! I hate alien films.',
                 'Space is cool! I liked the movie.',
                 'More space films, please!',]

#Tokenize reviews
tokenized_reviews = [word_tokenize(doc.lower()) for doc in movie_reviews]

#Cretes dictionary of tokenized_reviews
dictionary = Dictionary(tokenized_reviews)

#Create gensim corpus
#Each list item structured as tuple (token id from dictionary, token frequency)
corpus = [dictionary.doc2bow(review) for review in tokenized_reviews]
print(corpus)

'''
This next section uses gensim to see most 
common terms per review and across all reviews
'''

#Save 3rd review: rev
rev = corpus[2]

#Sort the review for frequency: bow_doc
bow_rev = sorted(rev, key=lambda w: w[1], reverse = True)

#Print top 5 words of the review alongside count
for word_id, word_count in bow_rev[:5]:
    print(dictionary.get(word_id), word_count)
    
'''
Tf-idf with gensim

Stands for term frequency - inverse document frequency
Allows you to determine most important words in text 
Ex. astronomer might not find sky important, so need to downweight it

*** weight of token = # occurences of token * (log(# of documents/# documents containing token)
'''

from gensim.models.tfidfmodel import TfidfModel 

#Create TfidfModel using corpus
tfidf = TfidfModel(corpus)

#Calculate tfidf weights of rev
tfidf_weights = tfidf[rev]

#Print first 5 weights 
print(tfidf_weights[:5])

#Sort weights from highest to lowest 
sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)

#Print top 5 weighted words
for term_id, weight in sorted_tfidf_weights[:5]:
    print(dictionary.get(term_id), weight)




